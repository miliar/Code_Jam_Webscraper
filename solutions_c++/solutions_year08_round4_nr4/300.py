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

#define MAX_N 1000
#define MAX_K 5


int k,n,s,res,p[MAX_K],a;
char W[MAX_N+10],W2[MAX_N+10];

int count()
{
	deb(REP(j,k)printf("%d ",p[j]););
	REP(i,s/k)
		REP(j,k)
			W2[k*i+j]=W[k*i+p[j]];
	deb(printf(" %s ",W2););
	int iw2,res=0;
	REP(i,s)
	{
		iw2=i;
		while((i+1<s)&&(W2[i+1]==W2[iw2]))
			i++;
		res++;
	}
	deb(printf("%d\n",res););
	return res;
}

int main()
{
	scanf("%d",&n);
	REP(i,n)
	{
		scanf("%d\n%s",&k,W);
		deb(printf("%s\n",W););
		s=strlen(W);
		REP(j,k)
			p[j]=j;
		res = count();
		while(next_permutation(p,p+k))
		{
			a=count();
			res = MINN(a,res);
		}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}
