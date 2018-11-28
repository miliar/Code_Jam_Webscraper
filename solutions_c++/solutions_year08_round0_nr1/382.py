#include <iostream>
#include <cstring>
#define max 0x1fffffff

using namespace std;

char name[105][105];
int a[1005];
int b[1005];
int c[1005];
char ch;
char s[1005];

int i,u,k,j,m,n,x,z,t;
int a1,a2;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	cin>>z;
	t=0;
	while (z--)
	{
		scanf("%d",&n);
		scanf("%c",&ch);

		t++;
		printf("Case #%d: ",t);
		for (i=0;i<n;i++)
		{
			u=-1;
			while (scanf("%c",&ch)==1&&ch!=10)
			{
				u++;
				s[u]=ch;
			}
			u++;
			s[u]=0;
			strcpy(name[i],s);
		}

		i=i;
		scanf("%d",&m);
		scanf("%c",&ch);
		for (i=0;i<m;i++)
		{
			u=-1;
			while (scanf("%c",&ch)==1&&ch!=10)
			{
				u++;
				s[u]=ch;
			}
			u++;
			s[u]=0;
			for (j=0;j<n;j++) if (strcmp(name[j],s)==0)
			{
				b[i]=j;
				break;
			}
		}

		i=i;
		for (i=0;i<n;i++) c[i]=0;
		for (x=0;x<m;x++)
		{
			for (i=0;i<n;i++) a[i]=c[i];
			for (i=0;i<n;i++) 
			if (i==b[x])
			{
				c[i]=max;
			}
			else
			{
				k=max;
				for (u=0;u<n;u++)
				{
					if (i==u)
					{
						j=a[u];
					}
					else j=a[u]+1;
					if (j<k) k=j;
				}
				c[i]=k;
			}
		}

		k=max;
		for (i=0;i<n;i++) if (c[i]<k) k=c[i];
		cout<<k<<endl;
	}
	return 0;
}




