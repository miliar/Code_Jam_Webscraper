#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("out.txt");

vector<map<string, int> > paths;

int addtopath(char *str) {
	char *p;
	int id = 0, rtn = 0, end = 0;
	++str;
	while (end != 1) {
		for (p = str; *p != '/' && *p != '\0'; ++p);
		if (*p == '\0') end = 1;
		*p = '\0';
		string temp(str);
		if (paths[id].find(temp) == paths[id].end()) {
			paths[id][temp] = paths.size();
			id = paths.size();
			paths.push_back(map<string, int>());
			++rtn;
		} else id = paths[id][temp];
		str = p + 1;
	}
	return rtn;
}

int main() {
	int t, n, m, ans;
	char temp[256];
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		fout << "Case #" << i << ": ";
		ans = 0;
		paths.clear();
		paths.push_back(map<string, int>());
		fin >> n >> m;
		for (int j = 0; j < n; ++j) {
			fin >> temp;
			addtopath(temp);
		}
		for (int j = 0; j < m; ++j) {
			fin >> temp;
			ans += addtopath(temp);
		}
		fout << ans << endl;
	}
	return 0;
}
