#include <cstdio>
#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
#include <cstring>
using namespace std;
int dp[505][21];

int main()
{
       int i,j ,k;
       int casos;
       cin >> casos;
       string s;
       getline(cin, s);
       for(int h = 0 ; h < casos; h ++ )
       {
	      getline(cin, s);
	      for( i = 0 ; i <= s.size(); i++)memset(dp[i], 0, sizeof(dp[i]));
	      for( i = 0 ; i <= (int)s.size(); i++) dp[i][0] = 1;
	      string wel = "welcome to code jam";
	      for( i = 0 ; i < s.size(); i ++ )for( j = 0 ; j < 19; j ++ )
	      {
		     if( wel[j] != s[i] ) continue;
		     for( k = i+1; k <= s.size(); k ++ ) dp[k][j+1] = (dp[k][j+1]+dp[i][j])%10000;
	      }
	      cout << "Case #"<<h+1 <<": " ;
	      int res = dp[(int)s.size()][19];
	      if( res < 1000 ) cout <<"0";
	      if( res < 100 ) cout << "0";
	      if( res < 10 ) cout << "0";
	      cout << res << endl;
       }
       return 0;
}

       