//
// Round 1, Task A.
//


#define _USE_MATH_DEFINES	1

#include <iostream>
#include <iomanip>
#include <fstream>
#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>



void solve();

using namespace std;



int main()
{
	ifstream inf("in.txt");
	cin.rdbuf(inf.rdbuf());
	ofstream ouf("out.txt");
	cout.rdbuf(ouf.rdbuf());

	solve();

	return 0;
}


struct Point
{
	int x;
	int y;
};

void solve()
{
	int T;
	cin >> T;

	static Point p[100000];

	for (int t = 1; t <= T; ++t)
	{
		long long n, A, B, C, D, M, X, Y;

		cin >> n >> A >> B >> C >> D >> X >> Y >> M;
		p[0].x = X;
		p[0].y = Y;
		for (int i = 1; i < n; ++i)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			p[i].x = X;
			p[i].y = Y;
		}
		
		int rez = 0;
		for (int i = 0; i < n; ++i)
		for (int j = i + 1; j < n; ++j)
		for (int k = j + 1; k < n; ++k)
			if (!((p[i].x + p[j].x + p[k].x) % 3) && !((p[i].y + p[j].y + p[k].y) % 3))
				++rez;

		cout << "Case #" << t << ": " << rez << endl;
	}
}