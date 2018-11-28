#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int k;

int check(vector<char> a)
{
	int l = 0;
	int res = 0;
	for (int i = 1; i < a.size(); i++)
		if (a[i] != a[i - 1])
		{
			if (i - l >= k && a[l] == 'R')
				res |= 1;
			if (i - l >= k && a[l] == 'B')
				res |= 2;
			l = i;
		}
	if (a.size() - l >= k && a[l] == 'R')
		res |= 1;
	if (a.size() - l >= k && a[l] == 'B')
		res |= 2;
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int n;
		scanf("%d%d", &n, &k);
		char a[60][60];
		for (int i = 0; i < n; i++)
			scanf("%s", a[i]);
		for (int i = 0; i < n; i++)
		{
			int j = n - 1;
			for (int ii = n - 1; ii >= 0; ii--)
				if (a[i][ii] != '.')
					a[i][j--] = a[i][ii];
			for (int ii = j; ii >= 0; ii--)
				a[i][ii] = '.';
		}

		int total = 0;
		for (int i = 0; i < n; i++)
		{
			vector<char> v;
			for (int j = 0; j < n; j++)
				v.push_back(a[i][j]);
			total |= check(v);
		}
		for (int i = 0; i < n; i++)
		{
			vector<char> v;
			for (int j = 0; j < n; j++)
				v.push_back(a[j][i]);
			total |= check(v);
		}
		for (int i = 0; i < 2 * n - 1; i++)
		{
			vector<char> v;
			int j = 0;
			if (i - j >= n)
				j = i + 1 - n;
			while (j < n && i - j >= 0)
				v.push_back(a[j][i - j]), j++;
			total |= check(v);
		}
		for (int i = -n + 1; i < n; i++)
		{
			vector<char> v;
			int j = 0;
			if (i < 0)
				j = -i;
			while (j < n && i + j < n)
				v.push_back(a[j][i + j]), j++;
			total |= check(v);
		}

		string res;
		if (total == 0)
			res = "Neither";
		if (total == 1)
			res = "Red";
		if (total == 2)
			res = "Blue";
		if (total == 3)
			res = "Both";
		printf("Case #%d: %s\n", testCount + 1, res.c_str());
	}
	return 0;
}