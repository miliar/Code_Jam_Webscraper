#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <string>
#include <cmath>

using namespace std;

int i,u,k,j,m,n,x,z,t;
char s[100];
bool a[6021][6021];
int b[4][2]={0,1,1,0,0,-1,-1,0};
int a1,a2;
int b1,b2;
int ans,yes;
int c1,c2,d1,d2;

int main()
{
	freopen("A-small-attempt5.in","r",stdin);
	freopen("1.out","w",stdout);
	t=0;
	b1=6020;b2=3010;
	scanf("%d",&z);
	for (i=0;i<b1;i++) for (u=0;u<b1;u++) a[i][u]=0;
	while (z--)
	{
		t++;
		
		k=0;
		a1=a2=b2;
		scanf("%d",&n);
		a[a1][a2]=1;
		c1=c2=d1=d2=b2;
		for (i=0;i<n;i++)
		{
			scanf("%s%d",&s,&m);
			for (u=0;u<m;u++)
			{
				j=0;
				while (s[j])
				{
					if (s[j]=='F')
					{
						a1+=b[k][0];
						a2+=b[k][1];
						a[a1][a2]=1;
						a1+=b[k][0];
						a2+=b[k][1];
						a[a1][a2]=1;
						
						if (a1<c1) c1=a1;
						if (a1>c2) c2=a1;
						if (a2<d1) d1=a2;
						if (a2>d2) d2=a2;

					}
					else if (s[j]=='R')
					{
						k++;
						if (k==4) k=0;
					}
					else 
					{
						k--;
						if (k==-1) k=3;
					}
					j++;
				}
			}
		}

		ans=0;

		for (i=c1+1;i<=c2;i+=2) for (u=d1+1;u<=d2;u+=2)
			if (!a[i][u])
			{
				yes=1;
				x=0;
				for (j=c1;j<i;j+=2) if (a[j][u]) x++;
				if (x%2) yes=0;
				if (yes)
				{
					yes=0;
					for (j=i-1;j>=c1;j-=2) if (a[j][u]) 
					{
						yes++;
						break;
					}
					for (j=i+1;j<=c2;j+=2) if (a[j][u])
					{
						yes++;
						break;
					}
					if (yes==2) 
					{
						ans++;
						continue;
					}
					yes=0;
					for (j=u-1;j>=d1;j-=2) if (a[i][j])
					{
						yes++;
						break;
					}
					for (j=u+1;j<=d2;j+=2) if (a[i][j])
					{
						yes++;
						break;
					}
					if (yes&&yes%2==0)
					{
						ans++;
					}
				}
			}
		printf("Case #%d: %d\n",t,ans);
		for (i=c1;i<=c2;i++) for (u=d1;u<=d2;u++) a[i][u]=0;
	}

	return 0;
}