#include <stdio.h>
#include <stdarg.h>
#include <cassert>

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


int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a < b ? b : a;
}

int curx, cury;
int cur_direction;


int minx[10000], maxx[10000], miny[10000], maxy[10000];
char inp_str[100];
__int64 area;

int MINX, MAXX, MINY, MAXY;

void processString()
{
	for(int i = 0; inp_str[i] != 0; i++)
	{
		int oldx = curx;
		int oldy = cury;
		if (inp_str[i] == 'F')
		{
			if (cur_direction == 0)
			{
				miny[curx+5000] = min(miny[curx+5000], cury);
				maxy[curx+5000] = max(maxy[curx+5000], cury);
				curx++;
			}
			if (cur_direction == 1)
			{
				minx[cury+5000] = min(minx[cury+5000], curx);
				maxx[cury+5000] = max(maxx[cury+5000], curx);
				cury++;
			}
			if (cur_direction == 2)
			{
				miny[curx-1+5000] = min(miny[curx-1+5000], cury);
				maxy[curx-1+5000] = max(maxy[curx-1+5000], cury);
				curx--;
			}
			if (cur_direction == 3)
			{
				minx[cury-1+5000] = min(minx[cury-1+5000], curx);
				maxx[cury-1+5000] = max(maxx[cury-1+5000], curx);
				cury--;
			}
			area += curx*oldy - oldx*cury;
		}
		else if (inp_str[i] == 'L')
		{
			cur_direction = (cur_direction + 3) % 4;
		}
		else if (inp_str[i] == 'R')
		{
			cur_direction = (cur_direction + 1) % 4;
		}
		else
			assert(false);
		MINX = min(MINX, curx);
		MINY = min(MINY, cury);
		MAXX = max(MAXX, curx);
		MAXY = max(MAXY, cury);
		
	}
}



void solve(int test_case)
{
	curx = cury = 0;
	cur_direction = 3;
	MINX = MINY = 10000;
	MAXX = MAXY = -10000;
	area = 0;
	for(int i = 0; i < 10000; i++)
	{
		minx[i] = miny[i] = 10000;
		maxx[i] = maxy[i] = -10000;
	}
	int l;
	scanf("%d", &l);
	for(int i = 0; i < l; i++)
	{
		int t;
		scanf("%s%d", &inp_str, &t);
		for(int j = 0; j < t; j++)
			processString();
	}
	assert(curx == 0 && cury == 0);
	__int64 area2 = 0;
	for(int x = MINX; x <= MAXX; x++)
		for(int y = MINY; y <= MAXY; y++)
			if ((maxx[y+5000] > x && minx[y+5000] <= x) || (maxy[x+5000] > y && miny[x+5000] <= y))
				area2++;
	assert(area % 2 == 0);
	if (area < 0)
		area = -area;
	
	printf ("Case #%d: %I64d\n", test_case, area2-area/2);
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