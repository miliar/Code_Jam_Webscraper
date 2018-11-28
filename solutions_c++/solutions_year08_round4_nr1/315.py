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

#define MAX_M 10000
#define INF 1000000000


int tree[MAX_M+10][2],n,m,v,a,b,c,h[MAX_M+10],r[MAX_M+10];

int main()
{
	scanf("%d",&n);
	REP(i,n)
	{
		scanf("%d%d",&m,&v);
		REP(j,(m-1)/2)
			scanf("%d%d",&r[j+1],&h[j+1]);
		REP(j,m+1)
			REP(k,2)
				tree[j][k]=INF;
		REP(j,(m+1)/2)
		{
			scanf("%d",&a);
			tree[m-(m+1)/2+1+j][a]=0;
		}
		deb(FUP(i,1,m)printf("(%d %d %d r=%d h=%d)\n",i,tree[i][0],tree[i][1],r[i],h[i]););
		b=m-(m+1)/2;
		FDN(j,b,1)
		{
			if((h[j] && (r[j])) || (!r[j]))
			{
				tree[j][0]=MINN(tree[j][0],tree[2*j][0]+tree[2*j+1][0]+(r[j]==1));
				tree[j][1]=MINN(tree[j][1],MINN(tree[2*j][0]+tree[2*j+1][1],MINN(tree[2*j][1]+tree[2*j+1][0],tree[2*j][1]+tree[2*j+1][1]))+(r[j]==1));
			}
			if((h[j] && (!r[j])) || (r[j]))
			{
				tree[j][1]=MINN(tree[j][1],tree[2*j][1]+tree[2*j+1][1]+(r[j]==0));
				tree[j][0]=MINN(tree[j][0],MINN(tree[2*j][0]+tree[2*j+1][0],MINN(tree[2*j][1]+tree[2*j+1][0],tree[2*j][0]+tree[2*j+1][1]))+(r[j]==0));
			}
		}
		deb(FUP(i,1,m)printf("(%d %d %d)\n",i,tree[i][0],tree[i][1]);printf("\n\n"););
		printf("Case #%d: ",i+1);
		if(tree[1][v]!=INF)
			printf("%d\n",tree[1][v]);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
