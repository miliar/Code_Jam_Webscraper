#include <set>
#include <iostream>
#include <string>

using namespace std;
int test;
void work()
{
	int s, q, ans = 0;
	scanf("%d", &s);
	char tmp[300];
	gets(tmp);
	set<string> S;
	for (int i = 0; i < s; ++i)
		gets(tmp);
	scanf("%d", &q);
	gets(tmp);
	for (int i = 0; i < q; ++i)
	{
		gets(tmp);
		S.insert(tmp);
		if (S.size() == s)
		{
			++ans;
			S.clear();
			S.insert(tmp);
		}
	}
	if (!S.empty())
		++ans;
	if (!ans)
		++ans;
	printf("Case #%d: %d\n", ++test, --ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
