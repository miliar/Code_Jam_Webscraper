#include<stdio.h>
#include<string.h>
#include<math.h>

int f[101][260];
int a[101];

int main()
{
	int t,p;
	int d,s,m,n;
	int i,j,k;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d%d%d%d",&d,&s,&m,&n);
		for (i=1;i<=n;i++)
			scanf("%d",&a[i]);
		memset(f,-1,sizeof(f));
		for (i=0;i<=255;i++)
			f[0][i]=0;
		for (j=1;j<=n;j++)
		{
			if (a[j]>=m) i=a[j]-m;
			else i=0;
			for (;i<=a[j]+m&&i<=255;i++)
				if (f[j-1][i]>=0)
				{
					if (f[j][a[j]]==-1||f[j][a[j]]>f[j-1][i]) f[j][a[j]]=f[j-1][i];
				}
			for (k=0;k<=255;k++)
			{
				if (k>=m) i=k-m;
				else i=0;
				for (;i<=k+m&&i<=255;i++)
					if (f[j-1][i]>=0)
					{
						if (f[j][k]==-1||f[j][k]>f[j-1][i]+abs(k-a[j])) f[j][k]=f[j-1][i]+abs(k-a[j]);
					}
			}
			for (k=0;k<=255;k++)
				if (f[j-1][k]>=0)
				{
					if (f[j][k]==-1||f[j][k]>f[j-1][k]+d) f[j][k]=f[j-1][k]+d;
				}
			bool flag=true;
			while (flag)
			{
				flag=false;
				for (k=0;k<=255;k++)
				{
					if (k>=m) i=k-m;
					else i=0;
					for (;i<=k+m&&i<=255;i++)
						if (f[j][i]>=0)
						{
							if (f[j][k]==-1||f[j][k]>f[j][i]+s) 
							{
								f[j][k]=f[j][i]+s;
								flag=true;
							}
						}
				}
			}
		}
		int mm=-1;
		for (k=0;k<=255;k++)
			if (f[n][k]>=0)
			{
				if (mm==-1||mm>f[n][k]) mm=f[n][k];
			}
		printf("Case #%d: %d\n",p,mm);
	}
	return 0;
}


