/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
#include <stack>
#include <deque>
#include <queue>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<double> point;
typedef long double ldb;

bool mark[3000][3000];
int dp[2000000 + 10];

int main(){

	int t; cin >> t;

	for (int o=1; o<=t; o++){
		int a,b; cin >> a >> b;
		int ans = 0;
		for (int i=a; i<=b; i++){
			int tmp = i;
			vector <int> dig;
			while (tmp){
				dig.push_back(tmp%10);
				tmp/=10; 
			}
			reverse(dig.begin(),dig.end());
			int PW = 1;
			for (int j=1; j<(int)dig.size(); j++)
				PW*=10;
			int now = i;
			set <int> SET;
			for (int j=1; j<(int)dig.size(); j++){
				now-= dig[j-1] * PW;
				now*=10; 
				now+= dig[j-1];
				if (now<=b && i<now && dig[j]!=0 && SET.find(now)==SET.end()){
					SET.insert(now);
					ans++;
				}
			}
		}
		cout << "Case #" << o << ": " << ans << endl;
	}

	return 0;
}
