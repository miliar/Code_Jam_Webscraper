#include <cstring>
#include <cstdio>
#include <string>
using namespace std;

#define MAXS 100011

typedef struct t_segment
{
	int x0, y0, x1, y1;
} segment;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

int ind = 0, area = 0;
segment S[MAXS];

void insertEdges(char *str, int &x0, int &y0, int &cd)
{
	int lastx = x0, lasty = y0;
	int cx = x0, cy = y0;
	int len = strlen(str);
	for (int i = 0; i < len; i++)
	{
		if (str[i] == 'F')
			cx += dx[cd], cy += dy[cd];
		if (str[i] != 'F' || i == len - 1)
		{
			if (lastx != cx || lasty != cy)
				S[ind].x0 = lastx, S[ind].y0 = lasty, S[ind].x1 = cx, S[ind++].y1 = cy;
			lastx = cx, lasty = cy;
			if (str[i] == 'L')
				cd = (cd + 4 - 1) % 4;
			else
				cd = (cd + 1) % 4;
		}
	}
	x0 = lastx, y0 = lasty;
}

int inPoly(double x, double y)
{
	int nr = 0;
	for (int i = 0; i < ind; i++)
	{
		int x0 = S[i].x0, y0 = S[i].y0, x1 = S[i].x1, y1 = S[i].y1;

		if (x0 == x1 && y0 < y && y1 > y && x0 < x)
			nr++;
	}

	return nr % 2;
}

void solve()
{
	area = 0;

	for (int i = -100; i < 100; i++)
		for (int j = -100; j < 100; j++)
		{
			if (i == 2 && j == 2)
				i++, i--;
			double x = i + 0.5, y = j + 0.5;
			if (!inPoly(x, y))
			{
				int east = 0, west = 0, north = 0, south = 0;
				for (int k = 0; k < ind; k++)
				{
					if (S[k].x0 == S[k].x1 && S[k].y0 < y && S[k].y1 > y)
					{
						if (S[k].x0 < x)
							east = 1;
						else
							west = 1;
					}
					if (S[k].y0 == S[k].y1 && S[k].x0 < x && S[k].x1 > x)
					{
						if (S[k].y0 < y)
							south = 1;
						else
							north = 1;
					}
				}
				if ((east && west) || (north && south))
					area++;
			}
		}
}

void readAndSolve()
{
	int N;

	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
	{
		int l;
		scanf("%d", &l);

		int cd = 1;
		int x = 0, y = 0;
		ind = 0;
		string path = "";
		for (int p = 0; p < l; p++)
		{
			char str[64];
			int nr;
			scanf("%s %d", str, &nr);
			for (; nr > 0; nr--)
				path += str;
		}
		insertEdges((char *) path.c_str(), x, y, cd);
		for (int i = 0; i < ind; i++)
		{
			if (S[i].x0 == S[i].x1)
			{
				if (S[i].y0 > S[i].y1)
					swap(S[i].y0, S[i].y1);
			}
			else
				if (S[i].x0 > S[i].x1)
					swap(S[i].x0, S[i].x1);
		}
		solve();
		printf("Case #%d: %d\n", i, area);
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	readAndSolve();

	return 0;
}