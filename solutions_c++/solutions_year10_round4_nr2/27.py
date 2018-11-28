//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back

using namespace std;

const int MAX_P = 10 + 3;
const int MAX_G = 2 << 10 + 10;

int p;
long long dp[MAX_G][MAX_P];
long long cost[MAX_G];
int miss[MAX_G];

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		scanf("%d", &p);
		int n = 1 << p;
		FOR(i, n)
			scanf("%d", &miss[i]);
		reverse(miss, miss + n);
		
		FOR(i, n - 1)
			cin>>cost[i];
		reverse(cost, cost + (n - 1));
		
		memset(dp, -1, sizeof dp);
		FOR(i, n)
			FOR(j, miss[i] + 1)
				dp[i + n - 1][j] = 0;
		
		for(int i = n - 2; i >= 0; i--)
			for(int j = 0; j <= p; j++){
				if(dp[2 * i + 1][j + 1] != -1 && dp[2 * i + 2][j + 1] != -1)
					dp[i][j] = dp[2 * i + 1][j + 1] + dp[2 * i + 2][j + 1];
				if(dp[2 * i + 1][j] != -1 && dp[2 * i + 2][j] != -1){
					int newval = dp[2 * i + 1][j] + dp[2 * i + 2][j];
					newval += cost[i];
					if(dp[i][j] == -1 || dp[i][j] > newval)
						dp[i][j] = newval;
				}
			}
		cout<<"Case #"<< test <<": "<< dp[0][0] <<"\n";
	}
	return 0;
}
