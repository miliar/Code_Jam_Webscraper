#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

typedef vector<int> VI;

typedef long long lint;

struct Point
{
	lint x;
	lint y;
	Point(int x_, int y_): x(x_), y(y_) {}
};

Point operator - (Point a, Point b)
{
	return Point(b.x - a.x, b.y - a.y);
}



lint operator * (Point a, Point b)
{
	return a.x * b.y - a.y * b.x;
}

bool OnSegment(Point p1, Point p2, Point px)
{
	lint lx = min(p1.x, p2.x);
	lint rx = max(p1.x, p2.x);

	lint ly = min(p1.y, p2.y);
	lint hy = max(p1.y, p2.y);

	lint x = px.x;
	lint y = px.y;

	return x >= lx && x <= rx && y >= ly && y <= hy;
}

bool SegIntersect(Point p1, Point p2, Point p3, Point p4)
{
	lint d1 = (p3 - p1) * (p2 - p1);
	lint d2 = (p4 - p1) * (p2 - p1);
	lint d3 = (p1 - p4) * (p3 - p4);
	lint d4 = (p2 - p4) * (p3 - p4);

	bool dif1 = (d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0);
	bool dif2 = (d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0);
	
	if(dif1 && dif2)
		return true;
	
	if(d1 == 0 && OnSegment(p1, p2, p3))
		return true;

	if(d2 == 0 && OnSegment(p1, p2, p4))
		return true;

	if(d3 == 0 && OnSegment(p3, p4, p1))
		return true;

	if(d4 == 0 && OnSegment(p3, p4, p2))
		return true;

	return false;
}

bool Intersect(const VI & a, const VI & b)
{
	int l = a.size();
	for(int i = 0; i < l - 1; i++)
	{
		Point p1(i, a[i]);
		Point p2(i + 1, a[i + 1]);
		
		for(int k = max(0, i - 1); k <= min(i + 1, l - 2); k++)
		{
			Point p3(k, b[k]);
			Point p4(k + 1, b[k + 1]);
			if(SegIntersect(p1, p2, p3, p4))
				return true;
		}
	}
	return false;
}

int GetBit(int mask, int pos)
{
	return (mask & (1 << pos)) != 0;
}

vector<int> solve;

const int MAX_N = 16;

vector<int> ok;
vector<int> bits[1 << MAX_N];
vector<int> masks[1 << MAX_N];

int Go(int mask)
{
	if(solve[mask] != -1)
		return solve[mask];
	int m = bits[mask].size();
	solve[mask] = 1 << 25;/*
	for(int i = 0; i < (1 << m); i++)
	{
		int nextMask = 0;
		for(int j = 0; j < m; j++)
			if(GetBit(i, j))
				nextMask |= (1 << bits[mask][j]);
		if(ok[nextMask])
			solve[mask] = min(solve[mask], 1 + Go(mask ^ nextMask));
	}*/
	for(int i = 0; i < masks[mask].size(); i++)
	{
		int nextMask = masks[mask][i];
		if(ok[nextMask])
			solve[mask] = min(solve[mask], 1 + Go(mask ^ nextMask));
	}
	return solve[mask];
}

int Solve(const vector<VI> & data)
{
	int n = data.size();
	vector<VI> adj(n, vector<int>(n, 0));

	for(int i = 0; i < n; i++)
		adj[i][i] = 1;

	for(int i = 0; i < n; i++)
		for(int j = i + 1; j < n; j++)
			adj[i][j] = adj[j][i] = Intersect(data[i], data[j]);
	
	ok.assign(1 << n, 1);

	for(int i = 0; i < (1 << n); i++)
		for(int j = 0; j < n; j++)
			for(int k = j + 1; k < n; k++)
				if(GetBit(i, j) && GetBit(i, k) && adj[j][k])
					ok[i] = false;
	
	solve.assign(1 << n, -1);
	for(int i = 0; i < n; i++)
		solve[1 << i] = 1;
	solve[0] = 0;
	int res = Go((1 << n) - 1);
	return res;
}

int main()
{
	ifstream in("in.txt");
	int tests, n, k;
	in >> tests;
	vector<VI> data;
	for(int i = 0; i < (1 << MAX_N); i++)
		for(int j = 0; j < MAX_N; j++)
			if(GetBit(i, j))
				bits[i].push_back(j);
	for(int mask = 0; mask < (1 << MAX_N); mask++)
	{
		int m = bits[mask].size();
		for(int i = 0; i < (1 << m); i++)
		{
			int nextMask = 0;
			for(int j = 0; j < m; j++)
				if(GetBit(i, j))
					nextMask |= (1 << bits[mask][j]);
			masks[mask].push_back(nextMask);
		}
	}
	for(int t = 1; t <= tests; t++)
	{
		in >> n >> k;
		data.assign(n, vector<int>(k));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < k; j++)
				in >> data[i][j];
		cout << "Case #" << t << ": " << Solve(data) << endl;
	}
	return 0;
}