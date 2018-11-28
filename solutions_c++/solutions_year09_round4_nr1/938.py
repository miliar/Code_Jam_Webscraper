#include <iostream>
#include <list>
#include <queue>
#include <set>
#include <map>

#define N 50

using namespace std;

char t[N+2][N+2];
long n;
long ls[N+2];
long ban[N+2] = {0,};
void logic()
{
	memset(ban, 0, sizeof(ban));
	cin >> n;
	long y;
	for(y = 1; y <= n; y++)
	{
		cin >> &t[y][1];
	}

	long last;
	long j;
	for(y = 1; y <= n; y++)
	{
		last =  1;
		for(j = 1; j <= n; j++)
		{
			if (t[y][j] == '1') {last = j;}
		}
		ls[y] = last;
	}
	long ans = 0;
	long z;
	long cnt;

	for(y = 1; y <= n; y++)
	{
		for(j = 1; j <= n; j++)
		{
			if (ban[j]) {continue;}
			if (ls[j] <= y)
			{
				ban[j] = 1;
				cnt = 0;
				for(z = j-1; z >= 1; z--)
				{
					if (!ban[z]) {cnt++;}
				}
				ans += cnt;
				break;
			}
		}
	}
	cout << ans;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	long t, y;
	cin >> t;
	for(y = 1; y <= t; y++)
	{
		cout << "Case #" << y << ": ";
		logic();
		cout << "\n";
	}
}