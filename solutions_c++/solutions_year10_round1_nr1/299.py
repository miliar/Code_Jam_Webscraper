#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

char a[55][55];
bool visit[55][55];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int C,T=0,n,k;
	scanf("%d",&C);
	while (C>0)
	{
		C--;T++;
		scanf("%d%d",&n,&k);
		for (int i=1;i<=n;i++)
			scanf("%s",a[i]);

		for (int i=1;i<=n;i++)
		{
			int k=n-1;
			for (int j=n-1;j>=0;j--)
				if (a[i][j]!='.')
				{
					if (j!=k)
						a[i][k]=a[i][j],a[i][j]='.';
					k--;
				}
		}

		bool R=false,B=false;
		for (int j=0;j<n;j++)
		{
			int p=0,q=0;
			char last='.';
			for (int i=1;i<=n;i++)
			{
				if (a[i][j]!=last)
					p=q=0;
				p+=(a[i][j]=='R'),q+=(a[i][j]=='B');
				last=a[i][j];
				if (p>=k)
					R=true;
				if (q>=k)
					B=true;
			}
		}

		for (int i=1;i<=n;i++)
		{
			int p=0,q=0;
			char last='.';
			for (int j=0;j<n;j++)
			{
				if (a[i][j]!=last)
					p=q=0;
				p+=(a[i][j]=='R'),q+=(a[i][j]=='B');
				last=a[i][j];
				if (p>=k)
					R=true;
				if (q>=k)
					B=true;
			}
		}

		memset(visit,0,sizeof(visit));
		for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
		if (visit[i][j]==false)
		{
			int p=0,q=0;
			char last='.';
			for (int u=0;u<n*2;u++)
			{
				if ((i+u>n)||(j-u<0)) break;
				if (a[i+u][j-u]!=last)
					p=q=0;
				p+=(a[i+u][j-u]=='R'),q+=(a[i+u][j-u]=='B');
				visit[i+u][j-u]=true;
				last=a[i+u][j-u];
				if (p>=k)
					R=true;
				if (q>=k)
					B=true;
			}
		}

		memset(visit,0,sizeof(visit));
		for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
		if (visit[i][j]==false)
		{
			int p=0,q=0;
			char last='.';
			for (int u=0;u<n*2;u++)
			{
				if ((i+u>n)||(j+u>=n)) break;
				if (a[i+u][j+u]!=last)
					p=q=0;
				p+=(a[i+u][j+u]=='R'),q+=(a[i+u][j+u]=='B');
				visit[i+u][j+u]=true;
				last=a[i+u][j+u];
				if (p>=k)
					R=true;
				if (q>=k)
					B=true;
			}
		}
		
		if ((R==true)&&(B==true))
			printf("Case #%d: Both\n",T);
		else
		if ((R==false)&&(B==false))
			printf("Case #%d: Neither\n",T);
		else
		if ((R==true)&&(B==false))
			printf("Case #%d: Red\n",T);
		else
		if ((R==false)&&(B==true))
			printf("Case #%d: Blue\n",T);
	}
	fclose(stdin);fclose(stdout);
}
