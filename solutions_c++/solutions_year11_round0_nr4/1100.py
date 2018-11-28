#include <iostream>

using namespace std;

int p[1010];
int test;
int sol[1010];
void go()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> p[i];
	int total = 0;
	for (int i = 1; i <= n; ++i) if (p[i])
	{
		int ciclu = 0;
		int st = i;
		while (p[st])
		{
			int nxt = p[st];
			p[st] = 0;
			st = nxt;
			++ciclu;
		}
		total += sol[ciclu];
	}
	cout << "Case #" << ++test << ": " << total << ".000000\n";
}
int main()
{
	int t; cin >> t;
	sol[0] = sol[1] = 0;
	sol[2] = 2;
	sol[3] = 3;
	for (int i = 4; i <= 1000; ++i)
	{
		sol[i] = i;
	}
	while (t--) go();
	return 0;
}
