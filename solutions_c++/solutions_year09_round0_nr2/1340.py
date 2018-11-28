#include <stdio.h>
#include <stdlib.h>

FILE* fp1;
FILE* fp2; 
char hh;
int t, h, w, r, R, s;
int m[105][105];
char mm[105][105];
int dir[4][2]={-1, 0, 0, -1, 0, 1, 1, 0};
struct p
{
	int x, y;
}res[10005];

p check()
{
	p s;
	s.x = -1;
	s.y = -1;
	bool flag = false;
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
			if (mm[i][j] == ' ')
			{
				s.x = i;
				s.y = j;
				flag = true;
				break;
			}
		if (flag) break;
	}
	return s;
}

p mmin(p x)
{
	p re;
	int x1 = -1, y1 = -1;
	int s1 = 100000;
	for (int i = 0; i < 4; i++)
	{
		re.x = x.x + dir[i][0];
		re.y = x.y + dir[i][1];
		if (re.x >= 0 && re.x < h && re.y >= 0 && re.y < w)
		{
			if (s1 > m[re.x][re.y]) 
			{
				s1 = m[re.x][re.y];
				x1 = re.x;
				y1 = re.y;
			}
		} 
	}
	re.x = x1;
	re.y = y1;
	return re;
}

int main()
{
	fp1 = fopen("B-large.in", "r+");
	fp2 = fopen("b.txt", "w+");
	fscanf (fp1, "%d", &t);
	for (int pp = 1; pp <= t; pp++)
	{
		fscanf (fp1, "%d%d", &h, &w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
			{
				fscanf (fp1, "%d", &m[i][j]);
				mm[i][j] = ' ';
			}
		hh = 'a';
		while (1)
		{
			p re = check();
			if (re.x == -1 && re.y == -1) 
			{
				break;
			}
			r = 0;
			R = 1;
			res[r].x = re.x;
			res[r].y = re.y;
			mm[re.x][re.y] = hh;
			while (r < R)
			{
				int x = res[r].x;
				int y = res[r].y;
				int xx, yy, x1, y1;
				p kk = mmin(res[r]);
				if (kk.x != -1 && m[kk.x][kk.y] < m[x][y] && mm[kk.x][kk.y] == ' ')
				{
					res[R].x = kk.x;
					res[R].y = kk.y;
					mm[res[R].x][res[R].y] = hh;
					R++;
				}
				for (int i = 0; i < 4; i++)
				{
					xx = x + dir[i][0];
					yy = y + dir[i][1];
					if (xx >= 0 && xx < h && yy >= 0 && yy < w && mm[xx][yy] == ' ')
					{
						if (m[x][y] < m[xx][yy]) 
						{
							p t;
							t.x = xx;
							t.y = yy;
							p kkk = mmin(t);
							if (kkk.x == x && kkk.y == y)
							{
								res[R].x = t.x;
								res[R].y = t.y;
								mm[res[R].x][res[R].y] = hh;
								R++;
							}
						}
					} 
				}
				r++;
			}
			hh++;
		}
		fprintf(fp2, "Case #%d:\n", pp);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (j != w - 1) fprintf (fp2, "%c ", mm[i][j]);
				else fprintf (fp2, "%c\n", mm[i][j]);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}

