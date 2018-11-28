#pragma warning(disable:4786)
#include<math.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<utility>
#include<algorithm>
#include<string.h>
#include<stdio.h>
#include<set>
#include<stdlib.h>
#include<sstream>
#include<functional>
#include<queue>
#include<stack>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define ABS(A) ((A)>0?(A):(-(A)))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;
typedef __int64 LL;

//int dr[]={-1,0,1,0};
//int dc[]={0,1,0,-1};
//int dr[]={-2,-2,-1,1,2,2,1,-1};
//int dc[]={-1,1,2,2,1,-1,-2,-2};

int x[10],y[10],r[10];

double cover(int a,int b)
{
	return (sqrt( S(x[a]-x[b]) + S(y[a]-y[b]) ) + r[a] + r[b])/2.;


}

int main()
{
	freopen("D-small-attempt0.in","r",stdin); freopen("D-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in\n","r",stdin); freopen("A-small-attempt1.out\n","w",stdout);
//	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	double ans,temp;
	int T,ks,N,i;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		}

		ans=0;
		if(N==1)
		{
			ans = r[0];
		}
		else if(N==2)
		{
			ans = MAX(r[0],r[1]);
		}
		else if(N==3)
		{
			temp=cover(1,2);
			ans=MAX(r[0],temp);
			temp=cover(0,2);
			ans=MIN(ans,MAX(r[1],temp));
			temp=cover(0,1);
			ans=MIN(ans,MAX(r[2],temp));
		}

		printf("Case #%d: %.6lf\n",ks,ans);


	}

	return 0;
}