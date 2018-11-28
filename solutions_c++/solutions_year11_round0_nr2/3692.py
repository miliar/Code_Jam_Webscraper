#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<cstring>
#include<cstdio>
#include<map>
#include<cstdlib>
#include<fstream>
#include<queue>
using namespace std;
int main()
{
	#if 1
	freopen("1.in","r",stdin);
	freopen("2.out","w+",stdout);
	#endif
	int test,t,c,d,n;
	int i,j,k,len,flag;
	string f1,f2,s,ans;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		ans="";
		cin>>c;
		if(c==1) 
		{
			cin>>f1;
		}
		cin>>d;
		if(d==1) 
		{
			cin>>f2;
		}
		cin>>n;
		cin>>s;
		ans+=s[0];
		len=ans.length();
		for(i=1;i<n;i++)
		{
			len=ans.length();
			if (c==1 &&(!ans.empty())&& (ans[len-1]==f1[0]&&s[i]==f1[1])||(ans[len-1]==f1[1]&&s[i]==f1[0]))
			{
				ans=ans.substr(0,len-1)+f1[2];
				continue;
			}
			if (d==1)
			{
				flag=0;
				for(j=0;j<len;j++)
				{
					if ((ans[j]==f2[0]&&s[i]==f2[1])||(ans[j]==f2[1]&&s[i]==f2[0]))
					{
						ans="";
						flag=1;
						break;
					}
				}
				if (flag) continue;
			}
			ans+=s[i];
		}
		cout<<"Case #"<<t<<": [";
		if (!ans.empty())
		{
			for (i=0;i<(int)ans.length()-1;i++)
				cout<<ans[i]<<", ";
			cout<<ans[(int)ans.length()-1];
		}
		cout<<"]"<<endl;
	}
	return 0;
}