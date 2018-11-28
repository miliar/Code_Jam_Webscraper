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


int main()
{
#ifdef MYDEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	clock_t beg = clock();
#endif

	int T;
	cin >>T;
	FOR(t,0,T)
	{
		printf("Case #%d: ",t+1);
		int n;
		scanf("%d",&n);
		int sum,m,xor;
		sum=xor=0;
		m=1<<30;
		FOR(i,0,n)
		{
			int a;
			scanf("%d",&a);
			m=MIN(m,a);
			sum+=a;
			xor^=a;
		}
		if(xor!=0)
			printf("NO\n");
		else
			printf("%d\n",sum-m);
	}
#ifdef MYDEBUG
    //fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
	return 0;
}
