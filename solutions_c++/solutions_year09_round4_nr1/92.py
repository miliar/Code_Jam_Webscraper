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

int col[100],done[100];
char line[100][100];

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in\n","r",stdin); freopen("A-small-attempt1.out\n","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	int T,ks,i,j,c,ans,N;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&N);
		for(i=0;i<N;i++)
			scanf("%s",line[i]);

		for(i=0;i<N;i++) done[i]=0;

		ans=0;
		for(i=0;i<N;i++)
		{
			for(j=N-1;j>=0;j--) if(line[i][j]=='1') break;
			col[i]=j;
		}

		for(i=0;i<N;i++)
		{
			c=0;
			for(j=0;j<N;j++) if(done[j]==0)
			{
				c++;
				if(col[j]<=i) break;
			}

			ans+=c-1;
			done[j]=1;
		}

		printf("Case #%d: %d\n",ks,ans);

	}

	return 0;
}