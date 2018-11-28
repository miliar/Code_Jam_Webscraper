#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

void solve(int _T)
{
	int N;
	cin >> N;

	char c; int d, last;
	int x[2], t[2];
	x[0] = x[1] = 1;
	last = t[0] = t[1] = 0;
	while (N --) {
		cin >> c >> d;
		bool tar = (c == 'O');
		int cur = max(t[tar] + abs(d - x[tar]), last);
		t[tar] = last = cur + 1;
		x[tar] = d;
	}
	printf("Case #%d: %d\n", _T, max(t[0], t[1]));
}

int main() 
{
	int T;
	cin >> T;
	for (int _T = 1; _T <= T; _T ++)
		solve(_T);
}
