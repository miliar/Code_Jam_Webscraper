#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps 0.00000001
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> words;
	for (int i = 0; i < D; ++i) {
		string s;
		cin >> s;
		words.push_back(s);
	}
	for (int id = 0; id < N; ++id) {
		cerr << id;
		cout << "Case #" << id + 1 << ": ";
		int res = 0;
		string pattern;
		cin >> pattern;
		int cur = 0;
		vector<string> stat_pattern;
		for (int i = 0; i < L; ++i) {
			string var = "";
			if (pattern[cur] == '(') {
				++cur;
				for (;pattern[cur] != ')'; ++cur) 
					var += pattern[cur];
				++cur;
			} else {
				var += pattern[cur];
				++cur;
			}
			stat_pattern.push_back(var);
		}
		for (int i = 0; i < D; ++i) {
			bool ok = true;
			for (int j = 0; j < words[i].size(); ++j) {
				if (count(all(stat_pattern[j]), words[i][j]) == 0) ok = false;
			}
			res += int(ok);
		}
		cout << res << "\n";
	}
	return 0;
}