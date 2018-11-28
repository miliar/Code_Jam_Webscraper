#include <stdio.h>
#include <map>
#include <string>
#include <vector>

using namespace std;

int ans = 0;
std::vector<std::map<string, int> > V;

void fun (char* buf, int funny)
{
	string tmp;

	int cur = 0;
	for (int j = 0; buf[j];)
	{
		tmp = "";
		j ++;
		while (buf[j] != '/' && buf[j])
			tmp += buf[j ++];
		if (V[cur].find(tmp) == V[cur].end())
		{
			ans += funny;
			V.push_back(std::map<string,int>());
			V[cur][tmp] = V.size() - 1;
		}

		cur = V[cur][tmp];
	}

}

int main ()
{
	freopen ("a_large.in", "r", stdin);
	freopen ("a_large.out", "w", stdout);

	int ct, t;
	int n, m;

	t = 0;
	for (scanf("%d", &ct); ct > 0; ct --)
	{
		V.clear ();
		V.push_back (std::map<string,int>());
		ans = 0;

		scanf ("%d%d", &n, &m);
		for (int i = 0; i < n; i ++)
		{
			char buf[1000];
			scanf ("%s", buf);

			fun (buf, 0);			
		}
		for (int i = 0; i < m; i ++)
		{
			char buf[1000];
			scanf ("%s", buf);

			fun (buf, 1);			
		}

		printf ("Case #%d: %d\n", ++ t, ans);
	}

	return 0;
}