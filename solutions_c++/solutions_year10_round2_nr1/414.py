#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int func(vector<string>& a, vector<string>& b) {
	set<string> hoge;
	for (unsigned i = 0; i < a.size(); ++ i) {
		string s = a[i];
		unsigned p;
		while ((p = s.rfind('/')) != string::npos) {
			hoge.insert(s);
			s.erase(p);
		}
	}
	int cnt = 0;
	for (unsigned i = 0; i < b.size(); ++ i) {
		string s = b[i];
		unsigned p;
		while ((p = s.rfind('/')) != string::npos) {
			if (hoge.insert(s).second) ++ cnt;
			s.erase(p);
		}
	}
	return cnt;
}

int main() {
	string buf;
	getline(cin, buf);
	int T = atoi(buf.c_str());
	for (int i = 1; i <= T; ++ i) {
		int N, M;
		getline(cin, buf);
		istringstream in(buf);
		in >> N >> M;
		vector<string> a(N);
		vector<string> b(M);
		for (int j = 0; j < N; ++ j) {
			getline(cin, a[j]);
		}
		for (int j = 0; j < M; ++ j) {
			getline(cin, b[j]);
		}
		cout << "Case #" << i << ": " << func(a, b) << endl;
	}
}
