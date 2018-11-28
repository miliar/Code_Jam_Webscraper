#include<stdio.h>
#include<string.h>
int que[100],qt=0;
int k;
int was[100];
int len=100000;
char ch2[10000];
char ch1[10000];
int change()
{
	int n=strlen(ch1);
	int i=0;
	while(i<n)
	{
		int t=que[i%k]-1;
		int t2=i/k;
		t2*=k;
		ch2[i]=ch1[t2+t];
		i++;
	}
	int m=n;
	for(i=1;i<n;i++)
	{
		if(ch2[i-1]==ch2[i])
			m--;
	}
	return m;
}

void dfs(int x)
{
	if(x==0)
	{
		int mm=change();
		if(mm<len)
			len=mm;
	}
	for(int i=1;i<=k;i++)
	{
		if(was[i]==0)
		{
			was[i]=1;
			que[qt]=i;
			qt++;
			dfs(x-1);
			qt--;
			was[i]=0;
		}
	}
}


int main()
{
	int n,t=1;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("hi.txt","w",stdout);
	scanf("%d",&n);
	while(t<=n)
	{
		scanf("%d",&k);
		char ch=getchar();
		gets(ch1);
		len=1000000;
		qt=0;
		memset(was,0,sizeof(was));
		dfs(k);
		printf("Case #%d: %d\n",t,len);
		t++;
	}
}