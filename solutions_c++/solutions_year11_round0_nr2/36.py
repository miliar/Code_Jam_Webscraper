#include <iostream>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		int combgrid[26][26];
		bool oppgrid[26][26];
		for (int i = 0; i < 26; i++) for (int j = 0; j < 26; j++) {
			combgrid[i][j] = -1;
			oppgrid[i][j] = 0;
		}
		
		int C, D, N;
		
		cin >> C;
		for (int i = 0; i < C; i++) {
			string comb;
			cin >> comb;
			int x = comb[0]-'A', y = comb[1]-'A', z = comb[2]-'A';
			combgrid[x][y] = combgrid[y][x] = z;
		}
		
		cin >> D;
		for (int i = 0; i < D; i++) {
			string opp;
			cin >> opp;
			int x = opp[0]-'A', y = opp[1]-'A';
			oppgrid[x][y] = oppgrid[y][x] = 1;
		}
		
		cin >> N;
		string input;
		cin >> input;
		
		string res = "";
		res += input[0];
		int m = 1;
		
		for (int i = 1; i < N; i++) {
			if (m == 0) {
				res += input[i];
				m = 1;
				continue;
			}
			int cur = input[i]-'A';
			int prev = res[m-1]-'A';
			//adding input[i] to list
			//first compare cur a prev for combination;
			if (combgrid[cur][prev] != -1)
				res[m-1] = combgrid[cur][prev] + 'A';
			else {
				//look for pairs that cancel
				bool exist[26];
				bool reset = 0;
				for (int j = 0; j < 26; j++) exist[j] = 0;
				for (int j = 0; j < m; j++) exist[res[j]-'A'] = 1;
				for (int j = 0; j < 26; j++)
					if (exist[j] && oppgrid[j][cur]) {
						//reset res
						res = "";
						m = 0;
						reset = 1;
						break;
					}
				if (!reset) {
					res += cur + 'A';
					m++;
				}
			}
			//cout << res << endl;
		}
		
		//cout << res << endl;
		
		
		cout << "Case #" << icase << ": ";
		cout << "[";
		if (m > 0) cout << res[0];
		for (int i = 1; i < m; i++) cout << ", " << res[i];
		cout << "]" << endl;
	}
	return 0;
}
