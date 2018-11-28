#include <cstdio>
#include <map>
#include <string>
#include <vector>

using namespace std;

struct Tree {
	vector<string> segments;
	vector<Tree*> trees;
	bool find(const string& key) {
		for (int i = 0; i < segments.size(); i++) {
			if (segments[i] == key) return true;
		}
		return false;
	}
	void create(const string& key) {
		segments.push_back(key);
		trees.push_back(new Tree());
	}
	Tree* get(const string& key) {
		for (int i = 0; i < segments.size(); i++) {
			if (segments[i] == key) return trees[i];
		}
		return NULL;
	}
	~Tree() {
		for (int i = 0; i < trees.size(); i++) {
			delete trees[i];
		}
	}
};

int maketree(Tree& srctree) {
	size_t nbytes = 254;
	char *buffer = new char[nbytes + 1];
	getline(&buffer, &nbytes, stdin);
	char *path = buffer + 1, *finder = path;
	int mkdirs = 0;
	Tree *tree = &srctree;

	bool nextbreak = false;
	do {
		while (isalnum(*finder)) finder++;
		if (*finder != '/') nextbreak = true;
		*finder = '\0';

		if (!tree->find(path)) {
			tree->create(path);
			mkdirs++;
		}
		tree = tree->get(path);

		path = finder + 1;
		finder = path;
	} while (!nextbreak);

	delete [] buffer;

	return mkdirs;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int numcases;
	scanf("%d\n", &numcases);
	for (int cas = 0; cas < numcases; cas++) {
		Tree tree;
		int n, m;
		scanf("%d %d\n", &n, &m);

		for (int i = 0; i < n; i++) maketree(tree);
		int nummkdirs = 0;
		for (int i = 0; i < m; i++) nummkdirs += maketree(tree);

		printf("Case #%d: %d\n", cas + 1, nummkdirs);
	}
}

