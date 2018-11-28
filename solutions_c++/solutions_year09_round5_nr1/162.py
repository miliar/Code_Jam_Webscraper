#include <iostream>

#include <fstream>
#include <vector>

using namespace std;


int r, c;
char a[14][14];
int b[14][14];
int e[14][14];


int beg, end;

int nn = 0;

int que[2000000];
int was[2000000];

int x[5];
int y[5];

const int dx[4] = {1, 0, 0, -1};
const int dy[4] = {0, 1, -1, 0};

int t[14][14];

int Map(int a[14][14])
{
	int i, j, k, f;
	int x[5];
	int y[5];
	memset(t, 0, sizeof(t));

	int qx[5];


	f = 0;
	i = j = 0;
	for (i = 1; i <= r; i++)
	{
		for (j = 1; j <= c; j++)
		{
			if (a[i][j] == 1) 
			{
				f = 1;
				break;
			}
		}
		if (f) break;
	}

	x[0] = i;
	y[0] = j;
	t[i][j] = 1;
	qx[0] = 0;
	int be = 0, en = 0;
	k = 0;
	int xx, yy;
	while (be <= en)
	{
		i = qx[be++];
		for (j = 0; j < 4; j++)
		{
			xx = x[i] + dx[j];
			yy = y[i] + dy[j];
			if (a[xx][yy] == 1 && t[xx][yy] == 0)
			{
				k++;
				x[k] = xx;
				y[k] = yy;
				t[xx][yy] = 1;
				qx[++en] = k;
			}
		}
	}
	k++;
	if (k < nn) return -1;


	int dd[4]; 
	for (i = 1; i < nn; i++)
	{
		f = 0;
		for (j = 0; j < i; j++)
		{
			for (k = 0; k < 4; k++)
			{
				if (x[i] == x[j] + dx[k] && y[i] == y[j] + dy[k])
				{
					dd[i] = k + 4 * j;
					f = 1;
					break;
				}
			}
			if (f) break;
		}
		if (f == 0) return -1;
	}
	f = 0;
	for (i = nn-1; i > 0; i--)
	{
		f = f * (4*i) + dd[i]; 
	}
	f = f * 12 + y[0]-1;
	f = f * 12 + x[0]-1;
	return f;
}



void Load()
{
	int i, j;
	cin >> r >> c;
	memset(a, '#', sizeof(a));
	memset(b, 0, sizeof(b));
	memset(e, 0, sizeof(e));
	memset(x, 0, sizeof(x));
	memset(y, 0, sizeof(y));
	memset(que, 0, sizeof(que));
	memset(was, 0, sizeof(was));
	memset(t, 0, sizeof(t));
	nn = 0;
	for (i = 1; i <= r; i++)
	{
		for (j = 1; j <= c; j++)
		{
			cin >> a[i][j];
			if (a[i][j] == 'o' || a[i][j] == 'w')
			{ 
				b[i][j] = 1;
				nn++;
			}
			if (a[i][j] == 'x' || a[i][j] == 'w') e[i][j] = 1;
		}
	}
	beg = Map(b);
	end = Map(e);
}







bool Can(int i, int dir)
{
	int xx, yy;
	xx = x[i] - dx[dir];
	yy = y[i] - dy[dir];
	if (a[xx][yy] == '#' || b[xx][yy] == 1) return false;
	xx = x[i] + dx[dir];
	yy = y[i] + dy[dir];
	if (a[xx][yy] == '#' || b[xx][yy] == 1) return false;
	return true;
}

void Move(int i, int dir)
{
	b[x[i]][y[i]] = 0;
	x[i] = x[i] + dx[dir];
	y[i] = y[i] + dy[dir];
	b[x[i]][y[i]] = 1;
}



void UnMap(int v)
{
	x[0] = v % 12 + 1;
	v /= 12;
	y[0] = v % 12 + 1;
	v /= 12;
	int d, j;
	int i;

	for (i = 1; i < nn; i++)
	{
		d = v % (4*i);
		v /= 4*i;
		j = d / 4;
		d = d % 4;
		x[i] = x[j] + dx[d];
		y[i] = y[j] + dy[d];
	}
}



//12 x 12 y 4 8 12 16





void Solve()
{

//	cerr << beg << " " << end << "\n";


	int be, en;
	be = 0; en = 0;	
	que[be] = beg;
	int i, j, k, l, cur, nxt;
	was[beg] = 1;
	while (be <= en)
	{
		cur = que[be++];
		if (cur == end) break;
		UnMap(cur);
		memset(b, 0, sizeof(b));
		for (i = 0; i < 5; i++)
			b[x[i]][y[i]] = 1;
		for (i = 0; i < 5; i++)
		{
			for (k = 0; k < 4; k++)
			{
				if (!Can(i, k)) continue;
				Move(i, k);
				if ((nxt = Map(b)) != -1)
				{
					if (was[nxt] == 0 || was[nxt] > 1 + was[cur])
					{
						was[nxt] = 1 + was[cur];
						que[++en] = nxt;
					}
				}
				else
				{
					for (j = 0; j < 5; j++)
					{
						for (l = 0; l < 4; l++)
						{
							if (!Can(j, l)) continue;
							Move(j, l);
							if ((nxt = Map(b)) != -1)
							{
								if (was[nxt] == 0  || was[nxt] > 2 + was[cur])
								{
									was[nxt] = 2 + was[cur];
									que[++en] = nxt;
								}
							}
							Move(j, 3-l);

						}
					}
				}
				Move(i, 3 - k);
			}

		}
		
	}
	cout << was[end] - 1 << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
