#include <iostream>
using namespace std;

int n;

char s[1002];
char s2[1002];
bool f[6];
int a[6];
int minn;

void solve(int x)
{
	int i,j;
	if(x==n)
	{
		int t=0,l=strlen(s);
		for(i=0;i<l;i+=n)
			for(j=0;j<n;j++)
				s2[i+j]=s[i+a[j]];
		s2[i]='\0';
		for(i=0;i<l;i++)
		{
			if(s2[i]!=s2[i+1])
				t++;
		}
		if(t<minn)
			minn=t;
		return;
	}
	for(i=0;i<n;i++)
	{
		if(!f[i])
		{
			f[i]=true;
			a[x]=i;
			solve(x+1);
			f[i]=false;
		}
	}
}

int main()
{	
	freopen("cin.txt","r",stdin);
	freopen("cout.txt","w",stdout);
	int nn,i;
	scanf("%d",&nn);
	for(i=1;i<=nn;i++)
	{
		minn=99999999;
		printf("Case #%d: ",i);
		scanf("%d",&n);
		scanf("%s",s);
		memset(f,0,sizeof(f));
		solve(0);
		printf("%d\n",minn);
	}
	return 0;
}