#include<iostream>
#include<map>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
int main()
{
	long long cs,cnt,i,j,kk,num[100],ans,mi;
	string str;
	map <char ,int > mp;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>cs;
	for (kk=1;kk<=cs;kk++)
	{
		cin>>str;
		mp.clear();
		cnt=0;
		for (i=0;i<str.size();i++)
		{
			if (mp.find(str[i])==mp.end())
			{
				mp[str[i]]=1;
				cnt++;
			}
		}
		if (cnt==1) cnt++;
		mp.clear();
		mp[str[0]]=1;
		num[0]=1;
		for (i=1,j=0;i<str.size();i++)
		{
			if (mp.find(str[i])==mp.end())
			{
				 if (j==0) 
				 {
						mp[str[i]]=j;
						num[i]=j;
						j=2;
				 }
				 else
				 {
						mp[str[i]]=j;
						num[i]=j;
						j++;
				 }
			}
			else 
			{
				num[i]=mp[str[i]];
			}
		}
		ans=0;
		mi=1;
		for (i=str.size()-1;i>=0;i--)
		{
			ans+=num[i]*mi;
			mi*=cnt;
		}	
		cout<<"Case #"<<kk<<": "<<ans<<endl;
	}
	return 0;
}
				 
