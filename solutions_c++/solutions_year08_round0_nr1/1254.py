#include<iostream>
#include<map>
#include<string>

using namespace std;

int S, Q;
map<string, int> dic;
int dp[1010][110];
int req[1010];

void solve(int id) {
	if (Q == 0) {
		cout << "Case #" << id << ": " << 0 << endl;
		return;
	}

	for (int s=0; s<S; ++s) {
		if (req[Q-1] != s) 
			dp[Q-1][s] = 0;
		else
			dp[Q-1][s] = 1;
	}

	for (int q=Q-2; q>=0; --q) {
		for (int s=0; s<S; ++s) {
			int opt = -1;
			for (int choose=0; choose<S; ++choose) if (choose != s) {
				int tmp = dp[q+1][choose] + 1;
				if (opt == -1 || opt > tmp)
					opt = tmp;
			}
			dp[q][s] = opt;

			if (s != req[q]) {
				dp[q][s] = min(dp[q][s], dp[q+1][s]);
			}
		}
	}

	int opt = -1;
	for (int s=0; s<S; ++s) {
		if (opt == -1 || dp[0][s] < opt)
			opt = dp[0][s];
	}
	cout << "Case #" << id << ": " << opt << endl;
}



int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output", "w", stdout);
	int T;
	cin >> T;
	for (int id=1; id<=T; ++id) {
		dic.clear();
		cin >> S;
		cin.ignore(100, '\n');
		string line;
		for (int i=0; i<S; ++i) {
			getline(cin, line);
			dic.insert(make_pair(line, i));
		}
		cin >> Q;	
		cin.ignore(100, '\n');
		for (int i=0; i<Q; ++i) {
			getline(cin, line);
			req[i] = dic[line];
		}
		solve(id);
	}

	return 0;
}