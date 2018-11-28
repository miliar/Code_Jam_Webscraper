#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ext/hash_map>
#include <queue>

using namespace std;
using namespace __gnu_cxx;
deque<char *> tofree;

struct eqstr {
	bool operator()(const char* s1, const char* s2) const
	{
		return strcmp(s1, s2) == 0;
	}
};

struct dir_t;

typedef hash_map<const char *, dir_t *, hash<const char*>, eqstr> hm;

struct dir_t {
	char *name;
	int n, s;
	hm sub;
} *root;

dir_t *new_dir(const char *name)
{
	dir_t *ret = new dir_t;
	ret->name = strdup(name);
	ret->n = ret->s = 0;
	return ret;
}

void free_dirs(dir_t *dir)
{
	//printf("free %s\n", dir->name);
	for (hm::iterator it = dir->sub.begin(); it != dir->sub.end(); it++) {
		free_dirs(it->second);
	}
	free(dir->name);
	delete dir;
}

int create(dir_t *dir, char *path)
{
	if (!path) return 0;
	char *p = strchr(path, '/');
	if (p) {
		*p = 0;
		p++;
	}
	hm::iterator it = dir->sub.find(path);
	//printf("in %s create %s (%s) %d\n", dir->name, path, p, it != dir->sub.end());
	if (it == dir->sub.end()) {
		dir_t *s = new_dir(path);
		char *q = strdup(path);
		tofree.push_front(q);
		dir->sub[q] = s;
		return create(s, p) + 1;
	} else {
		return create(it->second, p);
	}
}

int main()
{
	int t, m, n, c, i, count;
	char buf[1000];
	scanf("%d", &t);
	for (c = 1; c <= t; c++) {
		root = new_dir("");
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s", buf);
			create(root, buf + 1);
		}
		count = 0;
		for (i = 0; i < m; i++) {
			scanf("%s", buf);
			count += create(root, buf + 1);
		}
		printf("Case #%d: %d\n", c, count);
		free_dirs(root);
		while (!tofree.empty()) {
			char *p = tofree.front();
			tofree.pop_front();
			free(p);
		}
	}
	return 0;
}
