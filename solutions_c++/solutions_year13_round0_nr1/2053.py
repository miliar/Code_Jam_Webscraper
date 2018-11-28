#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

char f[4][7];

bool test(int i, int j, char c)
{
	return f[i][j] == c || f[i][j] == 'T';
}

bool est(char c)
{
	bool h[4] = {true, true, true, true}, v[4] = {true, true, true, true}, d[2] = {true, true};

	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			h[i] = h[i] && test(i, j, c);
			v[j] = v[j] && test(i, j, c);
		}
		d[0] = d[0] && test(i, i, c);
		d[1] = d[1] && test(i, 3-i, c);
	}

	for (int i=0;i<4;++i)
	{
		if (h[i] || v[i])
			return true;
	}

	if (d[0] || d[1])
		return true;

	return false;
}

void solve()
{
	bool wo = est('O');
	bool wx = est('X');
	bool dot = false;

	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			if (f[i][j] == '.')
				dot = true;
		}
	}

	if (wo)
	{
		cout << "O won";
	}
	else if (wx)
	{
		cout << "X won";
	}
	else if (dot)
	{
		cout << "Game has not completed";
	}
	else
	{
		cout << "Draw";
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;

	cin >> t;

	char tmp[3];

	cin.getline(tmp, 3);

	for (int i = 0;i<t;++i)
	{
		for (int j=0;j<4;++j)
		{
			cin.getline(f[j], 7);
		}

		cin.getline(tmp, 3);

		cout << "Case #" << i + 1 << ": ";

		solve();

		cout << endl;
	}

	return 0;
}