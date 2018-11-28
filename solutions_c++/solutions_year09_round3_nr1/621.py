#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<algorithm>
#include<functional>
#include<utility>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdio>
#include<ctime>
#include<string>
using namespace std;

map<char ,int>my;
int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output1.txt", "wt", stdout);
	int t;
	cin>>t;
	int i,j,kth=1;
	while(t--)
	{ 
		string s;
		cin>>s;
		int i,j;
		int len=s.size();
		my.clear();
        for(i=0;i<len;i++)
		{
			my[s[i]]++;
		}

		int r=0;
		for(i=0;i<10;i++)
			if(my['0'+i]!=0)
               r++;
		for(i=0;i<26;i++)
			if(my['a'+i]!=0)
				r++;

		string re=s;
		int biao[100];
		memset(biao,0,sizeof(biao));
		int z=2;
		int use=0,uz=0;
		for(i=0;i<len;i++)
		{
			if(biao[i]==0)
			{
		    	char c=s[i];
				int bp=0;
			    for(j=i;j<len;j++)
                   if(s[j]==c)
				   {
					   if(i==0)
					     re[j]='1';
					   else if(use==0)
					   {
						   re[j]='0';
						   bp=1;
					   }
					   else
					   {
						   re[j]='0'+z;
						   uz=1;
					   }
					   biao[j]=1;
				   }
				   if(bp==1)
				   use=1;
				   if(uz==1)
					   z++;
			}
		}
	long long int ans=0;
	if(r==1)
		r=2;
	for(i=0;i<len;i++)
	{
         ans=ans*r+re[i]-'0';
	}
	  printf("Case #%d: %lld\n",kth++,ans);
	} 
	return 0;
}

