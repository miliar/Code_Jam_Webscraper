#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;
int t,a,b,ggg;
bool vis[2000004];
string nts(int n)
{
	string s="";
	while (n)
	{
		s=(char)(n%10+'0')+s;
		n/=10;
	}
	return s;
}
int stn(string s)
{
	int ret=0;
	for (int i=0;i<s.size();i++)
		ret=ret*10+(s[i]-'0');
	return ret;
}
int main()
{
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d%d",&a,&b);
		long long ans=0;
		memset(vis,0,sizeof(vis));
		for (int i=a;i<=b;i++)
		if (!vis[i])
		{
			vis[i]=true;
			long long gg=1;
			string s=nts(i);
			int ll=s.size();
			for (int i=1;i<ll;i++)
			{
				char t=s[0];
				s.replace(0,1,"");
				s=s+t;
				int kk=stn(s);
				if (a<=kk&&kk<=b)
				if (!vis[kk])
				{
					vis[kk]=true;
					gg++;
				}
			}
			ans+=(gg-1)*gg/2;
		}
		printf("Case #%d: %lld\n",++ggg,ans);
	}
}
