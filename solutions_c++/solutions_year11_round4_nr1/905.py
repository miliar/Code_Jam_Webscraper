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

typedef pair<int,int> pii;
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

vector<pii > mas;
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
		int x,walk,run,trun,n;
		scanf("%d %d %d %d %d",&x,&walk,&run,&trun,&n);
		mas.clear();
		int dis=x;
		FOR(j,0,n)
		{
			int a,b,s;
			scanf("%d %d %d",&a,&b,&s);
			mas.pb(mp(s,b-a));
			dis-=b-a;
		}
		if(dis)
			mas.pb(mp(0,dis));
		sort(ALL(mas));
		//reverse(ALL(mas));
		double res=0;
		double time=trun;
		FOR(i,0,mas.sz)
		{
			double len=mas[i].second;
			if(len/(double)(mas[i].first+run)<=time)
			{
				res+=len/(double)(mas[i].first+run);
				time-=len/(double)(mas[i].first+run);
			}
			else
			{
				res+=time;
				len-=time*(mas[i].first+run);
				time=0;
				res+=len/(double)(mas[i].first+walk);
			}
		}
		printf("%.20lf\n",res);
	}
#ifdef MYDEBUG
    fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
	return 0;
}

