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

V(pii) mas; // (val,type)
V(int) A,B;
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
		A.clear();
		B.clear();
		mas.clear();
		FOR(i,0,n)
		{
			int a;
			string s;
			cin >>s >>a;
			if(s=="O")
			{
				mas.pb(mp(a,0));
				A.pb(a);
			}
			else
			{
				mas.pb(mp(a,1));
				B.pb(a);
			}
		}
		int res=0;
		int p1,p2;
		p1=p2=1;
		int it,i1,i2;
		it=i1=i2=0;
		while(it<n)
		{
			bool flag=true;
			if(mas[it].second==0)
			{
				while(flag)
				{
					++res;
					if(p1>mas[it].first)--p1;
					else if(p1<mas[it].first)++p1;
					else 
					{
						flag=false;
						++i1;
					}
					if(i2<B.sz)
					{
						if(p2>B[i2])--p2;
						else if(p2<B[i2])++p2;
					}
				}
			}
			else
			{
				while(flag)
				{
					++res;
					if(p2>mas[it].first)--p2;
					else if(p2<mas[it].first)++p2;
					else
					{
						flag=false;
						++i2;
					}
					if(i1<A.sz)
					{
						if(p1>A[i1])--p1;
						else if(p1<A[i1])++p1;
					}
				}
			}
			++it;
		}
		printf("%d\n",res);
	}
#ifdef MYDEBUG
    //fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
#endif
	return 0;
}
