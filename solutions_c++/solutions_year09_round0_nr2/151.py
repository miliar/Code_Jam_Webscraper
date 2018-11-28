#include <iostream>
#include <limits>
#include <complex>
#include <map>
#include <vector>

using namespace std;

const int inf = numeric_limits<int>::max();
const char nobasin = '\255';
typedef complex<int> point;

struct neighbour
{
	int alt;
	point p;

	neighbour() {}
	neighbour(int nalt, const point &np) : alt(nalt), p(np) {}

	bool operator<(const neighbour &r) const { return alt < r.alt; }
};

point d[] = {
	point(0,-1),
	point(-1,0),
	point(1,0),
	point(0,1) };

int basintag, labeltag;
int board[102][102];
char basin[102][102];
map<char, char> labels;

char getLabel(char idx)
{
	if (labels.count(idx) == 0)
		return labels[idx] = labeltag++;

	return labels[idx];
}

int& atboard(const point &p) { return board[p.real()][p.imag()]; }
char& atbasin(const point &p) { return basin[p.real()][p.imag()]; }

void flood(point p)
{
	if (atbasin(p) != nobasin) return;

	vector<neighbour> ns;
	for (int c = 0; c < 4; ++c)
	{
		point np = p + d[c];
		ns.push_back( neighbour( atboard(np), np) );
	}

	neighbour lowest = ns.front();
	for (int c = 1; c < ns.size(); ++c)
		if (ns[c] < lowest) lowest = ns[c];

	if (lowest.alt >= atboard(p))
		atbasin(p) = 'A' + basintag++;
	else
	{
		flood(lowest.p);
		atbasin(p) = atbasin(lowest.p);
	}
}


int main()
{
	int tc;
	cin >> tc;
	for (int cc = 1; cc <= tc; ++cc)
	{
		basintag = 0;

		int h, w;
		cin >> h >> w;

		for (int x = 0; x <= w+1; ++x)
		for (int y = 0; y <= h+1; ++y)
		{
			board[x][y] = inf;
			basin[x][y] = nobasin;
		}

		for (int y = 1; y <= h; ++y)
		for (int x = 1; x <= w; ++x)
			cin >> board[x][y];

		for (int x = 1; x <= w; ++x)
		for (int y = 1; y <= h; ++y)
			flood(point(x,y));

		labeltag = 'a';
		labels.clear();
		for (int y = 1; y <= h; ++y)
		for (int x = 1; x <= w; ++x)
			basin[x][y] = getLabel( basin[x][y] );

		cout << "Case #" << cc << ':' << endl;
		for (int y = 1; y <= h; ++y)
		{
			for (int x = 1; x <= w; ++x)
				cout << basin[x][y] << ' ';
			cout << endl;
		}
	}
	return 0;
}
