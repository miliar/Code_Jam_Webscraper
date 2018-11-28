#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <functional>
using namespace std;

char s[100];
map<char,int> mp;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		mp.clear();
		scanf("%s",s);
		int osn=2;
		mp[s[0]]=1;
		int i=1;
		while(s[i]==s[0])
			i++;
		if(s[i]!=0)
		{
			mp[s[i++]]=0;
			while(s[i]!=0)
			{
				if(mp.find(s[i])==mp.end())
					mp[s[i]]=osn++;
				i++;
			}
		}
		long long ans=0;
		for(i=0;s[i]!=0;i++)
			ans=ans*osn+mp[s[i]];
		printf("Case #%d: %lld\n",t,ans);
	}
	//
	return 0;
}