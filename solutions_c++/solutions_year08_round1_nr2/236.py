#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

typedef pair<int,int> PII;

int choices[2500][2500];
int unmalted[2500];
int cust[2500];
bool ans[2500];
bool sat[2500];
int tot;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int N, M;
		cin >> N >> M;
		memset(cust, -1, sizeof cust);
		memset(unmalted, -1, sizeof unmalted);
		for(int i = 0; i < M; i++) {
			int typ, tmp, m;
			cin >> typ;
			memset(choices[i], -1, sizeof choices[i]);
			for(int j = 0; j < typ; j++) {
				cin >> tmp >> m;
				if(choices[i][tmp-1] < 0)
					choices[i][tmp-1] = m;
				else
					choices[i][tmp-1] = 2;
				if(m == 1)
					unmalted[i] = tmp-1;
			}
			cust[i] = typ;
		}

		memset(ans, 0, sizeof ans);
		memset(sat, 0, sizeof sat);
		tot = 0;
		for(int i = 0; i < M; i++) {
			for(int j = 0; j < N; j++) {
				if(choices[i][j] == 2) {
					sat[i] = true;
					tot ++;
					cust[i] = 0;
				}
			}
		}

		while(tot < M) {
			int i = 0;
			for(i = 0; i < M; i++) {
				if(sat[i]) continue;
				if(cust[i] > 1) continue;
				if(unmalted[i] >= 0) break;
			}
			if(i == M) {
				cout << "Case #" << t+1 << ":";
				for(int ff = 0; ff < N; ff++)
					cout << " " << ans[ff];
				cout << endl;
				tot = M + 1;
				break;
			}
			int fl = unmalted[i];
			ans[fl] = true;
			sat[i] = true;
			cust[i] = 0;
			tot ++;
			for(int j = 0; j < M; j++) {
				if(sat[j]) continue;
				if(unmalted[j] == fl) {
					sat[j] = true;
					cust[j] = 0;
					tot ++;
				}
				if(choices[j][fl] >= 0) {
					choices[j][fl] = -1;
					cust[j] --;
					if(cust[j] == 0) {
						cout << "Case #" << t+1 << ": IMPOSSIBLE\n";
						tot = M + 1;
						break;
					}
				}
			}

		}
		if(tot == M) {
			cout << "Case #" << t+1 << ":";
			for(int ff = 0; ff < N; ff++)
				cout << " " << ans[ff];
			cout << endl;
		}
	}
	return 0;
}
