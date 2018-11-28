#include <cstdio>
#include <cstring>
#include <string>
#include <map>

using namespace std;

int N, M, res, d;

struct t_list
{
	map<string, t_list*> links;
};

t_list *root;

t_list* add_link(t_list *node, char *str)
{
	string tmp = str;
	if (node->links.find(tmp) == node->links.end())
	{
		t_list *new_node = new t_list();
		node->links[tmp] = new_node;
		res += d;
		return new_node;
	}

	return node->links[tmp];
}

void add_dir(char *str)
{
	++str;
	int L = strlen(str);
	t_list *node = root;

	while (true)
	{
		char *tmp = strchr(str, '/');
		if (tmp == 0) { add_link(node, str); break; }
		*tmp = 0; node = add_link(node, str); str = tmp + 1;
	}
}

void solve()
{
	char cur_line[100001];

	for (int i = 0; i < N; ++i)
	{
		gets(cur_line);
		d = 0; add_dir(cur_line);
	}

	for (int i = 0; i < M; ++i)
	{
		gets(cur_line);
		d = 1; add_dir(cur_line);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		scanf("%d%d\n", &N, &M);
		root = new t_list(); res = 0;
		solve();
		printf("%d\n", res);
	}

	return 0;
}
