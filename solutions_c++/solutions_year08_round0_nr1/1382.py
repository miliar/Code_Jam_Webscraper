#include<iostream>
#include<vector>
#include<string>
#include<map>

using namespace std;

typedef vector<int> _vi;
typedef vector<vector<int> > _vvi;

#define INFTY 1000000000
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)

void do_it(int test){
	int S;
	cin >> S;
	char tmp[110];
	map<string, int> M;

	cin.ignore(10, '\n');

	REP(i,S){
		cin.getline(tmp, 110);
		string s(tmp);
		M[s] = i;
	}

	int Q;
	cin >> Q;
	cin.ignore(10, '\n');

	_vvi dp(Q+1, _vi(S, 0));
	FUP(i,1,Q){
		cin.getline(tmp, 110);
		string s(tmp);
		int act = M[s];

		REP(j,S){
			dp[i][j] = INFTY;
			if(j == act) continue;
			REP(k,S)
				if(k!=j)
					dp[i][j] = min(dp[i][j], dp[i-1][k] + 1);
				else
					dp[i][j] = min(dp[i][j], dp[i-1][k]);
		}
	}

	int res = INFTY;
	REP(i,S)
		res = min(res, dp[Q][i]);
	cout << "Case #" << test << ": " << res << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

