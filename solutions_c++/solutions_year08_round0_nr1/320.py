#include <iostream>
#include <map>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int dp[1001][200];

int main(void) {
	int N;
	cin >> N;
	fu(ts,1,N+1) {
		map<string,int> engines;
		cout << "Case #" << ts << ": ";
		int S;
		cin >> S;
		string s;
		getline(cin,s);
		fu(i,0,S) {
			getline(cin,s);
			engines[s]=i;
		}
		memset(dp,100,sizeof(dp));
		int Q;
		cin >> Q;
		getline(cin,s);
		fu(i,0,S) dp[0][i]=0;
		fu(i,0,Q) {
			getline(cin,s);
			int w=-1;
			if(engines.count(s)) w=engines[s];
			fu(j,0,S) if(j!=w) fu(k,0,S) dp[i+1][j]<?=dp[i][k]+(j!=k);
		}
		int ret=100000;
		fu(i,0,S) ret<?=dp[Q][i];
		cout << ret << endl;
	}
}
