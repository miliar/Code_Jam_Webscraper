#include<iostream>
#include<fstream>
using namespace std;

string want="welcome to code jam";
char chr[1001];
int dp[1001][19];

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int T;
	cin>>T;
	cin.getline(chr,800);
	for(int c=1;c<=T;c++)
	{
		cin.getline(chr,800);
		string t = chr;
		int n=t.length()-1;
		memset(dp,0,sizeof(dp));
		for(int i=0;i<=n;i++)
		{
			if(chr[i] == 'w')
				dp[i][0]++;
			for(int j=1;j<=18;j++)
				if(chr[i] == want[j])
					if(i)
						dp[i][j]=(dp[i][j]+dp[i-1][j-1])%1000;
			for(int j=0;j<=18;j++)
				dp[i][j]=(dp[i][j]+dp[i-1][j])%1000;
		}
		cout<<"Case #"<<c<<": ";
		int ans = dp[n][18];
		if(ans < 1000)
			cout<<0;
		if(ans < 100)
			cout<<0;
		if(ans < 10)
			cout<<0;
		cout<<ans;
		cout<<endl;
		
	}
	return 0;
}
