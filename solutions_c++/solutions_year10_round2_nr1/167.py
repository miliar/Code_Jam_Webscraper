#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define CODE A-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

struct dir;

typedef map<string, dir*> msd;
typedef vector<string> vs;

struct dir {
	msd sub;
	~dir() {
		for (msd::iterator it = sub.begin(); it != sub.end(); ++it)
			delete it->second;
	}
};

vs splitpath(const string &path) {
	vs dirs;
	int lastSlash = 0;
	int len = path.size();
	for (int i = 1; i < len; ++i) {
		if (i + 1 == len || path[i + 1] == '/') {
			dirs.push_back(path.substr(lastSlash + 1, i - lastSlash));
			lastSlash = i + 1;
		}
	}
	return dirs;
}

int mkdirs;
void mkdir(const string &path, dir *root) {
	vs dirs = splitpath(path);
	dir *curr = root;
	for (unsigned i = 0; i < dirs.size(); ++i) {
		if (curr->sub.count(dirs[i]) == 0) {
			curr->sub[dirs[i]] = new dir;
			mkdirs += 1;
		}
		curr = curr->sub[dirs[i]];
	}
}

int solve() {
	int n, m;
	dir root;
	char line[125];
	scanf("%d %d\n", &n, &m);
	for (int i = 0; i < n; ++i) {
		scanf(" %s\n", line);
		mkdir(line, &root);
	}
	mkdirs = 0;
	for (int i = 0; i < m; ++i) {
		scanf(" %s\n", line);
		mkdir(line, &root);
	}
	return mkdirs;
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
