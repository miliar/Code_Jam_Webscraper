#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
using namespace std;

#define CLEAR(t) memset((t),0,sizeof(t))
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define ALL(X) (X).begin(),(X).end()
typedef long long ll;


int m, V, mm;
int t[10009];
bool zm[10009];

int mem[10009][2];

int go(int a, int s)
{
	if(a>mm)
	{
		//	printf("out %d s=%d t=%d\n", a,s,t[a]);
		if(s==t[a]) return 0;
		return 100000000;
	}
	int &ret=mem[a][s];
	if(ret!=-1) return ret;
	
	ret=100000000;
	
	REP(k,2)
	{
		if(k==1 && zm[a]) t[a]=!t[a];
		for(int i=0; i<4; i++)
		{
			int aa=i%2;
			int bb=i/2;
			if(t[a]==0 && !((aa||bb)==s)) continue;
			if(t[a]==1 && !((aa&&bb)==s)) continue;
			
			int w=go(a*2, aa) + go((a*2)+1, bb);
			if(k==1) w++;
			ret=min(ret,w);
		}
		if(k==1 && zm[a]) t[a]=!t[a];
	}
	
	//printf("go %d %d =>%d\n", a,s,ret);
	return ret;
}

int main()
{
	int _lz;
	scanf("%d", &_lz);
	for(int _z=1; _z<=_lz; _z++)
	{
		scanf("%d %d", &m, &V);
		FOR(i,1,((m-1)/2)+1)
		{
			int a,b;
			scanf("%d %d", &a, &b);
			t[i]=a;
			zm[i]=b;
		}
		mm=((m-1)/2);
		FOR(i,((m-1)/2)+1,m+1)
		{
			scanf("%d", &t[i]);
		}
		REP(i,10009) REP(j,2) mem[i][j]=-1;
		int ret=go(1,V);
		
		if(ret!=100000000) printf("Case #%d: %d\n", _z, ret);
		else printf("Case #%d: IMPOSSIBLE\n", _z);
	}
	return 0;
} 


