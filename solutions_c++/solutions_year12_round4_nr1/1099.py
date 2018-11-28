#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <utility>
#include <queue>
#include <iostream>
#include <iomanip>
#include <ctype.h>
#include <sstream>
#include <map>
#include <stdio.h>
#include <ctype.h>
#include <iomanip>

#define LL long long
#define fr(i,n) for(i=0;i<n;i++)
#define INF = 2000000000;
#define FOR(n) for(int i = 0;i < n;i++)
#define CLEAR(x) memset(x,0,sizeof(x))

using namespace std;

pair<int,int> p[10002];
int dp[10002];
int len;

string solve(){
	memset(dp,-1,sizeof(dp));
	int n,x;
	cin >> n;
	FOR(n)
		cin >> p[i].first >> p[i].second;
	
	cin >> len;
	dp[0]=p[0].first;
	

	FOR(n-1){
		x=i+1;
		if (dp[i]!=-1){
			
			while(true){
				if (x >= n)
					break;
				//cout << x <<' ' << i << endl;
				//c/out << p[x].first<<' ' <<p[i].first<< endl;
				//cout << "DIFF :" <<p[x].first-p[i].first << ' ' << endl;
				if (p[x].first-p[i].first <= dp[i]){
					dp[x]=max(dp[x],min(p[x].second,p[x].first-p[i].first));
					//cout << "X" << ' ' <<  x << ' ' << dp[x]<< endl;
				}else
					break;
				x++;
			}
		}
	}

	
	
	FOR(n){
		if (len-p[i].first <= dp[i])
			return "YES";
	}
	
	return "NO";
}

int main(){
    //freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t;tt++){
		cout << "Case #" << tt << ": " << solve() << endl;    
    }
    return 0;
}



