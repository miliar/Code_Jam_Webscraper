#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Directory {
public:
	static int mkCnt;

	~Directory() {
		for (map<string, Directory *>::iterator it = subDirs.begin(); it != subDirs.end(); ++it) {
			delete it->second;
		}
	}

	Directory * getSubDir(const string & name) {
		map<string, Directory *>::const_iterator it = subDirs.find(name);
		if (it == subDirs.end()) {
			Directory * newDir = new Directory;
			subDirs.insert(make_pair(name, newDir));
			mkCnt++;
			return newDir;
		} else {
			return it->second;
		}
	}

	map<string, Directory *> subDirs;
};

int Directory::mkCnt;

void mkDirs(Directory * root, string path) {
	for (size_t i = 0; i < path.size(); i++) {
		if (path[i] == '/') {
			path[i] = ' ';
		}
	}
	istringstream sin(path);
	Directory * cur = root;
	string name;
	while (sin >> name) {
		cur = cur->getSubDir(name);
	}
}

int main() {
	int caseNum;
	cin >> caseNum;
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		int oNum, nNum;
		cin >> oNum >> nNum;
		Directory * root = new Directory;
		string path;
		getline(cin, path);
		Directory::mkCnt = 0;
		while (oNum-- > 0) {
			getline(cin, path);
			mkDirs(root, path);
		}
		Directory::mkCnt = 0;
		while (nNum-- > 0) {
			getline(cin, path);
			mkDirs(root, path);
		}
		printf("Case #%d: %d\n", caseIndex, Directory::mkCnt);
	}
	return 0;
}
