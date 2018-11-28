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

string next(string s) {
	if (s.size() == 1) return s + "0";
	for (int i = s.size() - 2; i >= 0; --i) {
		if (s[i] < s[i + 1]) {
			string p = s.substr(i, s.size() - i);
			char min_m = '9';
			for (int j = 1; j < p.size(); ++j) 
				if (p[j] > p[0])
					min_m = min(min_m, p[j]);
			string res = s.substr(0, i);
			res += min_m;
			p.erase(p.begin() + p.find(min_m));
			sort(all(p));
			res += p;
			return res;
		}
	}
	char min_m = '9' + 1;
	for (int j = 1; j < s.size(); ++j) 
		 if (s[j] > '0') min_m = min(min_m, s[j]);
	if (min_m > '9') return s + "0";
	string res = "";
	res += min_m;
	res += "0";
	s.erase(s.begin() + s.find(min_m));
	sort(all(s));
	res += s;
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int id = 0; id < T; ++id) {
		cout << "Case #" << id + 1 << ": ";
		string s;
		cin >> s;
		cout << next(s) << "\n";
	}
	return 0;
}