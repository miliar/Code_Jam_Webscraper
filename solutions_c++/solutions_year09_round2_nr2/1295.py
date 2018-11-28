#include <iostream>

#define INF 99999999

using namespace std;

int n,ans,len;
bool hash[100];
char s[100],data[100];

void dfs(int x,int L)
{
	if (x>=L)
	{
		int x;
		if (s[0]==0)
			return;
		sscanf(s,"%d",&x);
		if (x>n && x<ans)
			ans=x;
		return;
	}
	for (int i=0;i<L;i++)
		if (!hash[i])
		{
			hash[i]=true;
			s[x]=data[i];
			dfs(x+1,L);
			hash[i]=false;
			s[x]=0;
		}
}

void run()
{
	dfs(0,len);
	data[len]='0';
	dfs(0,len+1);
	/*if (ans>=INF)
	{
		char zan[100]={0};
		zan[0]=data[len-1];
		for (int i=1;i<len;i++)
			zan[i+1]=data[len-i];
		sscanf(zan,"%d",&ans);
	}*/
}

void ini()
{
	int i,T;
	cin>>T;
	for (i=1;i<=T;i++)
	{
		memset(data,0,sizeof(data));
		cin>>n;
		sprintf(data,"%d",n);
		memset(hash,0,sizeof(hash));
		len=strlen(data);
		ans=INF;
		run();
		printf("Case #%d: %d\n",i,ans);
	}
}

int main()
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	ini();
	return 0;
}
