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
#define pb push_backs
#define HAS(v,k) ((v).find(k)!=(v).end())
#define ALL(a) a.begin(),a.end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define sqr(a) ((a)*(a))
#define V(t) vector<t>
#define VV(t) V(V(t))

LL gcd(LL a,LL b)
{
	if(b==0)return a;
	return gcd(b,a%b);
}
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
		LL pd,pg,n;
		cin >>n >>pd >>pg;
		if((pd==0 && pg!=0) || (pd!=0 && pg==0))
			printf("Broken\n");
		else if(pd==0 && pg==0)
			printf("Possible\n");
		else if((pd!=100 && pg==100))
			printf("Broken\n");
		else if(pd==100 && pg==100)
			printf("Possible\n");
		else
		{
			LL dg=gcd(100,pd);
			LL wd=pd/dg;
			LL d=100*wd/pd;
			/*dg=gcd(100,pg);
			LL wg=pg/dg;
			LL g=100*wg/pg;
			LL k=(d+g-1)/g;
			g*=k;*/
			if(d<=n)
				printf("Possible\n");
			else
				printf("Broken\n");
		}
	}
#ifdef MYDEBUG
    fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
	return 0;
}
