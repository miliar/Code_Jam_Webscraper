#include<cstdio>
#include<cstring>

typedef struct point {
	int x, y;
}POINT;

int T, H, W;
int map[101][101], mark[101][101];
int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

bool OK(POINT a)
{
	return a.x >= 0 && a.x < H && a.y >= 0 && a.y < W;
}

POINT rec[10000];

bool find(POINT a, int mm)
{
	int i, j, cnt = 0;
	while( true )
	{
		rec[cnt ++] = a;
		if(mark[a.x][a.y] != -1)break;
		bool flag = true;
		POINT cur = a;
		for(i = 0; i < 4; i ++)
		{
			POINT next;
			next.x = cur.x + d[i][0];
			next.y = cur.y + d[i][1];
			if(OK(next))
			{
				if(map[next.x][next.y] < map[a.x][a.y])
				{
					a = next;
					flag = false;
				}
			}
		}
		if(flag){
			break;
		}
	}
	int tmp = mark[a.x][a.y];
	if(tmp == -1)tmp = mm;
	for(i = 0; i < cnt; i ++)
	{
		mark[rec[i].x][rec[i].y] = tmp;
	}
	return tmp != mm;
}

int main()
{
	int i, j, k, mm, cc = 0;
	//int ii, jj;
	scanf("%d", &T);
	while( T -- )
	{
		memset(mark, -1, sizeof(mark));
		scanf("%d %d", &H, &W);
		for(i = 0; i < H; i ++)
		{
			for(j = 0; j < W; j ++)
			{
				scanf("%d", &map[i][j]);
			}
		}
		mm = 0;
		printf("Case #%d:\n", ++cc);
		for(i = 0; i < H; i ++)
		{
			for(j = 0; j < W; j ++)
			{
				POINT a;
				a.x = i; a.y = j;
				if(!find(a, mm))mm ++;
				putchar('a' + mark[i][j]);
				if(j < W-1)putchar(' ');
				/*for(ii = 0; ii < H; ii ++)
				{
					for(jj = 0; jj < W; jj ++)
					{
						printf("%d ", mark[ii][jj]);
					}
					putchar('\n');
				}*/
			}
			putchar('\n');
		}
	}
	return 0;
}
