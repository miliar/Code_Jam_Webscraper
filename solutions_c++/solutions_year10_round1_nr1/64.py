#include <iostream>
#include <cstdio>
#include <vector>

const int N = 50;

using namespace std;

int t, n, r, ans;
string T[N];
string text;


bool same(int x, int y, int a, int b)
{
	int i;
	for(i = 0; i < r; ++i)
		if(T[x + a * i][y + b * i] != T[x][y])
			return false;
	return true;
}
bool any(int x, int y)
{
	bool res = false;
	if(x <= n - r)
		res |= same(x, y, 1, 0);
	if(y <= n - r)
		res |= same(x, y, 0, 1);
	if(x <= n - r && y <= n - r)
		res |= same(x, y, 1, 1);
	if(x >= r - 1 && y <= n - r)
		res |= same(x, y, -1, 1);
	return res;
}

int check(int x, int y)
{
	if(T[x][y] == '.')
		return 0;
	if(T[x][y] == 'R' && any(x, y))
		return 1;
	if(T[x][y] == 'B' && any(x, y))
		return 2;
}

int main()
{
	int i, j, k;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		ans = 0;
		cin >> n >> r;
		for(i = 0; i < n; ++i)
			cin >> T[i];
		for(i = 0 ; i < n; ++i)
			for(j = k = n - 1; j >= 0; --j)
				if(T[i][j] != '.')
					swap(T[i][j], T[i][k--]);
		for(i = 0; i < n; ++i)
			for(j = 0; j < n; ++j)
				ans |= check(i, j);
		if(ans == 3)
			text = "Both";
		else if(ans == 2)
			text = "Blue";
		else if(ans == 1)
			text = "Red";
		else
			text = "Neither";
		cout << "Case #" << testCase << ": " << text << endl;
	}
}
