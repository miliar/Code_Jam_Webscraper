#include <stdio.h>
#include <string>
#include <map>
#include <vector>
#define maxn 128
#define maxnode 20010
using namespace std;

struct dict{
public:
	char name[maxn];
	map<string, dict*> child;
}node[maxnode];
int curNode;
int T, t = 1;
int n, m;

int buildTree(dict *root, char *str)
{
	if(*str == '\0')
		return 0;

	char *ps = str;
	bool end = false;
	int  ret = 0;
	dict *nextNode;
	while(*ps && *ps != '/')
	{
		++ps;
	}
	if(*ps == '\0')
		end = true;
	*ps = '\0';

	if(root->child.find(str) == root->child.end())
	{
		strcpy(node[curNode].name, str);
		node[curNode].child.clear();
		root->child[str] = &node[curNode];
		nextNode = &node[curNode];
		++curNode;
		++ret;
	}else
		nextNode = root->child[str];

	if(!end)
		return ret + buildTree(nextNode, ps + 1);
	else
		return ret;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for(scanf("%d", &T); T; --T)
	{
		scanf("%d%d", &n, &m);

		char str[maxn];

		curNode = 1;
		node[0].name[0] = '\0';
		node[0].child.clear();

		for(int i = 0; i < n; ++i)
		{
			scanf("%s", str);
			buildTree(&node[0], str + 1);
		}

		int ans = 0;

		for(int i = 0; i < m; ++i)
		{
			scanf("%s", str);
			ans += buildTree(&node[0], str + 1);
		}

		printf("Case #%d: %d\n", t++, ans);
	}
}