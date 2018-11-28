//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_S = 1000 * 10 + 10;
const int MAX_N = 100 + 10;

int n;
int brd[MAX_N];

long long l;
int dp[MAX_S];

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		cin>>l>>n;
		FOR(i, n)
			cin>>brd[i];
		sort(brd, brd + n);
		
		long long ans = -1;
		
		FOR(i, MAX_S){
			dp[i] = i ? MAX_S : 0;
			for(int j = 0; j < n && brd[j] <= i; j++)
				if(dp[i - brd[j]] + 1 < dp[i])
					dp[i] = dp[i - brd[j]] + 1;
			
			if(dp[i] == MAX_S)
				continue;
			
			long long curans = dp[i];
			long long val = l - i;
			for(int j = n - 1; j >= 0; j--){
				curans += (val / brd[j]);
				val %= brd[j];
			}
			if(!val && (ans == -1 || curans < ans))
				ans = curans;
		}
		if(ans != -1)
			cout<<"Case #"<<test<<": "<<ans<<"\n";
		else	cout<<"Case #"<<test<<": IMPOSSIBLE\n";
	}
	return 0;
}
