#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}




int map[1000][1000];

const int shift_x[] = {-1, 0, 0, 1, 0};
const int shift_y[] = {0, -1, 1, 0, 0};


int find(int x, int y)
{
	int ans = 4;
	int h = map[x][y];
	for(int i = 0; i < 4; i++)
	{
		int d = map[x+shift_x[i]][y+shift_y[i]];
		if (d < h)
		{
			h = d;
			ans = i;
		}
	}
	return ans;
}

int code(int x, int y)
{
	return x * 2000 + y;
}


class disjoint_set
{
public:
	int p[1000000];
	int w[1000000];
	void clear()
	{
		for(int i = 0; i < 1000000; i++)
		{
			p[i] = i;
			w[i] = 0;
		}
	}
	int find(int a)
	{
		if (a != p[a])
			p[a] = find(p[a]);
		return p[a];
	}
    void join(int a, int b)
    {
    	a = find(a);
    	b = find(b);
    	if (a == b)
    		return;
    	if (w[a] < w[b])
    	{
    		p[a] = b;
    	}
    	else
    	{
    		p[b] = a;
    		if (w[a] == w[b])
    			w[a] ++;
    	}
    }
}set;

char let[1000000];

void solve(int test_case)
{
	printf("Case #%d: \n", test_case);
	int w,h;
	scanf("%d%d", &h, &w);
	set.clear();
	clr(let);
	for(int i = 0; i <= h+1; i++)
		for(int j = 0; j <= w + 1; j++)
		{
			map[i][j] = 1<<30;
		}
	for(int i = 1; i <= h; i++)
		for(int j = 1; j <= w; j++)
		{
			scanf("%d", &map[i][j]);
		}
	for(int i = 1; i <= h; i++)
		for(int j = 1; j <= w; j++)
		{
			int x = find(i,j);
			set.join(code(i,j), code(i + shift_x[x], j + shift_y[x]));
		}
	char l ='a';
	for(int i = 1; i <= h; i++)
	{
		for(int j = 1; j <= w; j++)
		{
			int num =set.find(code(i,j));
			if (let[num] == 0)
				let[num] = l++;
			printf("%c ", let[num]);
		}   	
		printf("\n");
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
