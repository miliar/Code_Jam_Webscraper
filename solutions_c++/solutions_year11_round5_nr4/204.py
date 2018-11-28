#include<iostream>
#include<string>
#include<cmath>
using namespace std;
char c[100];
string res;
void solve(int t,string &s)
{
	if(t==s.length())
	{
		long long int x = 0;
		for(int i=0;i<t;i++)
		{
			x=x<<1|c[i];
		}
		long double z = x*1.0L;
		long double p = sqrt(z);
		long long y = (long long)p;
		if(y*y==x||(y-1)*(y-1)==x||(y+1)*(y+1)==x)	
		{
			res=s;
			for(int i=0;i<t;i++)res[i]=c[i]+'0';
			return ;
		}
	}
	else
	{
		if(s[t]=='?')
		{
			c[t]=0;
			solve(t+1,s);
			c[t]=1;
			solve(t+1,s);
		}
		else
		{
			c[t]=s[t]-'0';
			solve(t+1,s);
		}
	}
}
int main()
{
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	int cas_num;
	scanf("%d",&cas_num);
	for(int case_num=1;case_num<=cas_num;case_num++)
	{
		printf("Case #%d: ",case_num);
		string s ;
		cin>>s;
		solve(0,s);
		cout<<res<<endl;
	}
}