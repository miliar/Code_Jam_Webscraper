#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
using namespace std;
typedef long long ll;
string ans;
string dic[105],ls;
bool in(string s,char c)
{
	for(int i=0;i<(int)s.size();i++) if(s[i]==c) return true;
	return false;
}
bool maybe[105];
bool ck(string a,string x,char c)
{
	for(int i=0;i<(int)x.size();i++)
	{
		if(x[i]!=' '&&x[i]!=a[i]) return true;
		else if(x[i]==' '&&a[i]==c) return true;
	}
	return false;
}
int main()
{
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	int _,cas=0,n,m;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++) cin>>dic[i];

		printf("Case #%d:",++cas);

		for(int k=0;k<m;k++)
		{
			int mx=-1;
			cin>>ls;

			for(int i=0;i<n;i++)//Ã¶¾Ù
			{
				int tmp=0;//·ÖÊý
				string x;

				for(int j=0;j<(int)dic[i].size();j++) x+=' ';
				int cnt=0;

				for(int j=0;j<n;j++)
				{
					if(dic[j].size()==dic[i].size())
					{
						cnt++;
						maybe[j]=true;
					}
					else maybe[j]=false;
				}

				for(int j=0;j<26&&cnt>1;j++)
				{
					bool have=false;
					for(int l=0;l<n;l++)
					{
						if(!maybe[l]) continue;
						if(in(dic[l],ls[j]))
						{
							have=true;
							break;
						}
					}
					if(!have) continue;

					if(in(dic[i],ls[j]))
					{
						for(int l=0;l<(int)dic[i].size();l++)
							if(dic[i][l]==ls[j]) x[l]=ls[j];
						for(int l=0;l<n;l++)
						{
							if(!maybe[l]) continue;
							if(ck(dic[l],x,ls[j]))
							{
								maybe[l]=false;
								cnt--;
							}
						}
					}

					else
					{
						tmp++;
						for(int l=0;l<n;l++)
						{
							if(!maybe[l]) continue;
							if(in(dic[l],ls[j]))
							{
								maybe[l]=false;
								cnt--;
							}
						}
					}
				}
				if(tmp>mx)
				{
					mx=tmp;
					ans=dic[i];
				}
			}
			cout<<" "<<ans;
		}
		puts("");
	}
    return 0;
}
