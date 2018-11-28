#include<stdio.h>
#include<string>
#include<vector>
#include<map>
using namespace std;

struct SNode
{
	string name;
	vector<SNode> childs;
	//map<string, SNode> childs;
};

SNode root;

char epath[105][1000], cpath[105][1000];
int nexist, ncreate;

int ccount;

void clearTree(SNode &nownode)
{
	int i;

	for (i = 0; i < nownode.childs.size(); i ++) {
		clearTree(nownode.childs[i]);
	}
	nownode.childs.clear();
}

void buildTree(SNode &nownode, char *path, int len, int nowp, bool tocount)
{
	int i, j, k;
	string dname;
	int nextp;

	if (nowp >= len) return;

	dname = "";
	for (i = nowp; i < len; i ++) {
		if (path[i] == '/') break;
		dname += path[i];
	}
	nextp = i + 1;

	for (i = 0; i < nownode.childs.size(); i ++) {
		if (nownode.childs[i].name.compare(dname) == 0) {
			buildTree(nownode.childs[i], path, len, nextp, tocount);
			break;
		}
	}

	if (i >= nownode.childs.size()) {
		if (tocount) ccount ++;
		SNode newnode;

		newnode.childs.clear();
		newnode.name = dname;
		nownode.childs.push_back(newnode);
		buildTree(nownode.childs[nownode.childs.size() - 1], path, len, nextp, tocount);
	}
}

int main()
{
	int i, j, k;
	int t, nowt;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;
		scanf("%d%d", &nexist, &ncreate);
		for (i = 0; i < nexist; i ++) {
			scanf("%s", epath[i]);
		}
		for (i = 0; i < ncreate; i ++) {
			scanf("%s", cpath[i]);
		}

		clearTree(root);

		ccount = 0;
		for (i = 0; i < nexist; i ++) {
			buildTree(root, epath[i], strlen(epath[i]), 1, false);
		}

		for (i = 0; i < ncreate; i ++) {
			buildTree(root, cpath[i], strlen(cpath[i]), 1, true);
		}

		printf("Case #%d: %d\n", nowt, ccount);
	}

	return 0;
}



