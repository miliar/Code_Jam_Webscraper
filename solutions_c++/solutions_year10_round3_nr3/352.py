#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

struct node{
	int size;
	int count;
};

int cmp(const void *a, const void *b)
{
	return  ((node*)b)->size - ((node*)a)->size;
}

#define N 513

int map[N][N];

int n, m;



node square[N*N];
int pos;

int tohex(char c)
{
	if(c >= '0' && c <= '9') return c - '0';
	if(c >= 'A' && c <= 'F') return c - 'A' + 10;
	return 0;
}

void add(int s)
{
	int i;
	for(i = 0; i < pos; i++)
	{
		if(square[i].size == s)
		{
			square[i].count ++;
			break;
		}
	}
	if(i >= pos)
	{
		square[pos].size = s;
		square[pos].count = 1;
		pos++;
	}
}

void use(int x, int y, int s)
{
	int i, j;
	for(i = x; i < m && (i - x) < s; i++)
	{
		for(j = y; j < n && (j - y) < s; j++)
		{
			map[i][j] = -1;
		}
	}
}

int search(int x, int y)
{
	int i;
	int s = 1;
	while(1)
	{
		for(i = 0; i < s && i + x < m; i++)
		{
			if(map[x+i][y+s] == -1) break;
			if(map[x+i][y+s-1] == map[x+i][y+s])break;
		}
		if(i < s && i + x < m) break;
		for(i = 0; i < s && i + y < n; i++)
		{
			if(map[x+s][y+i] == -1) break;
			if(map[x+s-1][y+i] == map[x+s][y+i])break;
		}
		if(i < s && i + y < n) break;

		if(map[x + s][y + s] == -1) break;
		if(map[x + s][y + s] == map[x + s - 1][y + s]) break;
		if(map[x + s][y + s] == map[x + s][y + s - 1]) break;

		s++;
	}
	return s;
}

void print()
{
	int i, j;
	for(i = 0; i < m; i++)
	{
		for(j = 0; j < n; j++)
		{
			printf("%d", map[i][j]);
		}
		printf("\n");
	}

}

int main()
{
	freopen("C-small.in.txt", "r", stdin);
	freopen("C-small.out.txt", "w", stdout);
	//freopen("C-large.in.txt", "r", stdin);
	//freopen("C-large.out.txt", "w", stdout);

	int t, i, j, k;
	int len, bit;
	char row[N];
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		scanf("%d %d", &m, &n);
		for(j = 0; j < m; j++)
		{
			scanf("%s", row);
			len = n / 4;
			for(k = 0; k < n; k += 4)
			{
				bit = tohex(row[k/4]);
				map[j][k] = ((bit & 0x8) > 0) ? 1 : 0;
				map[j][k+1] = ((bit & 0x4) > 0) ? 1 : 0;
				map[j][k+2] = ((bit & 0x2) > 0) ? 1 : 0;
				map[j][k+3] = ((bit & 0x1) > 0) ? 1 : 0;				
			}
		}
		pos = 0;

		//print();
		int maxx, maxy, maxs;
		int sum = m * n;
		while(sum > 0)
		{
			maxs = 0;
			for(j = 0; j < m; j++)
			{
				for(k = 0; k < n; k++)
				{
					if(map[j][k] != -1)
					{
						len = search(j, k);
						if(len > maxs) {
							maxx = j;
							maxy = k;
							maxs = len;
						}
					}
				}
			}
			if(j < m) break;
			use(maxx, maxy, maxs);
			add(maxs);
			sum -= maxs * maxs;
		}
		//print();
		qsort(square, pos, sizeof(node), cmp);
		printf("Case #%d: %d\n", i + 1, pos);
		for(j = 0; j < pos; j++)
		{
			printf("%d %d\n", square[j].size, square[j].count);
		}
	}
	return 0;
}