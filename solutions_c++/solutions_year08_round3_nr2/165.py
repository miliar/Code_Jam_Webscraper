#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
typedef vector<bool> VB;
struct point
{
    bool flag;
	__int64 value;
};
__int64 value(string str)
{
    __int64 ans=0;
	int i;
	__int64 t=0;
	bool flag=true;
	for(i=0;i<str.size();i++)
	{
	    if(str[i]=='+'||str[i]=='-')
		{
			if(flag)
			{
				ans+=t;
				t=0;
			}
			else
			{
				ans-= t;
				t=0;
			}
			if(str[i]=='+')
				flag=true;
			else
				flag=false;
		}
		else
			t=t*10+str[i]-'0';
	}
	if(flag)
	{
	  ans+=t;
	}
	else
	{
	  ans-=t;
	}
	return ans;
}
bool can(__int64 t)
{
	if(t%2==0||t%3==0||t%5==0||t%7==0)
	{
		return true;
	}
	return false;
}
int main()
{
 	freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
	int i,j,Case,num;
	string str,str1;
	int ans;
	vector<string> strings[40];
	cin>>Case;  	 
	num=1;
	while (Case--)
	{
	     cin>>str;
		 strings[0].clear();
		 str1="";
		 str1+=str[0];
		 strings[0].push_back(str1);
		 for(i=1;i<str.size();i++)
		 {
			strings[i].clear();
		    for(j=0;j<strings[i-1].size();j++)
			{
			   str1=strings[i-1][j];
			   strings[i].push_back(str1+str[i]);
			   strings[i].push_back(str1+'+'+str[i]);
			   strings[i].push_back(str1+'-'+str[i]);
			}
		 }
	    ans=0;
		for(i=0;i<strings[str.size()-1].size();i++)
		{
			__int64 t=value(strings[str.size()-1][i]);
			if(can(t))
			{
			  ans++;
			}
		}
		printf("Case #%d: %d\n",num++,ans);		
	}
	return 0; 
}