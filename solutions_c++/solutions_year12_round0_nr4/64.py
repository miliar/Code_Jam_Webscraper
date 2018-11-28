#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

struct position
{
	int x, y;
	
	position(int x = 0, int y = 0) : x(x), y(y) { }
	
	position(const position &P) : x(P.x), y(P.y) { }
	
	bool equals(const position &P)
	{
		return x == P.x && y == P.y;
	}
};

void mirror(int &p, int &s)
{
	s = -s, p += s;
}

int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int i = 0; i < N; i++)
	{
		int H, W, D;
		scanf("%d %d %d\n", &H, &W, &D);
		
		string *map = new string[H];
		position start;
		for(int j = 0; j < H; j++)
		{
			getline(cin, map[j]);
			
			size_t found = map[j].find('X');
			if(found != string::npos)
				start.x = j, start.y = (int)found;
		}
		
		int score = 0, killed = 0;
		for(int s = -D; s <= D; s++)
		for(int k = sqrt((double)D * D - s * s), t = -k; t <= k; t++)
		{
			//printf("%d %d:\n", s, t), fflush(stdout);
			if(s == 0 && t == 0)
				continue;
			
			position X(start);
			int sx = s > 0 ? 1 : -1, sy = t > 0 ? 1 : -1, dx = 2 * fabs((double)s), dy = 2 * fabs((double)t), error, p_error;
			if(dx >= dy)
			{
				p_error = error = dx / 2;
				for(int u = 0; u < dx / 2; u++, p_error = error)
				{
					X.x += sx, error += dy;
					if (error > dx)
					{
						X.y += sy, error -= dx;
						if(error + p_error > dx)
						{
							if(map[X.x - sx][X.y] == '#')
							{
								mirror(X.y, sy);
								if(map[X.x][X.y] == '#')
									mirror(X.x, sx);
							}
							else if(map[X.x][X.y] == '#')
								mirror(X.x, sx);
						}
						else if(error + p_error < dx)
						{
							if(map[X.x][X.y - sy] == '#')
							{
								mirror(X.x, sx);
								if(map[X.x][X.y] == '#')
									mirror(X.y, sy);
							}
							else if(map[X.x][X.y] == '#')
								mirror(X.y, sy);
						}
						else if(error + p_error == dx && map[X.x][X.y] == '#')
						{
							if(map[X.x - sx][X.y] != '#' && map[X.x][X.y - sy] != '#')
							{
								killed++;
								break;
							}
							else if(map[X.x - sx][X.y] == '#' && map[X.x][X.y - sy] == '#')
							{
								mirror(X.x, sx), mirror(X.y, sy), error = dx - p_error;
							}
							else if(map[X.x - sx][X.y] == '#')
							{
								mirror(X.y, sy);
							}
							else if(map[X.x][X.y - sy] == '#')
							{
								mirror(X.x, sx);
							}
						}

					}
					else if(map[X.x][X.y] == '#')
						mirror(X.x, sx);
					
					if(X.equals(start) && error == dx / 2)
					{
						if(u == dx / 2 - 1)
							score++;
						break;
					}
				}
			}
			else
			{
				p_error = error = dy / 2;
				for(int u = 0; u < dy / 2; u++, p_error = error)
				{				
					X.y += sy, error += dx;
					if (error > dy)
					{
						X.x += sx, error -= dy;
						if(error + p_error > dy)
						{
							if(map[X.x][X.y - sy] == '#')
							{
								mirror(X.x, sx);
								if(map[X.x][X.y] == '#')
									mirror(X.y, sy);
							}
							else if(map[X.x][X.y] == '#')
								mirror(X.y, sy);
						}
						else if(error + p_error < dy)
						{
							if(map[X.x - sx][X.y] == '#')
							{
								mirror(X.y, sy);
								if(map[X.x][X.y] == '#')
									mirror(X.x, sx);
							}
							else if(map[X.x][X.y] == '#')
								mirror(X.x, sx);
						}
						else if(error + p_error == dy && map[X.x][X.y] == '#')
						{
							if(map[X.x - sx][X.y] != '#' && map[X.x][X.y - sy] != '#')
							{
								killed++;
								break;
							}
							else if(map[X.x - sx][X.y] == '#' && map[X.x][X.y - sy] == '#')
							{
								mirror(X.x, sx), mirror(X.y, sy), error = dy - p_error;
							}
							else if(map[X.x][X.y - sy] == '#')
							{
								mirror(X.x, sx);
							}
							else if(map[X.x - sx][X.y] == '#')
							{
								mirror(X.y, sy);
							}
						}
					}
					else if(map[X.x][X.y] == '#')
						mirror(X.y, sy);
					
					
					if(X.equals(start) && error == dy / 2)
					{
						if(u == dy / 2 - 1)
							score++;
						break;
					}
				}
			}
			
		}
		
		delete[] map;
		printf("Case #%d: %d\n", i + 1, score);
	}
	
	return 0;
}
