#include <iostream>

using namespace std;

int b[200][2];
int a[200][2];
int a1,a2,b1,b2,c1,d1;
int c[1000];
int d[1000];
char s[100];

int t,i,u,k,j,m,n,x,z;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	t=0;
	cin>>z;
	while (z--)
	{
		t++;
		printf("Case #%d: ",t);
		scanf("%d%d%d",&k,&n,&m);

		for (i=0;i<n;i++)
		{
			scanf("%s",s);
			a1=s[0]-48;
			a2=s[1]-48;
			j=a1*10+a2;
			a1=s[3]-48;
			a2=s[4]-48;
			j=j*60;
			j+=a1*10+a2;
			a[i][0]=j;
			scanf("%s",s);
			a1=s[0]-48;
			a2=s[1]-48;
			j=a1*10+a2;
			a1=s[3]-48;
			a2=s[4]-48;
			j=j*60;
			j+=a1*10+a2;
			a[i][1]=j+k;
		}

		for (i=0;i<m;i++)
		{
			scanf("%s",s);
			a1=s[0]-48;
			a2=s[1]-48;
			j=a1*10+a2;
			a1=s[3]-48;
			a2=s[4]-48;
			j=j*60;
			j+=a1*10+a2;
			b[i][0]=j;
			scanf("%s",s);
			a1=s[0]-48;
			a2=s[1]-48;
			j=a1*10+a2;
			a1=s[3]-48;
			a2=s[4]-48;
			j=j*60;
			j+=a1*10+a2;
			b[i][1]=j+k;
		}

		b1=0;b2=0;
		a1=0;a2=0;
		k=60*24;
		for (i=0;i<k;i++)
		{
			if (i==12*60)
				i=i;
			for (u=0;u<m;u++) if (b[u][1]==i)
			{
				a1++;
			}
			for (u=0;u<n;u++) if (a[u][0]==i)
			{
				if (a1)
					a1--;
				else 
				{
					b1++;
				}
			}

			for (u=0;u<n;u++) if (a[u][1]==i)
			{
				a2++;
			}
			for (u=0;u<m;u++) if (b[u][0]==i)
			{
				if (a2)
					a2--;
				else 
				{
					b2++;
				}
			}
		}
		printf("%d %d\n",b1,b2);
	}
	return 0;
}






