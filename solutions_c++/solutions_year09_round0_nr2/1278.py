#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-9; 
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

#define Check assert

const int dx[] = {0, -1, 1, 0};
const int dy[] = {-1, 0, 0, 1};

template<class T> class cvector2
{
	vector<T> d;
	void chk(int x, int y) const
	{
		Check(x >= 0 && x < W && y >= 0 && y < H && "out of range");
	}
	int index(int x, int y) const
	{
		return x * H + y;
	}
public:
	int W, H;

	cvector2(int W, int H, const T& val = T()) : W(W), H(H)
	{
		Check(W >= 0 && H >= 0);
		d.resize(W * H, val);
	}
	void operator = (const cvector2<T>& r)		{ W = r.W; H = r.H; d = r.d; }
	void fill(const T& val = T())				{ d.clear(); d.resize(W * H, val); }
	T& operator () (int x, int y)				{ chk(x, y); return d[index(x, y)]; }
	const T& operator () (int x, int y) const	{ chk(x, y); return d[index(x, y)]; }
	bool Inside(int x, int y)					{ return x >= 0 && x < W && y >= 0 && y < H; }
};

cvector2<int> basin(1, 1);
cvector2<int> mapp(1, 1);
int basin_id = 0;

int Dfs(int x, int y)
{
	if (basin(x, y) == -1)
	{
		int min_v = mapp(x, y);
		int min_dir = -1;
		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (!mapp.Inside(nx, ny))
			{
				continue;
			}
			int v = mapp(nx, ny);
			if (v < min_v)
			{
				min_v = v;
				min_dir = i;
			}
		}
		if (min_dir != -1)
		{
			basin(x, y) = Dfs(x + dx[min_dir], y + dy[min_dir]);
		}
		else	
		{
			basin(x, y) = basin_id++;
		}
	}
	return basin(x, y);
}
void Go()
{
	int h, w;
	cin >> h >> w;
	mapp = cvector2<int>(w, h);
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			cin >> mapp(j, i);
		}
	}
	basin = cvector2<int>(w, h, -1);
	basin_id = 0;
	for (int i = 0; i < w; i++)
	{
		for (int j = 0; j < h; j++)
		{
			Dfs(i, j);
		}
	}
	string res;
	map<int, char> code;
	char last_code = 'a';
	for (int y = 0; y < h; y++)
	{
		for (int x = 0; x < w; x++)
		{
			int id = basin(x, y);
			char& c = code[id];
			if (c == 0)
			{
				c = last_code;
				last_code++;
			}
			if (x != 0)
			{
				cout << ' ';
			}
			cout << c;
		}
		cout << '\n';
	}
}
void main()
{
#ifndef _DEBUG
	const string file_name = "B-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int nn;
	cin >> nn;
	for (int jj = 1; jj <= nn; jj++)
	{	
		cout << "Case #" << jj << ": " << '\n';
		Go();
	}
}
