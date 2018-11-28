#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<sstream>
#include<algorithm>

using namespace std;

int main()
{
	int test;
	cin>>test;
	string text;
	getline(cin,text);
	int cnt=1;
	while(test--)
	{
		getline(cin,text);
		string patt="welcome to code jam";
		
		int dp[501][20];
		int i=0,j=0;
		for(j=0;j<501;j++)for(i=0;i<20;i++) dp[j][i]=0;
		
		if(text[0]==patt[0])
				dp[0][0]=1;
		for(i=1;i<text.size();i++)
		{
			if(text[i]==patt[0])
				dp[i][0]=(dp[i-1][0]+1)%10000;
				else
				dp[i][0]=dp[i-1][0];
			
			for(j=1;j<patt.size();j++)
				if(text[i]==patt[j])
				dp[i][j]=(dp[i-1][j]+dp[i-1][j-1])%10000;
				else
				dp[i][j]=dp[i-1][j];
				
		}
		int ans=dp[text.size()-1][patt.size()-1];
		stringstream ss;
		ss<<ans;
		string an;
		ss>>an;
		while(an.size()<4){an.insert(0,"0");}
		cout<<"Case #"<<cnt<<": "<<an<<endl;
		cnt++;
	}
}
