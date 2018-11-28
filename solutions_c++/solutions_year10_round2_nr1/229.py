#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)

using namespace std;

int treecount;
struct tree {
	string name;
	map<string, tree *> children;
	
	tree(string dir): name(dir) {}
	
	void insert(char *name) {
		char dirname[1024], *ptr = dirname;
		string dir;
		
		while(*name && *name != '/') *(ptr++) = *(name++);
		*ptr = 0;
		
		dir = dirname;
		
		if(children.find(dir) == children.end()) {
			treecount++;
			children.insert(make_pair(dir, new tree(dir)));
		}
		
		if(*name)
			children[dir]->insert(name+1);
	}
};

int main() {
	int T, N, M, ans;
	char cline[1024];
	
	scanf("%d\n", &T);
	
	FOR(nCase, T) {
		scanf("%d %d\n", &N, &M);
		
		tree *root = new tree("");
		
		FOR(i, N) {
			scanf("%s\n", cline);
			root->insert(cline+1);
		}
		
		treecount = 0;
		
		ans = 0;
		
		FOR(i, M) {
			scanf("%s\n", cline);
			root->insert(cline+1);
		}
		
		printf("Case #%d: %d\n", nCase+1, treecount);
	}
}
