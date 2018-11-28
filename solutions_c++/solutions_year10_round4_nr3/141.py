#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <map>
#include <algorithm>
#include <queue>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 0

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
	fflush(stdout);
#endif
}


typedef std::pair<int, int> pii;

/*class event
{
public:
	int type;
	pii pos;
	int time;
	event(int type = 0, int x = 0, int y = 0, int time = 0)
	{
		this->type = type;
		this->pos = std::make_pair(x, y);
		this->
	}
};

std::queue<event> q;
*/

int world[200][200];
int temp[200][200];

const int infty = 1e9;

int get(int x, int y)
{
	if (x < 0 || y < 0)
		return 0;
	return temp[x][y];
}

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	clr(world);
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		int x1, x2,y1,y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for(int i = x1; i <= x2; i++)
			for(int j = y1; j <= y2; j++)
			{
				world[i][j] = 1;
			}		
	}
	int time = 0;
	while(1)
	{
		time ++;
		bool flag = false;
		memcpy(temp, world, sizeof(world));

			dbg("\n");
		for(int i = 0; i < 200; i++)
		{			
			for(int j = 0; j < 200; j++)
			{
				dbg("%d", world[i][j]);
				if (get(i,j) + get(i-1,j) + get(i, j-1) >= 2)
				{
					world[i][j] = 1;
					flag = 1;
				}
				else
					world[i][j] = 0;
			}
			dbg("\n");
		}
		if (!flag)
			break;
	}	
	printf("%d\n", time);


}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
