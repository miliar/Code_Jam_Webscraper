#include <iostream>

using namespace std;

int a[20000][2];
int v[20000][2];

int i,u,k,j,m,n,x,z,V,t;
int a1,a2;

int main()
{
	z=0;
	t=0;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>z;
	while (z--)
	{
		t++;
		scanf("%d%d",&n,&V);
		m=(n-1)/2;
		for (i=0;i<m;i++)
		{
			scanf("%d%d",&k,&j);
			v[i][0]=k;
			v[i][1]=j;
		}
		for (;i<n;i++)
		{
			scanf("%d",&k);
			v[i][0]=k;
			a[i][0]=-1;
			a[i][1]=-1;
			a[i][k]=0;
			v[i][0]=0;
		}

		for (i=m-1;i>=0;i--)
		{
			k=i;
			a1=i*2+1;
			a2=a1+1;
			a[i][0]=-1;
			a[i][1]=-1;

			if (v[i][0])
			{
				if (a[a1][1]!=-1&&a[a2][1]!=-1)
				{
					a[i][1]=a[a1][1]+a[a2][1];
				}

				{
					x=-1;
					if (a[a1][0]!=-1&&a[a2][1]!=-1)
					{
						j=a[a1][0]+a[a2][1];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][0]!=-1&&a[a2][0]!=-1)
					{
						j=a[a1][0]+a[a2][0];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][1]!=-1&&a[a2][0]!=-1)
					{
						j=a[a1][1]+a[a2][0];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					a[i][0]=x;
				}
			}

			else 
			{
				if (a[a1][0]!=-1&&a[a2][0]!=-1)
				{
					a[i][0]=a[a1][0]+a[a2][0];
				}

				{
					x=-1;
					if (a[a1][0]!=-1&&a[a2][1]!=-1)
					{
						j=a[a1][0]+a[a2][1];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][1]!=-1&&a[a2][1]!=-1)
					{
						j=a[a1][1]+a[a2][1];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][1]!=-1&&a[a2][0]!=-1)
					{
						j=a[a1][1]+a[a2][0];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					a[i][1]=x;
				}
			}

			if (v[i][1])
			{
				v[i][0]++;
				if (v[i][0]>1) v[i][0]=0;
				if (v[i][0])
			{
				if (a[a1][1]!=-1&&a[a2][1]!=-1)
				{
					x=1+a[a1][1]+a[a2][1];
					if (a[i][1]>x||a[i][1]==-1) a[i][1]=x;
				}

				{
					x=-1;
					if (a[a1][0]!=-1&&a[a2][1]!=-1)
					{
						j=a[a1][0]+a[a2][1];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][0]!=-1&&a[a2][0]!=-1)
					{
						j=a[a1][0]+a[a2][0];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][1]!=-1&&a[a2][0]!=-1)
					{
						j=a[a1][1]+a[a2][0];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (x!=-1) x++;
					if (x!=-1&&(a[i][0]>x||a[i][0]==-1)) a[i][0]=x;
				}
			}

			else 
			{
				if (a[a1][0]!=-1&&a[a2][0]!=-1)
				{
					x=a[a1][0]+a[a2][0]+1;
					if (a[i][0]>x||a[i][0]==-1) a[i][0]=x;
				}

				{
					x=-1;
					if (a[a1][0]!=-1&&a[a2][1]!=-1)
					{
						j=a[a1][0]+a[a2][1];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][1]!=-1&&a[a2][1]!=-1)
					{
						j=a[a1][1]+a[a2][1];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (a[a1][1]!=-1&&a[a2][0]!=-1)
					{
						j=a[a1][1]+a[a2][0];
						if (x==-1) x=j;
						else if (j<x) x=j;
					}
					if (x!=-1) x++;
					if (x!=-1&&(a[i][1]==-1||a[i][1]>x)) 
					a[i][1]=x;
				}
			}
			}
		}
		printf("Case #%d: ",t);
		if (a[0][V]==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",a[0][V]);
		}
	return 0;
}







