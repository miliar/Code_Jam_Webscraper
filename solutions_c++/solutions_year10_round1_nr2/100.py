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

int D,I,M,N;
int pix[1000];
int res[300][1000];


int sv(int pv, int p)
{
	int &r=res[pv][p];
	if(r!=-1) return r;
	if(p==0) return r=0;
	r=1e9;
	
	if(pv==256) r=sv(pv,p-1)+D;
	else
	{
		r=min(r,sv(pv,p-1)+D);
		r=min(r,sv(256,p-1)+D);
		
		int opv=pix[p-1];
		
		//Modify cost
		int mc=abs(opv-pv);
		
		for(int i=0; i<256; ++i)
		{
			int dif=abs(pv-i);
			int nd=0;
			if(dif > M){
				if(M==0) continue;
				nd=((dif-1)/M)*I;//+min(dif%M,I);
			}
			
			r=min(r,sv(i,p-1)+mc+nd);
		}
	}
	
	//if(pv<10) cout << p << " " << pv << " " << r << endl;
	
	return r;
}


int main()
{
	int C;
	cin >> C;
	for(int cs=0; cs<C; ++cs)
	{
		
		cin >> D >> I >> M >> N;
		memset(res,-1,sizeof(res));
		
		RP(i,0,N) cin >> pix[i];
		
		int mn=1e9;
		//CHECK
		RP(i,0,257) mn=min(mn, sv(i,N));
		
		cout << "Case #" << cs+1 << ": ";
		cout << mn;
		cout << endl;
	}
}


