#include <string.h>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)

int main() 
{
		int t;
		cin >> t;
		getchar();
		int p = 1;
		while (p <= t) {
			string s;
			getline(cin, s);
			string src = "welcome to code jam";
			int dp[20];memset(dp,0,sizeof(dp));int sum=0;
				
				fir(k,0,s.size())
				firre(j,src.size()-1,0)
				{
					if (s[k]==src[j]){
							if (j-1>=0) {
								dp[j] += dp[j-1];
								dp[j] = dp[j]%10000;
							}
							else  
								dp[j]+=1;
							if (j==src.size()-1)
							{
								sum=dp[j];
							}
					}
				}
			sum %= 10000;
			cout <<"Case #" << p++ << ": ";
			printf("%4.4d\n", sum);
		}
    return 0;
}

