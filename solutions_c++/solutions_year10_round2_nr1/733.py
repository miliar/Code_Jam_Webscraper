#include <iostream>
#include <set>
using namespace std;

int T, N, M;

int main() {
	cin >> T;
	for (int kase = 0; kase < T; ++kase) {
		int ret = 0;
		cin >> N >> M;
		set<string> sta, stb;
		string str;
		for (int i = 0; i < N; ++i) {
			cin >> str;
			int idx;
			str += "/";
			string prefix = "";
			while ((idx = str.find("/")) != -1) {
				string seg = str.substr(0, idx);
				if (idx + 1 < str.length())
					str = str.substr(idx + 1);
				else
					str = "";
				if (seg.length() > 0) {
					sta.insert(prefix + seg);
					//cout << "exist " << prefix + seg << endl;
				}
				prefix += seg;
			}
		}
		for (int i = 0; i < M; ++i) {
			cin >> str;
			str += "/";
			int idx;
			string prefix = "";
			while ((idx = str.find("/")) != -1) {
				string seg = str.substr(0, idx);
				if (idx + 1 < str.length())
					str = str.substr(idx + 1);
				else
					str = "";
				if (seg.length() > 0) {
					stb.insert(prefix + seg);
					//cout << "add " << prefix + seg << endl;
				}
				prefix += seg;
			}
		}
		for (set<string>::iterator itr = stb.begin(); itr != stb.end(); ++itr) {
			if (sta.find(*itr) == sta.end())
				ret ++;
		}
		cout << "Case #" << kase + 1 << ": " << ret << endl;
	}
	return 0;
}

