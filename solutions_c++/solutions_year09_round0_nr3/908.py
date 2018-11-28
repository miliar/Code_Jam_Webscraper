#include <iostream>
#include <fstream>
#include <string>
#include <string.h>

using namespace std;

int dp [510][20];
int main()
{
	int n=0;
	int res=0;
	string str="welcome to code jam";
	freopen ("a.in" , "r" , stdin);
	freopen ("b.out", "w", stdout);
	scanf("%d",&n);
	string now;
	getline(cin,now);
	for(int cas=1;cas<=n;cas++)
	{
		res=0;
		memset (dp,0,sizeof (dp));
	getline(cin,now);
	for (int i=0;i<str.size();i++)
	{
		int lst_sum=0;
		if (i==0)
			lst_sum=1;

		for(int j=0;j<now.size();j++)
		{
			if (str[i]==now[j])
			{
				dp[j][i]=lst_sum;
				if (i==str.size()-1)
				{
					res+=lst_sum;
					res%=10000;
				}

			}
			if (i!=0)
				lst_sum+=dp[j][i-1];
			lst_sum%=10000;
		}
	}
		string st;
		if (res<10)  st="000";
		else
		if (res<100)  st="00";
		else
		if (res<1000)  st="0";
		cout<<"Case #"<<cas<<": "<<st<<res<<endl;
	}
	return 0;
}
