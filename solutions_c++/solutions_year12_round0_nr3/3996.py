#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <memory.h>

using namespace std;

const int MAXN = 3000000;

bool used[MAXN];

string next_circle(const string &s) {
	string res = s;
	for(int i = 0; i < res.length(); ++i)
		res[i] = s[(i+1)%res.length()];
	return res;
}

string itos(int i) {
	stringstream ss;
	ss << i;
	return ss.str();
}

int stoi(string s) {
	stringstream ss(s);
	int res;
	ss >> res;
	return res;
}

int n, a, b;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);
	for(int i = 0; i < n; ++i) {
		scanf("%d%d", &a, &b);
		//cout << "+++++++++++ (a, b) = (" << a<< ", " << b <<") +++++++++++" << endl;
		memset(used, 0, sizeof(used));
		long long res = 0;
		for(int j = a; j <= b; ++j) {
			if(used[j]) continue;
			long long cnt = 0;
			string s = itos(j);
			for(int k = 0; k < s.length(); ++k, s = next_circle(s)) {
			//	cout << s << endl;
				if(s[0] == '0') continue;
				int p = stoi(s);
				if(p >= a && p <= b) cnt += !used[p], used[p] = 1;				
			}
			res += cnt*(cnt-1)/2;
		//	cout << "CNT = " << cnt << endl;
		//	cout << "======" << endl;
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}