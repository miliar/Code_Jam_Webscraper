#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

string s = "welcome to code jam";
int m = 19;
int dp[510][25];
char _ch[10000];

int main(void){
	int i,j,test,T;
	
	cin >> T;
	cin.getline(_ch,sizeof(_ch));
	REP(test,T){
		cin.getline(_ch,sizeof(_ch));
		string t = _ch;
		int n = t.length();
		
		REP(i,n+1) REP(j,m+1) dp[i][j] = 0;
		dp[0][0] = 1;
		REP(i,n) REP(j,m+1){
			dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % 10000;
			if(j != m && t[i] == s[j]) dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % 10000;
		}
		
		string ans = itos(dp[n][m]);
		while(ans.length() < 4) ans = '0' + ans;
		gcj_print(ans);
	}
	
	return 0;
}
