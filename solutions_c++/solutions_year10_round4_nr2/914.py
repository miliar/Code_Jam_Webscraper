#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const int N = 110;

int n;
int mtx[N][N];
int tmp[N][N];

void myin ()
{
	int i, j, k;
	cin >> n;
	for (i = 1; i <= n; i++)
	{
		for (j = i, k = 1; j >= 1; j--, k++)
			cin >> mtx[j][k];
	}
	for (i = 2; i <= n; i++)
	{
		for (j = n, k = i; j >= i; j--, k++)
			cin >> mtx[j][k];
	}
	/*for (i = 1; i <= n; i++, cout << endl)
		for (j = 1; j <= n; j++)
			cout << mtx[i][j] << " ";*/
}

int ss[N];
int sn;

bool cc (int lv)
{
	int l, r;
	/*if (sn & 1)
	{
		l = r = sn / 2 + 1;
		if (l <= 0 || r > sn)
				return true;
		while (ss[l] == ss[r])
		{
			l--, r++;
			if (l <= 0 || r > sn)
				return true;
		}
	}
	else
	{
		l = sn / 2;
		r = sn / 2 + 1;
		if (l <= 0 || r > sn)
				return true;
		while (ss[l] == ss[r])
		{
			l--, r++;
			if (l <= 0 || r > sn)
				return true;
		}
	}*/
	if ((sn + lv) & 1)
	{
		l = r = (sn + lv)/ 2 + 1;
		if (l <= 0 || r > sn)
				return true;
		while (ss[l] == ss[r])
		{
			l--, r++;
			if (l <= 0 || r > sn)
				return true;
		}
	}
	else
	{
		l = (sn + lv) / 2;
		r = (sn + lv) / 2 + 1;
		if (l <= 0 || r > sn)
				return true;
		while (ss[l] == ss[r])
		{
			l--, r++;
			if (l <= 0 || r > sn)
				return true;
		}
	}
	return false;
}

int check1 (int lv)
{
	int i, j, k;
	for (i = 1; i <= n; i++)
	{
		sn = 0;
		for (j = i, k = 1; j >= 1; j--, k++)
			ss[++sn] = mtx[j][k];
		if (!cc (lv) && !cc(-lv))
			return 0;
	}
	for (i = 2; i <= n; i++)
	{
		sn = 0;
		for (j = n, k = i; j >= i; j--, k++)
			ss[++sn] = mtx[j][k];
		if (!cc (lv) && !cc(-lv))
			return 0;
	}
	return 1;
}

int check2 (int lv)
{
	int i, j, k;
	for (i = 1; i <= n; i++)
	{
		sn = 0;
		for (j = i, k = 1; j <= n; j++, k++)
			ss[++sn] = mtx[k][j];
		if (!cc (lv) && !cc(-lv))
			return 0;
	}
	for (i = 2; i <= n; i++)
	{
		sn = 0;
		for (j = i, k = 1; j <= n; j++, k++)
			ss[++sn] = mtx[j][k];
		if (!cc (lv) && !cc(-lv))
			return 0;
	}
	return 1;
}

/*void chg1 ()
{
	int i, j;
	for (i = 1; i <= n; i++)
		for (j = 1; j < i; j++)
			swap (mtx[i][j], mtx[j][i]);
}

void chg2 ()
{
	int i, j;
	for (i = 1; i <= n; i++)
		for (j = 1; j < n - i + 1; j++)
			swap (mtx[i][j], mtx[n - j + 1][n - i + 1]);
}

int check1 (int lv)
{
	int t1 = check (lv);
	chg1 ();
	int t2 = check (lv);
	return t1 || t2;
}

int check2 (int lv)
{
	chg2 ();
	int t1 = 
}*/

/*int chg1 ()
{
	int i, j, k, l;
	for (i = 1; i <= n; i++)
	{
		sn = 0;
		for (j = i, k = 1; j >= 1 && k <= i / 2; j--, k++)
			swap (mtx[j][k], mtx[i - j + 1][i - k + 1]);
	}
	for (i = 2; i <= n; i++)
	{
		sn = 0;
		for (j = n, k = i; j >= i; j--, k++)
			swap (mtx[j][k], mtx[][]);
	}
}*/

void work ()
{
	int i;
	int lab1 = 0;
	int lab2 = 0;
	for (i = 0; ; i++)
	{
		//memcpy (tmp, mtx, sizeof (mtx));
		lab1 |= check1 (i);
		lab2 |= check2 (i);
		//memcpy (mtx, tmp, sizeof (mtx));
		if (lab1 && lab2)
			break;
	}
	i += n;
	cout << i * i - n * n << endl;
}

int main ()
{
	int i, tests;
	freopen ("t1.in", "r", stdin);
	freopen ("tt.out", "w", stdout);
	cin >> tests;
	for (i = 1; i <= tests; i++)
	{
		myin ();
		cout << "Case #" << i <<": ";
		work ();
	}
return 0;
}