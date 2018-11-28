#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
int L, D, N;
map < string, int > myp;
vector <string> tp;
struct node
{
	set <char> cs;
};
vector <node> res;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, j, k, ans;
	char s[1111];
	scanf("%d %d %d", &L, &D, &N);
	tp.clear();
	for (i = 1; i <= D; ++i)
	{
		scanf("%s", s);
		tp.push_back(string(s));
	}
	for (i = 1; i <= N; ++i)
	{
		scanf("%s", s);
		res.clear();
		res.resize(L);
		for (k = j = 0; j < L; ++j)
		{
			res[j].cs.clear();
			if (s[k] == '(')
			{
				for (++k; s[k] != ')'; ++k)
				{
					res[j].cs.insert(s[k]);
				}
				++k;
			}
			else
			{
				res[j].cs.insert(s[k]);
				++k;
			}
		}
		for (ans = j = 0; j < D; ++j)
		{
			for (k = 0; k < L; ++k)
			{
				if (res[k].cs.count(tp[j][k]) == 0)
				{
					break;
				}
			}
			if (k == L)
			{
				++ans;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
