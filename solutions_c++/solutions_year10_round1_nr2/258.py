#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>

using namespace std;

int C,D,I,M,N,limit,f[105][260],a[105];
bool used[260];

int min(int a,int b)
{
	if (a>b) return b;
	return a;
}
int max(int a,int b)
{
	if (a>b) return a;
	return b;
}
int abs(int a)
{
	if (a>0) return a;
	return -a;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&C);
	int T=0;
	while (C>0)
	{
		C--;T++;
		scanf("%d%d%d%d",&D,&I,&M,&N);

		limit=0;
		for (int i=1;i<=N;i++)
		{
			scanf("%d",&a[i]);
			if (a[i]>limit)
				limit=a[i];
		}

		memset(f,0,sizeof(f));
		for (int i=1;i<=N+1;i++)
		for (int j=0;j<=limit+1;j++)
			f[i][j]=100000000;

		for (int i=0;i<=N;i++)
		{
			if (i!=0)
			for (int j=0;j<=limit;j++)
			{
				int value=100000000;
				for (int k=max(j-M,0);k<=min(j+M,limit);k++)
					value=min(value,f[i-1][k]);
				f[i][j]=min(f[i][j],value+abs(a[i]-j));
			}

			memset(used,0,sizeof(used));
			for (int j=0;j<=limit;j++)
			{
				int u=-1;
				for (int k=0;k<=limit;k++)
				if (used[k]==false)
					if (u==-1)
						u=k;
					else
						if (f[i][k]<f[i][u])
							u=k;
				used[u]=true;
				for (int k=max(u-M,0);k<=min(u+M,limit);k++)
					f[i][k]=min(f[i][k],f[i][u]+I);
			}
			
			for (int j=0;j<=limit;j++)
				f[i+1][j]=min(f[i+1][j],f[i][j]+D);
		}

		int ans=100000000;
		for (int j=0;j<=limit;j++)
			ans=min(ans,f[N][j]);
		printf("Case #%d: %d\n",T,ans);
	}

	fclose(stdin);fclose(stdout);
	return 0;
}
