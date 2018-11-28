#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

char happy[11][20000000];

char sv(int b, int v)
{
	char & a=happy[b][v];
	if(v==1) return a=1;
	if(a!=-1) return a;
	if(v>20000000-1) { P("gah");}
	
	//P(b) P(v)
	a=0;
	int nn=0;
	for(int p=1; p<=v; p*=b)
	{
		int d=(v/p)%b;
		nn+=d*d;
	}
	
	a=sv(b,nn);
	
	return a;
}

int main()
{
	int C, r,res;
	cin >> C;
	string ln;
	getline(cin,ln);
	
	memset(happy,-1,sizeof(happy));
	
	for(int cs=1; cs<=C; ++cs)
	{
		getline(cin,ln);
		istringstream in(ln);
		
		vector<int> b;
		while(in >> r) b.pB(r);
		//P(b);
		
		for(int i=2; ; ++i)
		{
			int y=1;
			R(j,b) if(!sv(b[j],i)) y=0;
			if(y) {res=i; break;}
		}
		
		
		cout << "Case #" << cs << ": " << res;
		
		cout << endl;
	}
	
	return 0;
}
