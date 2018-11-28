#include <iostream>
#include <cstring>

using namespace std;

char s[2000];
int i,u,k,j,m,n,x,z,t;
int a[1000];
int v[2000][10];
int visit[1000];

void pig(int a1)
{
	if (a1==k)
	{
		for (i=0;i<n;i++) s[i]=v[i/k][a[i%k]];
		u=1;
		for (i=1;i<n;i++)
			if (s[i]!=s[i-1]) u++;
		if (x==-1) x=u;
		else if (x>u) x=u;
	}

	int i;
	for (i=0;i<k;i++) if (visit[i])
	{
		a[a1]=i;
		visit[i]=0;
		pig(a1+1);
		visit[i]=1;
	}
}


int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>z;
	t=0;
	while (z--)
	{
		t++;
		scanf("%d",&k);
		scanf("%s",s);
		n=strlen(s);
		m=n/k;
		for (i=0;i<m;i++) for (u=0;u<k;u++)
		{
			v[i][u]=s[i*k+u]-97;
		}

		x=-1;
		for (i=0;i<k;i++) visit[i]=1;
		pig(0);
		printf("Case #%d: %d\n",t,x);
	}
	return 0;
}

