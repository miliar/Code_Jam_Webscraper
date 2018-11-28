#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <stack>
#include <map>
#include <cmath>
#include <ctime>
#include <memory.h>
using namespace std;

#ifdef MYDEBUG
#pragma comment(linker, "/stack:1000000000")
#endif

typedef pair<double,double> pii;
typedef long long LL;
typedef unsigned long long ULL;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define sz size()
#define mp make_pair
#define pb push_back
#define HAS(v,k) ((v).find(k)!=(v).end())
#define ALL(a) a.begin(),a.end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define sqr(a) ((a)*(a))
#define V(t) vector<t>
#define VV(t) V(V(t))

int mas[16][16];
pii mul(pii a,int b)
{
	return mp(a.first*b,a.second*b);
}
pii add(pii a,pii b)
{
	return mp(a.first+b.first,a.second+b.second);
}
pii sub(pii a,pii b)
{
	return mp(a.first-b.first,a.second-b.second);
}
int main()
{
#ifdef MYDEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	clock_t beg = clock();
#endif

	int T;
	scanf("%d",&T);
	FOR(t,0,T)
	{
		printf("Case #%d: ",t+1);
		int n,m,d;
		scanf("%d %d %d",&n,&m,&d);
		FOR(j,0,n)
		{
			string s;
			cin >>s;
			FOR(i,0,m)
			{
				mas[j][i]=(s[i]-'0')+d;
			}
		}
		int res=-1;
		for(int k=11;k>=3;--k)
		{
			if(res!=-1)break;
			FOR(dj,0,n-k+1)FOR(di,0,m-k+1)
			{
				pii v=mp(0.0,0.0);
				pii c=mp(k/2.0,k/2.0);
				FOR(j,0,k)FOR(i,0,k)
				{
					if((j==0 && i==0) || (j==k-1 && i==0) || (j==0 && i==k-1) || (j==k-1 && i==k-1))continue;
					pii t=sub(mp((double)j+0.5,(double)i+0.5),c);
					t=mul(t,mas[dj+j][di+i]);
					v=add(v,t);
				}
				if((ABS(v.first)<1e-6) && (ABS(v.second)<1e-6))res=k;
			}
		}
		if(res==-1)printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
#ifdef MYDEBUG
    fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
	return 0;
}

