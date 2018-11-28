#include<algorithm>
#include<iostream>
//                                                                                         Last Change:  2011-05-21 11:27:02
#include<string>
using namespace std;
int n,m;
string s[10001],t;
char cai[11];
bool can[10001],app[26];
bool find(string x,char y)
{
	for(int i=0;i<x.size();++i)
		if(x[i]==y)
			return true;
	return false;
}
int calc(string x)
{
	for(int i=0;i<x.size();++i)cai[i]=' ';
	for(int i=1;i<=n;++i)
	{
		can[i]=(s[i].size()==x.size());
	}
	for(int i=0;i<26;++i)app[i]=false;
	int ret=0;
	for(int i=0;i<26;++i)
	{
		int cnt=0;
		for(int k=0;k<x.size();++k)
			cnt+=cai[k]==' ';
		if(!cnt)break;
		char ch=t[i];
		bool need=false;
		cnt=0;
		for(int j=1;j<=n;++j)
			if(can[j])
			{
				for(int k=0;k<x.size();++k)
				{
					if(cai[k]!=' '&&cai[k]!=s[j][k])
					{
						can[j]=false;
						break;
					}
					if(cai[k]==' '&&app[s[j][k]-'a'])
					{
						can[j]=false;
						break;
					}
				}
				if(can[j])
				{
					++cnt;
					if(!need&&find(s[j],ch))
						need=true;
				}
			}
		if(cnt==1)break;
		if(need)
		{
			bool found=false;
			app[ch-'a']=true;
			for(int j=0;j<x.size();++j)
				if(x[j]==ch)
				{
					found=true;
					cai[j]=ch;
				}
			if(!found)++ret;
		}
	}
	return ret;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int _;cin>>_;
	for(int cas=1;cas<=_;++cas)
	{
		cout<<"Case #"<<cas<<':';
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;++i)
			cin>>s[i];
		for(int j=1;j<=m;++j)
		{
			cin>>t;
			string best="";
			int bestv=-1;
			for(int i=1;i<=n;++i)
			{
				int tmp=calc(s[i]);
				if(tmp>bestv)
					bestv=tmp,best=s[i];
			}
			cout<<' '<<best;
		}
		cout<<endl;
	}
	return 0;
}
