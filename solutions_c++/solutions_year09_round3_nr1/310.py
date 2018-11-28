#include<iostream>
#include<sstream>
#include<string>
#include<map>
using namespace std;

char s[80];
map<char,int> mp;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas=1;
	int t,i,j,k,len,b;
	__int64 ans;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas);
		cas++;
		scanf("%s",s);
		mp.clear();
		len=strlen(s);
		for(i=0;i<len;i++)
			mp[s[i]]=999;
		b=mp.size();
		if(b==1)
		{
			if(len==1)
				ans=1;
			else
			{
				ans=0;
				for(i=0;i<len;i++)
					ans=ans*2+1;
			}
		}
		else
		{
			int ct=2;
			mp[s[0]]=1;
			for(i=1;i<len;i++)
				if(s[i]!=s[i-1])
					break;
			mp[s[i]]=1000;
			ans=1;
			for(i=1;i<len;i++)
			{
				if(mp[s[i]]!=0)
				{
					if(mp[s[i]]==999)
					{
						ans=ans*b+ct;
						mp[s[i]]=ct;ct++;
					}
					else
					{
						if(mp[s[i]]==1000)
							ans=ans*b;
						else
							ans=ans*b+mp[s[i]];
					}
				}
			}
		}
		printf("%I64d\n",ans);
	}
	return 0;
}
