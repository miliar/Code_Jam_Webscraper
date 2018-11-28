#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
const char input[] = "B-small-attempt0.in";
const char output[] = "output.txt";

char a[20][20];
size_t ans = 0, R, C, D;

size_t size(size_t x0, size_t y0, size_t x1, size_t y1)
{
	if(x0 >= x1 || y0 >= y1)
		return 0;
	if(x1 - x0 != y1 - y0)
		return 0;
	return x1 - x0 + 1;
}

void update(size_t x0, size_t y0, size_t x1, size_t y1)
{
	size_t now = size(x0, y0, x1, y1);
	if(now <= ans)
		return;
	size_t cx = x0 + x1, cy = y0 + y1, px = 0, py = 0;
	size_t sum = 0;
	for(auto i = x0; i <= x1; i++)
		for(auto j = y0; j <= y1; j++)
			if((i != x0 && i != x1) || (j != y0 && j != y1)) {
				size_t m = a[i][j] - '0' + D;
				sum += m;
				px += m * i;
				py += m * j;
			}
	if(px * 2 == cx * sum && py * 2 == cy * sum)
	{
		cerr << x0<<' '<<y0<<' '<<x1<<' '<<y1<<endl;
		ans = now;
	}
}

void work()
{
	ans = 0;
	cin >> R >> C >> D;
	for(size_t i = 0; i < R; i++)
		cin >> a[i];
	for(size_t x0 = 0; x0 < R; x0 ++)
		for(size_t y0 = 0; y0 < C; y0 ++)
			for(size_t x1 = 0; x1 < R; x1 ++)
				for(size_t y1 = 0; y1 < C; y1 ++)
					update(x0, y0, x1, y1);
	if(ans >= 3)
		cout << ans << endl;
	else 
		puts("IMPOSSIBLE");
}

int main()
{
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
	int kase;
	scanf("%d", &kase);
	for(int i = 1; i <= kase; i++) {
		printf("Case #%d: ", i);
		work();
	}
}
