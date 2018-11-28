//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef double DD;
typedef long double LD;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FUP(I,A,B) for(int I=(A);I<=(B);I++)
#define FDN(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FALL(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define CLE(a,b) memset(a,b,sizeof(a))
#define MINN(a,b) ((a)>(b)?(b):(a))
#define MAXX(a,b) ((a)<(b)?(b):(a))
#define PB push_back
#define PF push_front
#define CB pop_back
#define CF pop_front
#define MP make_pair
#define FI first
#define SE second
#define SZ(X) ((int)(X.size()))
#define deb(A) A
/////////////////

#define MAX_L 1000

int n,p,k,l,L[MAX_L],c,r;
LL res;

bool cmp (const int & A, const int & B)
{
	return A > B;
}

int main()
{
	scanf("%d",&n);
	REP(i,n)
	{
		scanf("%d%d%d",&p,&k,&l);
		REP(j,l)
			scanf("%d",&L[j]);
		sort(L,L+l,cmp);
		printf("Case #%d: ",i+1);
		if(p*k<l)
			printf("Impossible\n");
		else
		{
			c=1;
			r=0;
			res=0;
			REP(j,l)
			{
				if(r==k)
				{
					r=0;
					c++;
				}
				r++;
				res += (LL)c*(LL)L[j];
			}
			printf("%lld\n",res);
		}
	}
	return 0;
}
