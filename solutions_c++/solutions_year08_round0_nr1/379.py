#include <stdio.h>
#include <set>
#include <string>
#include <iostream>

using namespace std;

char _s[1000];

int go()
{
	int S;
	int ret = 0;
	scanf("%d\n", &S);
	set<string> u;
	for (int i = 0; i < S; ++i) {
		gets(_s);
		u.insert(string(_s));
	}
	int q;
	scanf("%d\n", &q);
	set<string> z;
	for (int i = 0; i < q; ++i) {
		gets(_s);
		string s = _s;
		if (u.count(s) && !z.count(s)) {
			if (z.size() + 1 == u.size())
			{
				z.clear();
				++ret;
			}
			z.insert(s);
		}
	} 
	return ret;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	cin >> N;
	for (int i = 1; i <= N; ++i)
		printf("Case #%d: %d\n", i, go());
}