#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_N = 1000000 + 5;

int win[MAX_N];
int lastWin[MAX_N];
int T;
int main()
{
	lastWin[1] = 0;
	win[1] = 2;
	for(int i = 2; i <= 1000000; i ++)
	{
		lastWin[i] = upper_bound(win + 1, win + i, i) - win - 1;
		win[i] = lastWin[i] + i + 1;
	}
	scanf("%d", &T);
	for(int t = 0; t < T; t ++)
	{
		long long a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		long long res = 0;
		for(long long i = a1; i <= a2; i ++)
		{
			long long t1 = 1, t2 = lastWin[i];
			long long l = max(t1, b1);
			long long r = min(t2, b2);
			if( l <= r )	res += r - l + 1;
			t1 = win[i];	t2 = MAX_N;
			l = max(t1, b1);
			r = min(t2, b2);
			if( l <= r )	res += r - l + 1;
		}
		cout << "Case #" << t + 1 << ": "<< res << "\n";
	}
}
