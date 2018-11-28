#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
using namespace std;


#define file "a"
char a[130][130];
int b[830][830];
int k;

void Load()
{
	cin >> k;
	int i, j, t;
	nextLine();
	for (i = 0; i < 2 * k - 1; i++)
		for (j = 0; j < 2 * k - 1; j++)
			a[i][j] = ' ';
	for (i = 0; i < 2 * k - 1; i++)
	{
		for (j = 0; j < abs(k - i - 1); j++) a[i][j] = getchar();
		t = k - abs(k - i - 1);
		for (j = abs(k - i - 1); t > 0; t --, j++)
		{
			cin >> a[i][j];
			j++;
			a[i][j] = ' ';

		}
		nextLine();
	}
}

bool Check(int x, int y, int c, int &cur)
{
	if (c == ' ') return true;
	if (b[x + 250][y + 250] == -1)
	{
		b[x + 250][y + 250] = c;
//		cerr << "marked "<< x << " " << y << " as " << (char)c << "\n";
		cur++;
		return true;
	}
	else if (b[x + 250][y + 250] == c) return true;
	else return false;
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	cerr << "ok";
	int x0, y0, i, j;
	int cur, res;
	bool f = true;
	int all = 0;
	res = INF;

	for (i = 0; i < 2 * k - 1; i++)
	{
		for (j = 0; j < 2 * k - 1; j++)
		{
			if (a[i][j] != ' ') all++;
		}
	}
	int nk;
	for (x0 = 0; x0 <= 2 * k - 1; x0++)
	{
		for (y0 = 0; y0 <= 2 * k - 1; y0++)
		{
			x0 *= -1, y0 *= -1;
			for (i = 250 - 4 * k; i <= 250 + 4 * k; i++)
			for (j = 250 - 4 * k; j <= 250 + 4 * k; j++)
				b[i][j] = -1;
	//	memset(b, 0xFF, sizeof(b));

			cur = 0;
			f = true;
			for (i = 0; f && i < 2 * k - 1; i++)
			{
				for (j = 0; f && j < 2 * k - 1; j++)
				{
					if (!Check(x0 + i, y0 + j, a[i][j], cur)) f = false;
					if (!Check(-x0 - i, y0 + j, a[i][j], cur)) f = false;
					if (!Check(-x0 - i, -y0 - j, a[i][j], cur)) f = false;
					if (!Check(x0 + i, -y0 - j, a[i][j], cur)) f = false;	
				}
			}
			if (f)
			{
				nk = 0;
				for (i = 0; i < 2 * k - 1; i++)
				{
					for (j = 0; j < 2 * k - 1; j++)
					{
						if (b[x0 + i + 250][y0 + j + 250] != -1)
						{
							nk = max(abs(x0 + i + y0 + j), nk);
							nk = max(abs(-x0-i + y0 + j), nk);
						}
					}
				}
				nk++;
				int t;
				for (i = 0; i < nk; i++)
				{
					for (j = nk - i - 1, t = 0; t < (i + 1); t++, j += 2)
					{
						if (b[i - nk + 1 + 250][j - nk + 1 + 250] == -1)
						{
							cur++;
						}
					}
				}
				for (i = nk; i < 2 * nk - 1; i++)
				{
					for (j = i - nk + 1, t = 0; t < nk - (i - nk + 1); t++, j += 2)
					{
						if (b[i - nk + 1 + 250][j - nk + 1 + 250] == -1)
						{
							cur++;
						}
					}
				}
			}
			x0 *= -1, y0 *= -1;
			
			if (f)
			{
//				cerr << x0 << " " << y0 << " " << (int)f << " " << cur - all << "\n";
				res = min(res, cur - all);
			}
		}
	}
	cerr << Test << "\n";
	cout << res << "\n";
//	cerr << "\n";
}


int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}