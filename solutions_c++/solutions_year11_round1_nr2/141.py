#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAXN = 10005, MAXM = 105;

int T, N, M;
string dict[MAXN];
int mem[MAXN][30];

int possible[MAXN], P;
int ct[30];

inline void add(string s, int val) {
	for(int i = 0 ; i < (int)s.size() ; i++) {
		ct[s[i] - 'a'] += val;
	}
}

inline int guess(int m, string let) {
	P = 0;
	memset(ct, 0, sizeof(ct));
	for(int i = 0 ; i < N ; i++) {
		if ((int)dict[i].length() == (int)dict[m].length()) {
			possible[P++] = i;
			for(int j = 0 ; j < (int)dict[i].length() ; j++) {
				ct[dict[i][j] - 'a']++;
			}
		}
	}
	int ret = 0;
	for(int i = 0 ; i < 26 ; i++) {
		if (ct[let[i] - 'a'] == 0) {
			continue;
		}
		
		if (mem[m][let[i] - 'a'] == 0) {
			ret--;
		}
		
		for(int j = 0 ; j < P ;) {
			if (mem[possible[j]][let[i] - 'a'] == mem[m][let[i] - 'a']) {
				j++;
			}	else {
				add(dict[possible[j]], -1);
				possible[j] = possible[P - 1];
				P--;
			}
		}
	}
	return ret;
}

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N >> M;
		for(int i = 0 ; i < N ; i++) {
			cin >> dict[i];
			for(int j = 0 ; j < 26 ; j++) {
				mem[i][j] = 0;
				for(int k = 0 ; k < (int)dict[i].length() ; k++) {
					mem[i][j] = (mem[i][j] << 1) + ((int)(dict[i][k] - 'a') == j ? 1 : 0);
				}
			}
		}
		
		string str;
		cout << "Case #" << t << ":";
		for(int i = 0 ; i < M ; i++) {
			cin >> str;
			int score = 1;
			string ans = "";
			for(int j = 0 ; j < N ; j++) {
				int g = guess(j, str);
				if (g < score) {
					score = g;
					ans = dict[j];
				}
			}
			cout << " " << ans;
		}
		cout << endl;
	}
	return 0;
}
