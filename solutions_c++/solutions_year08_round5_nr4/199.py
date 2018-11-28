#include <stdio.h>
#include <stdarg.h>

#define IS_DEBUG 1

void dgb(const char * fmt, ...)
{
	#if IS_DEBUG
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
	#endif
}


bool is_rock[200][200];
int answer[200][200];


void solve(int test_case)
{
	for(int i = 0; i < 200; i++)
		for(int j = 0; j < 200; j++)
		{		
			answer[i][j] = 0; 
			is_rock[i][j] = false;
		}
	int h,w,r;
	scanf("%d%d%d", &h, &w, &r);
	for(int i = 0; i < r; i++)
	{
		int x,y;
		scanf("%d%d", &x, &y);
		is_rock[x-1][y-1] = true;
	}
	answer[0][0] = 1;
	for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++)
		{
			answer[i][j] %= 10007;
			if (!is_rock[i][j])
			{
				answer[i+2][j+1] += answer[i][j];
				answer[i+1][j+2] += answer[i][j];
			}
		}
	
	printf ("Case #%d: %d\n", test_case, answer[h-1][w-1] % 10007);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}