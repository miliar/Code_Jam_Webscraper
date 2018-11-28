// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <queue>

using namespace std;

ifstream in("B.in");
ofstream out("B.out");

struct Point
{
	int x, y;
	Point()
	{
		x = y = 0;
	}
	Point(int _x, int _y)
	{
		x = _x;
		y = _y;
	}
};

int T, H, W;

int M[110][110];
int P[110][110];

bool flowTo(const Point &p1, const Point &p2)
{
	int min = M[p1.y][p1.x];
	Point mp;
	if (p1.y > 0 && M[p1.y - 1][p1.x] < min)
	{
		mp.x = p1.x;
		mp.y = p1.y - 1;
		min = M[p1.y - 1][p1.x];
	}
	if (p1.x > 0 && M[p1.y][p1.x - 1] < min)
	{
		mp.x = p1.x - 1;
		mp.y = p1.y;
		min = M[p1.y][p1.x - 1];
	}
	if (p1.x < W-1 && M[p1.y][p1.x + 1] < min)
	{
		mp.x = p1.x + 1;
		mp.y = p1.y;
		min = M[p1.y][p1.x + 1];
	}
	if (p1.y < H-1 && M[p1.y + 1][p1.x] < min)
	{
		mp.x = p1.x;
		mp.y = p1.y + 1;
		min = M[p1.y + 1][p1.x];
	}
	return mp.x == p2.x && mp.y == p2.y;
}

int main()
{
	in >> T;
	for (int t = 0; t < T; ++t)
	{
		in >> H >> W;
		for (int y = 0; y < H; ++y)
		{
			for (int x = 0; x < W; ++x)
			{
				in >> M[y][x];
			}
		}
		memset(P, 0, sizeof(P));
		vector<Point> sinks;

		for (int y = 0; y < H; ++y)
		{
			for (int x = 0; x < W; ++x)
			{
				bool b = true;
				if (y > 0 && M[y-1][x] < M[y][x])
					b = false;
				if (y < H-1 && M[y+1][x] < M[y][x])
					b = false;
				if (x > 0 && M[y][x-1] < M[y][x])
					b = false;
				if (x < W-1 && M[y][x+1] < M[y][x])
					b = false;
				if (b)
				{
					sinks.push_back(Point(x, y));
				}
			}
		}

		for (int i = 0; i < sinks.size(); ++i)
		{
			queue<Point> Q;
			Q.push(sinks[i]);
			int color = i + 1;
			P[sinks[i].y][sinks[i].x] = color;
			while(!Q.empty())
			{
				Point p = Q.front();
				Q.pop();
				Point pp = Point(p.x-1, p.y);
				if (p.x > 0 && P[p.y][p.x - 1] == 0 && flowTo(pp, p))
				{
					P[p.y][p.x - 1] = color;
					Q.push(pp);
				}
				pp = Point(p.x+1, p.y);
				if (p.x < W-1 && P[p.y][p.x + 1] == 0 && flowTo(pp, p))
				{
					P[p.y][p.x + 1] = color;
					Q.push(pp);
				}
				pp = Point(p.x, p.y-1);
				if (p.y >0 && P[p.y-1][p.x] == 0 && flowTo(pp, p))
				{
					P[p.y-1][p.x] = color;
					Q.push(pp);
				}
				pp = Point(p.x, p.y+1);
				if (p.y < H-1 && P[p.y+1][p.x] == 0 && flowTo(pp, p))
				{
					P[p.y+1][p.x] = color;
					Q.push(pp);
				}
			}
		}

		out << "Case #" << t+1 << ":\n";
		char ch = 'a';
		vector <char> let;
		let.resize(27);
		for (int y = 0; y < H; ++y)
		{
			for (int x = 0; x < W; ++x)
			{
				if (let[P[y][x]] == '\0')
				{
					let[P[y][x]] = ch;
					++ch;
				}
				out << let[P[y][x]] << " ";
			}
			out << "\n";
		}
	}
	return 0;
}

