#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

bool win(int a, int b)
{
	if (a >= 2 * b) return true;
	else return !win(b, a-b);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int cnt = 0;
		for (int a = a1; a <= a2; a++)
			for (int b = b1; b <= b2; b++)
				if (win(max(a,b),min(a, b)))
					cnt++;
		cout << "Case #" << t << ": " << cnt << endl;
	}
}