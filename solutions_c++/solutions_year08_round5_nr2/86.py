#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;



int n, m;
int a[20][20];
int bx, by;
int ex, ey;

int nxtx[20][20][4];
int nxty[20][20][4];

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {-1, 0, 1, 0};

void Load()
{
	cin >> n >> m;
	int i, j, k;
	char c;
	for (i = 0; i < 20; i++)
	{
		a[i][0] = a[i][m+1] = a[0][i] = a[n+1][i] = 1;
	}
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= m; j++)
		{
			c = getchar();
			while (c != '.' && c != '#' && c != 'X' && c != 'O')
				c = getchar();
			if (c == 'O')
			{
				bx = i;
				by = j;
				c = '.';
			}
			if (c == 'X')
			{
				ex = i;
				ey = j;
				c = '.';
			}
			if (c != '.') 
				a[i][j] = 1;
			else
				a[i][j] = 0;
		}
	}

	int ci, cj;

	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= m; j++)
		{
		    if (a[i][j] != 0) continue;
		    for (k = 0; k < 4; k++)
		    {
			    ci = i; cj = j;
           		while (a[ci][cj] == 0)
           		{
           			ci += dx[k];
           			cj += dy[k];
           		}
           		ci -= dx[k];
           		cj -= dy[k];
           		nxtx[i][j][k] = ci;
           		nxty[i][j][k] = cj;
           	}
		}
	}
}


const unsigned char MNOGO = 255;

unsigned char dp[16][16][16][16][4][16][16][4];


class State
{
public:
	short int x, y, px, py, qx, qy, pd, qd;
};

State que[100000][2];
int hd[2], tl[2];




	


void Solve()
{

	memset(dp, 255, sizeof(dp));

	unsigned char res = MNOGO;
	int cur;
	int i, j, k;

	State s, s2;
	s.x = bx;
	s.y = by;
	s.px = s.qx = s.py = s.qy = s.pd = s.qd = 0;
	cur = 0;
	hd[0] = 0; tl[0] = 0;
	hd[1] = 0; tl[1] = -1;
	que[0][0] = s;

	dp[s.x][s.y][s.px][s.py][s.pd][s.qx][s.qy][s.qd] = 0;

	while (hd[cur] <= tl[cur])
	{




		s = que[hd[cur]][cur];
//		cerr << cur << " " << hd[cur] <<" " <<s.x << " " << s.y << " " << s.px << " " << s.py << " " << s.pd << " " << s.qx << " " << s.qy << " " << s.qd << " : " << (int)dp[s.x][s.y][s.px][s.py][s.pd][s.qx][s.qy][s.qd] << "\n";
		if (s.x == ex && s.y == ey)
		{
		    res = dp[s.x][s.y][s.px][s.py][s.pd][s.qx][s.qy][s.qd];
		 	break;
		}
		hd[cur]++;

		for (k = 0; k < 4; k++)
		{
			i = nxtx[s.x][s.y][k];	
			j = nxty[s.x][s.y][k];
			if (i == s.qx && j == s.qy && k == s.qd) continue;
			s2 = s;
			s2.px = i; s2.py = j; s2.pd = k;
			if (dp[s2.x][s2.y][s2.px][s2.py][s2.pd][s2.qx][s2.qy][s2.qd] == MNOGO)
			{
				dp[s2.x][s2.y][s2.px][s2.py][s2.pd][s2.qx][s2.qy][s2.qd] = dp[s.x][s.y][s.px][s.py][s.pd][s.qx][s.qy][s.qd];
				tl[cur]++;
				que[tl[cur]][cur] = s2;
			}
		}
	
		for (k = 0; k < 4; k++)
		{
			i = nxtx[s.x][s.y][k];	
			j = nxty[s.x][s.y][k];
			if (i == s.px && j == s.py && k == s.pd) continue;
			s2 = s;
			s2.qx = i; s2.qy = j; s2.qd = k;
			if (dp[s2.x][s2.y][s2.px][s2.py][s2.pd][s2.qx][s2.qy][s2.qd] == MNOGO)
			{
				dp[s2.x][s2.y][s2.px][s2.py][s2.pd][s2.qx][s2.qy][s2.qd] = dp[s.x][s.y][s.px][s.py][s.pd][s.qx][s.qy][s.qd];
				tl[cur]++;
				que[tl[cur]][cur] = s2;
			}

		}

		for (k = 0; k < 4; k++)
		{
			if (s.x == s.px && s.y == s.py && k == s.pd)
			{
				i = s.qx; j = s.qy;
			}
			else if (s.x == s.qx && s.y == s.qy && k == s.qd)
			{
				i = s.px; j = s.py;
			}
			else
			{
				i = s.x + dx[k]; j = s.y + dy[k];
			}
			if (a[i][j] == 1) continue;

			s2 = s;
			s2.x = i; s2.y = j;

			if (dp[s2.x][s2.y][s2.px][s2.py][s2.pd][s2.qx][s2.qy][s2.qd] == MNOGO)
			{
				dp[s2.x][s2.y][s2.px][s2.py][s2.pd][s2.qx][s2.qy][s2.qd] = dp[s.x][s.y][s.px][s.py][s.pd][s.qx][s.qy][s.qd] + 1;
				tl[1-cur]++;
				que[tl[1-cur]][1-cur] = s2;
			}

		}


		if (tl[cur] < hd[cur])
		{
		 	hd[cur] = 0;
		 	tl[cur] = -1;
		 	cur = 1 - cur;

		}

	}



	if (res == MNOGO)
	{
		cout << "THE CAKE IS A LIE";
	}
	else cout << (int)res;

}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int nt, tt;

	cin >> nt;

	for (tt = 1; tt <= nt; tt++)
	{
    	Load();
    	cout << "Case #" << tt << ": ";
    	Solve();
    	cerr << tt << "\n";
    	cout << "\n";
    }
	return 0;
}