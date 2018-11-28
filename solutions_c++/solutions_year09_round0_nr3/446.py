#include<iostream>
#include<string>
#include<vector>

using namespace std;


int N;


int dp[20];

string p = "welcome to code jam";
int lp = 19;

string line;

int main()
{
   cin >> N;

   getline(cin, line);
   for (int cc = 1;cc<=N;cc++)
   {
	   getline(cin, line);
	   int  n = line.size();
		    for (int j = 0;j<=lp;j++) dp[j] = 0;

	dp[0]=1;
	   for (int i = 0;i<n;i++)
		   for ( int k = lp-1;k >=0 ;k--)
			    if (line[i] == p[k])
					dp[k+1] = (dp[k+1] + dp[k]) % 10000;

	    cout<<"Case #" <<  cc << ": ";
		if (dp[lp] < 1000) cout << 0;
		if (dp[lp] < 100) cout << 0;
		if (dp[lp] < 10) cout << 0;
	   cout << dp[lp] << endl;
   }
}
