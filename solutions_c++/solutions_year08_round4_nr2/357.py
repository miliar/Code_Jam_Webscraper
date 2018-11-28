#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

bool b[100000001];
int a,mx,my;

void decom(int k, int& x, int& y)
{
	if (k == 0)
	{
		x = y = 0;
		return;
	}
	for (int i = 1; i <= mx; i++)
		if (k % i == 0 && k/i <= my)
		{
			x = i;
			y = k/i;
			return;
		}
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		cout << tind << endl;
		mset(b,0);
		fin >> mx >> my >> a;
		FI(i,0,mx+1)
			FI(j,0,my+1) b[i*j] = true;
		int up = mx*my-a;
		int i = 0;
		while (i <= up)
		{
			if (b[i] && b[i+a]) break;
			i++;
		}
		if (i > up)
			fout << "Case #" << tind << ": " << "IMPOSSIBLE" << endl;
		else
		{
			int x1 = -1,y1 = -1,x2 = -1,y2 = -1;
			decom(i, x1, y2);
			decom(i+a, x2, y1);
			fout << "Case #" << tind << ": 0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
		}

		int ans = 0;
	}
	return 0;
}
