#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[111][111],d[111],n;
double A[111],B[111],C[111];
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d",&n);
		memset(a,0,sizeof a);
		memset(d,0,sizeof d);
		for(int i=0;i<n;i++)A[i]=B[i]=C[i]=0;
		for(int i=0;i<n;i++)
		{
			char s[111];
			scanf("%s",s);
			for(int j=0;j<n;j++)
			{
				if(s[j]!='.')d[i]++;
				if(s[j]=='.')a[i][j]=0;
				if(s[j]=='0')a[i][j]=-1;
				if(s[j]=='1')a[i][j]=1;
			}
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(a[i][j]==1)A[i]+=1;
		for(int i=0;i<n;i++)A[i]/=d[i];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(a[i][j]!=0)B[i]+=(d[j]==1)?1:(A[j]*d[j]-((a[i][j]==-1)?1:0))/(d[j]-1);
		for(int i=0;i<n;i++)B[i]/=d[i];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(a[i][j]!=0)C[i]+=B[j];
		for(int i=0;i<n;i++)C[i]/=d[i];
		//for(int i=0;i<n;i++)printf("%d %.9lf %.9lf %.9lf\n",d[i],A[i],B[i],C[i]);
		printf("Case #%d:\n",__);
		for(int i=0;i<n;i++)printf("%.9lf\n",A[i]/4+B[i]/2+C[i]/4);
	}
	return 0;
}

