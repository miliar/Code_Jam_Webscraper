#include <iostream>
using namespace std;

char map[110][110];

int s[110][110] , h , w , mark[10010];

int dir[4][2] = {{-1 , 0} , {0 , -1} , {0 , 1} , {1 , 0}};

int find(int x)
{
	if(mark[x] != x)
		mark[x] = find(mark[x]);
	return mark[x];
}

int get(int x , int y)
{
	return x * w  + y;
}

int main()
{
	int i , j , cas , t , k , MIN , d , id , x , y , b , a;
	cas = 0;
	int fa , fb;
	freopen("2.txt" , "w" , stdout);
	scanf("%d" , &t);
	while(t --)
	{
		cas ++; 
		scanf("%d %d" , &h , &w);
		for(i = 0 ; i < h ; i ++)
		{
			for(j = 0 ; j < w ; j ++)
			{
				map[i][j] = '0';
				b = get(i , j);
				mark[b] = b;
				scanf("%d" , &s[i][j]);
			}
		}
		for(i = 0 ; i < h ; i ++)
		{
			for(j = 0 ; j < w ; j ++)
			{
				MIN = s[i][j];
				id = -1;
				for(d = 0 ; d < 4 ; d ++)
				{
					x = i + dir[d][0];
					y = j + dir[d][1];
					if(x < 0 || x >= h || y < 0 || y >= w)
						continue;
					if(s[x][y] < MIN)
					{
						id = d;
						MIN = s[x][y];
					}
				}
				if(id == -1)
					continue;
				x = i + dir[id][0];
				y = j + dir[id][1];
				a = get(i , j);
				b = get(x , y);
				fa = find(a);
				fb = find(b);
				if(fa != fb)
				{
					if(fa < fb)
						mark[fb] = fa;
					else
						mark[fa] = fb;
				}
			}
		}
		k = 0;
		for(i = 0 ; i < h ; i ++)
		{
			for(j = 0 ; j < w ; j ++)
			{
				a = get(i , j);
				fa = find(a);
				if(fa == a)
				{
					map[i][j] = k + 'a';
					k ++;
				}
				else
				{
					map[i][j] = map[fa / w][fa % w];
				}
			}
		}
		printf("Case #%d:\n" , cas);
		for(i = 0 ; i < h ; i ++)
		{
			for(j = 0 ; j < w ; j ++)
			{
				if(j == w - 1)
					printf("%c\n" , map[i][j]);
				else
					printf("%c " , map[i][j]);
			}
		}
	}
	return 0;
}