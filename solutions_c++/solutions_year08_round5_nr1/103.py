#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>

using namespace std;

#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b
#define fr(i, n) for(i = 0; i < n; i++)
#define frd(i, n) for(i = n-1; i >= 0; i--)
#define lo(i, a, b) for(i = a; i < b; i++)
#define lod(i, a, b) for(i = a; i > b; i--)

#define pb push_back

#define Eps 1e-09
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("A.in", "r"), *outf = fopen("A.out", "w");

struct Line{
	int stand;
	int st, en;

	bool operator < (const Line &p) const{
		if(stand < p.stand)
			return true;
		if( stand == p.stand && st < p.st)
			return true;
		return false;
	};
};

vector <Line> X, Y;
vi mX, mY, MX, MY, cX, cY;

void make( int *a, int *b, int dir, int r)
{
	Line temp;
	int x[5] = {0, 1, 0, -1};
	int y[5] = {1, 0, -1, 0};
	
	if( dir == 0 || dir == 2)
	{
		temp.stand = *a;
		temp.st = *b;
		*b = *b + y[dir] * r;
		temp.en = *b;
		if(temp.st > temp.en)
			swap(temp.st, temp.en);
		X.pb(temp);
	}

	else
	{
		temp.stand = *b;
		temp.st = *a;
		*a = *a + x[dir] * r;
		temp.en = *a;
		if(temp.st > temp.en)
			swap(temp.st, temp.en);
		Y.pb(temp);
	}
}

void input()
{
	int i, j, k, l, r, M;
	char str[ 100];

	int x = 0, y = 0;
	int dir = 0, repeat = 0;

	X.clear(), Y.clear();
	mX.clear(), mY.clear(), MX.clear();
	MY.clear(), cX.clear(), cY.clear();

	fscanf(inf, "%d", &M);

	fr(i, M)
	{
		fscanf(inf, " %s%d", str, &r);
		l = strlen(str);

		fr(j, r)
		{
			fr(k, l)
			{
				if( str[k] == 'F')
					repeat++;

				else if( str[k] == 'L')
				{
					if( repeat != 0)
						make(&x, &y, dir, repeat);

					repeat = 0;
					dir = (dir + 3) % 4;
				}

				else
				{
					if( repeat != 0)
						make(&x, &y, dir, repeat);
					
					repeat = 0;
					dir = (dir + 1) % 4;
				}
			}
		}
	}

	if( repeat != 0)
		make(&x, &y, dir, repeat);

	sort(X.begin(), X.end());
	sort(Y.begin(), Y.end());

	fr(i, X.size())
	{
		if(X[i].stand == 0 && X[i].st == 0)
		{
			if(i != 0 && X[i-1].stand ==0 && X[i-1].en == 0)
			{
				X[i-1].en = X[i].en;
				break;
			}
		}
	}

	if(i != X.size())
	{
		for(; i < X.size() - 1; i++)
			X[i] = X[i+1];

		X.pop_back();
	}

	M = max( X.size(), Y.size());

	cY.reserve( M);
	cX.reserve( M);
	fr(i, M)
		cY.pb(0), mY.pb(0), MY.pb(0), cX.pb(0), mX.pb(0), MX.pb(0);

	fr(i, X.size())
	{
		fr(j, Y.size())
		{
			if(j < Y.size() - 1 && X[i].st <= Y[j].stand && Y[j+1].stand <= X[i].en)
			{
				if( cX[j] == 0)
					mX[j] = MX[j] = X[i].stand, cX[j] = 1;
				else
				{
					mX[j] = min(mX[j], X[i].stand);
					MX[j] = max(MX[j], X[i].stand);
				}
			}

			if(i < X.size() - 1 && Y[j].st <= X[i].stand && X[i+1].stand <= Y[j].en)
			{
				if( cY[i] == 0)
					mY[i] = MY[i] = Y[j].stand, cY[i] = 1;
				else
				{
					mY[i] = min(mY[i], Y[j].stand);
					MY[i] = max(MY[i], Y[j].stand);
				}
			}
		}
	}
}

int work()
{
	int i, j, res = 0;
	int M = max(X.size(), Y.size());

	fr(i, M)
		cX[i] = 0;

	fr(i, (X.size()-1))
	{
		fr(j, (Y.size()-1))
		{
			if(X[i].st <= Y[j].stand && Y[j+1].stand <= X[i].en)
				cX[j]++;
			if( cX[j] % 2 == 0)
			{
				if((mX[j] <= X[i].stand && X[i].stand < MX[j]) || (mY[i] <= Y[j].stand && Y[j].stand < MY[i]))
					res += (Y[j+1].stand - Y[j].stand) * (X[i+1].stand - X[i].stand);
			}
		}
	}

	return res;
}

void output(int x, int res)
{
	fprintf(outf, "Case #%d: %d\n", x, res);
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);

	fr(i, T)
	{
		input();
		output(i+1, work());
	}
	return 0;
}