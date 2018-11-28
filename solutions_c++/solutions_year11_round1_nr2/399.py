#include<iostream>
#include<vector>
#include<string>
#include<cstring>
using namespace std;
int t,mt,n,m,i,f[200],ans,ansi;
vector<string>wo;
string ts;
int scan(char c)
{
	int n=wo.size();
	for(int i=0;i<n;i++)
	{
		if (f[i]) continue;
		int l=wo[i].size();
		for(int j=0;j<l;j++)if (wo[i][j]==c) return 1;
	}
	return 0;
}
int guess(char c,string s)
{
	int l=s.size();
	for(int i=0;i<l;i++)
	{
		for(int j=0;j<n;j++)
		{
			if (f[j]) continue;
			if ((wo[j][i]==c)&&(s[i]!=c)) f[j]=1;
			if ((wo[j][i]!=c)&&(s[i]==c)) f[j]=1;
		}
	}
	for(int i=0;i<l;i++)
	{
		if (s[i]==c) return 0;
	}
	return 1;
}
int main()
{
	freopen("B2.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&t);
	for(mt=1;mt<=t;mt++)
	{
		wo.clear();
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			cin>>ts;
			wo.push_back(ts);
		}
		printf("Case #%d:",mt);
		for(i=0;i<m;i++)
		{
			cin>>ts;
			ans=-1;
			for(int j=0;j<n;j++)
			{
				memset(f,0,sizeof(f));
				int pt=0;
				for(int k=0;k<n;k++)
				{
					if (wo[k].size()!=wo[j].size()) f[k]=1;
				}
				int l=ts.size();
				for(int k=0;k<l;k++)
				{
					if (scan(ts[k])) pt+=guess(ts[k],wo[j]);
				}
				if (pt>ans)
				{
					ans=pt;
					ansi=j;
				}
			}
			printf(" %s",wo[ansi].c_str(),ans);
		}
		puts("");
	}
}
