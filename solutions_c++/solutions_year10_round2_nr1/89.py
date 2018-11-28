#include <cstdio>
#include <map>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int tests, n, m;
vector<map<string, int> > inodes;
vector<int> exists;
char buf[128];

void add(char *path, int value) {
	char *s = strtok(path, "/");
	int p = 0;
	
	while (s) {
		if (inodes[p].count(s) == 0) {
			inodes[p][s] = exists.size();
			inodes.push_back(map<string, int>());
			exists.push_back(value);
		}
		p = inodes[p][s];
		s = strtok(NULL, "/");
	}
}

void new_case() {
	inodes.clear();
	exists.clear();
	inodes.push_back(map<string, int>());
	exists.push_back(1);
}

int main() {
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		new_case();
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", &buf);
			add(buf, 1);
		}
		for (int i = 0; i < m; i++) {
			scanf("%s", &buf);
			add(buf, 0);
		}
		int total = 0;
		for (int i = 0; i < (int)exists.size(); i++)
			if (exists[i] == 0)
				total++;
		printf("Case #%d: %d\n", tc, total);
	}
	return 0;
}