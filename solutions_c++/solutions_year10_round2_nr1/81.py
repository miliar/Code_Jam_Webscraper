#include <set>
#include <string>
#include <iostream>
using namespace std;

int addDir(const std::string &dir, set<string> &dirs) {
	int res = 0;
	for (unsigned int i=1; i<=dir.size(); i++) {
		if (i==dir.size() || dir[i]=='/') {
			string parent = dir.substr(0, i);
			if (dirs.find(parent)==dirs.end()) {
				dirs.insert(parent);
				res++;
			}
		}
	}
	return res;
}

void runTest() {
	int N, M;
	cin >> N >> M;
	set<string> dirs;
	string dir;
	for (int i=0; i<N; i++) {
		cin >> dir;
		addDir(dir, dirs);
	}
	int res = 0;
	for (int i=0; i<M; i++) {
		cin >> dir;
		res += addDir(dir, dirs);
	}
	cout << res << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		cout << "Case #" << (i+1) << ": ";
		runTest();
	}
	return 0;
}

