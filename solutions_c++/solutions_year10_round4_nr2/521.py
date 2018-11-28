#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <utility>
#include <sstream>
#include <cstring>

using namespace std;

typedef unsigned long long ll;

#define RP(i,s,e) for(int i=s;i<e;i++) 
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin();i!=(x).end();++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

const ll inf = 1e18;

int M[1<<10];
int p[11][1<<10];
int P;

ll v[12][1<<10][12];

ll get(int round, int match, int missr)
{
	if(missr<0) return inf;
	ll & a=v[round][match][missr];
	if(a!=-1) return a;
	if(round == 0)
	{
		if(missr<=M[match])
			return a=0;
		else return a=inf;
	}
	
	a=inf;
	a<?=get(round-1,match*2,missr)+get(round-1,match*2+1,missr)+p[round-1][match];
	a<?=get(round-1,match*2,missr+1)+get(round-1,match*2+1,missr+1);
	
	//cout << round << " " << match << " " << missr << " : " << a << endl;
	
	return a;
}

int main()
{
	int C;
	cin >> C;
	for(int cs=0;cs<C; ++cs)
	{
		cin >> P;
		//cout << P << endl << endl;
		RP(i,0,(1<<P)) cin >> M[i];
		RP(i,0,P) {
			int lm=1<<(P-i-1);
			//cout << lm << endl;
			for(int j=0; j<lm; ++j)
			{
				cin >> p[i][j];
				//cout << "Read " << p[i][j] << endl;
			}
		}
		
		memset(v,-1,sizeof(v));
		
		ll a=inf;
		a=get(P,0,0);
		
		cout << "Case #" << cs+1 << ": ";
		cout << a;
		cout << endl;
	}
	
	
}
