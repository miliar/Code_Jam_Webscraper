#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <complex>
#include <string>
#include <cmath>
#include <deque>
#include <map>
#include <cstdlib>
#include <locale>
#include <limits>
#include <complex>
#include <sstream>
#include <utility>
//#include <list>

#define pb push_back
#define Size(x) ((int)(x.size()))
//#define X real()
//#define Y imag()

using namespace std;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int lint;
//typedef unsigned long long lint;

string res[4] = {
	"X won",
	"O won",
	"Draw",
	"Game has not completed"
};

int status(int x, int o, bool t) // 0 x   1  o   -1 
{
	if (x >= 3)
	{
		if (x == 4 || t)
			return 0;
	}
	else if (o >= 3)
		if (o == 4 || t)
			return 1;
	return -1;
}

void pl(const int &z, int &x, int &o, bool &t)
{
	if (z == 'X')
		x ++;
	else if (z == 'O')
		o ++;
	else if (z == 'T')
		t = true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	stdin = freopen("A.in", "r", stdin);
	stdout = freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for (int q = 0; q < T; q++)
	{
		bool pr = false;
		cout << "Case #" << q + 1 << ": ";
		string a[4];
		for (int i = 0; i < 4; i++)
			cin >> a[i];
		int ans = -1;
		bool isfull = true;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a[i][j] == '.')
					isfull = false;
		for (int i = 0; i < 4; i++)
		{
			int x = 0, o = 0;
			bool t = false;
			for (int j = 0; j < 4; j++)
				pl(a[i][j], x, o, t);
			ans = status(x, o, t);
			if (ans > -1)
			{
				cout << res[ans] << endl;
				pr = true;
				break;
			}
		}
		for (int j = 0; j < 4; j++)
		{
			int x = 0, o = 0;
			bool t = false;
			for (int i = 0; i < 4; i++)
				pl(a[i][j], x, o, t);
			ans = status(x, o, t);
			if (ans > -1 && !pr)
			{
				cout << res[ans] << endl;
				pr = true;
				break;
			}
		}
		int x = 0, o = 0;
		bool t = false;
		for (int i = 0; i < 4; i++)
			pl(a[i][i], x, o, t);
		ans = status(x, o, t);
		if (ans > -1 && !pr)
		{
			cout << res[ans] << endl;
			pr = true;
			continue;
		}
		x = 0, o = 0, t = false;
		for (int i = 0; i < 4; i++)
			pl(a[i][4 - i - 1], x, o, t);
		ans = status(x, o, t);
		if (ans > -1 && !pr)
		{
			cout << res[ans] << endl;
			pr = true;
			continue;
		}
		if (!pr)
		{
			if (isfull)
				cout << res[2] << endl;
			else
				cout << res[3] << endl;
		}
		/*
			X won
			Draw
			Game has not completed
			O won
		*/
	}
	return 0;
}
