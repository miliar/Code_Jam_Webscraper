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
#define deb(A) //A
/////////////////

#define MAX_L 20

char L[MAX_L],Z[MAX_L],znak;
int n,il;
LL res;

bool ugly(LL a)
{
	a=abs(a);
	return (((a%2)==0) || ((a%3)==0) || ((a%5)==0) || ((a%7)==0));
}

void rek(int a, int b)
{
	if(a==b)
	{
		LL c=0,d=L[0]-'0';
		znak=1;
		FUP(j,1,a-1)
		{
			if(Z[j]==1)
			{
				c+=znak*d;
				d=L[j]-'0';
				znak =1;
			}
			if(Z[j]==-1)
			{
				c+=znak*d;
				d=L[j]-'0';
				znak = -1;
			}
			if(Z[j]==0)
			{
				d=(d*(LL)10)+L[j]-'0';
			}
		}
		c+=znak*d;
		deb(FUP(j,1,a-1)printf("z%d ",Z[j]);printf("%lld\n",c););
		if(ugly(c))
			res++;
		return;
	}
	Z[a]=1;
	rek(a+1,b);
	Z[a]=-1;
	rek(a+1,b);
	Z[a]=0;
	rek(a+1,b);
}

int main()
{
	scanf("%d\n",&n);
	REP(i,n)
	{
		gets(L);
		il = strlen(L);
		res=0;
		rek(1,il);
		printf("Case #%d: %lld\n",i+1,res);
	}
	return 0;
}
