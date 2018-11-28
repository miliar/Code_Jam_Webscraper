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

const int MAXW = 12;
const int MAXSUM = 300;
const int MAXST = 200;
int W, Q;
int a[MAXW][MAXW];

const int di[4] = {0, 0, 1, -1};
const int dj[4] = {-1, 1, 0, 0};

void Load()
{
	cin >> W >> Q;
	int i, j;
	nextLine();
	for (i = 1; i <= W; i++)
	{
		for (j = 1; j <= W; j++)
		{
			a[i][j] = getchar();
		}
		nextLine();
	}
}

int sum;
//vector <int> res, curr;
//int cur;

//int sz;

inline string better(string a, string b)
{
	if (a.size() < b.size()) return a;
	if (b.size() < a.size()) return b;
	return min(a, b);
}

inline int isdigit(int c)
{
	return c >= '0' && c <= '9';
}
string dp[2][21][21][MAXSUM * 2 + 1];
string result[351];
int qr[350];

void MakeGo(int i, int j, int k, int s)
{
	int h, l, i1, j1;
	for (h = 0; h < 4; h++)
	{
		i1 = j + di[h];
		j1 = k + dj[h];
		
		if (i1 >= 1 && i1 <= W  && j1 >= 1 && j1 <= W
		&& (a[i1][j1] == '-' || a[i1][j1] == '+'))
		{
			for (l = 0; l < 4; l++)
			{
				if (i1 + di[l] >= 1 && i1 + di[l] <= W  && j1 + dj[l] >= 1 && j1 + dj[l] <= W
					&& isdigit(a[i1 + di[l]][j1 + dj[l]]))
				{
					if (a[i1][j1] == '-' && s - a[i1 + di[l]][j1 + dj[l]] + '0' >= 0)
					{
						dp[(i + 1) & 1][i1 + di[l]][j1 + dj[l]][s - a[i1 + di[l]][j1 + dj[l]] + '0'] =
						better(dp[(i + 1) & 1][i1 + di[l]][j1 + dj[l]][s - a[i1 + di[l]][j1 + dj[l]] + '0'],
						dp[i & 1][j][k][s] + '-' + (char)a[i1 + di[l]][j1 + dj[l]]);	
					}	
					else if (s + a[i1 + di[l]][j1 + dj[l]] - '0' <= MAXSUM * 2)
					{
					    dp[(i + 1) & 1][i1 + di[l]][j1 + dj[l]][s + a[i1 + di[l]][j1 + dj[l]] - '0'] =
						better(dp[(i + 1) & 1][i1 + di[l]][j1 + dj[l]][s + a[i1 + di[l]][j1 + dj[l]] - '0'],
						dp[i & 1][j][k][s] + '+' + (char)a[i1 + di[l]][j1 + dj[l]]);
					}
				}
		
			}	
		}
	}	
}

void check()
{
	int i, j, k, l;
	for (i = 1; i <= 50; i++)
	{
		result[i] = string(MAXST + 1, '9');
	}
	for (i = 1; i <= W; i++)
		for (j = 1; j <= W; j++)
			for (k = 0; k <= MAXSUM * 2; k++)
				dp[0][i][j][k] = dp[1][i][j][k] = string(MAXST + 1, '9');
	for (i = 1; i <= W; i++)	
	{
		for (j = 1; j <= W; j++)
		{
			if (isdigit(a[i][j]))
			{
				dp[0][i][j][MAXSUM + a[i][j]  - '0'] = (char)a[i][j];
			}
		}
	}
	for (i = 1; i <= Q; i++)
	{
		cin >> qr[i];
	}
	int s;
	for (i = 0; i <= MAXST; i++)
	{
		for (j = 1; j <= W; j++)
		{
			for (k = 1; k <= W; k++)
			{
				for (s = 0; s <= MAXSUM * 2; s++)
				{
					if (dp[i & 1][j][k][s].size() < MAXST + 1)	
					{
				
						if (s - MAXSUM >= 1 && s - MAXSUM <= 50)
						{
							result[s - MAXSUM] = better(result[s - MAXSUM], dp[i & 1][j][k][s]);
						}
					//	cerr << "Stay here " << dp[i & 1][j][k][s] << "\n";
						MakeGo(i, j, k, s);
					}
				}		
			}
		}
		for (j = 1; j <= Q; j++)
		{
			if (result[qr[j]].size() == MAXST + 1)
			{
				break;
			}
		}
		if (j == Q + 1) break;
	}
	for (i = 1; i <= Q; i++)
	{
		cout << result[qr[i]] << "\n";
	}
}

void Solve(int Test)
{
	int i, j, k;
	cerr << Test << "\n";
	cout << "Case #" << Test << ":\n";
	check();
}


#define file "c"
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