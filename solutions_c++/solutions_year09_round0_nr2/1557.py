#include <iostream>
#include <fstream>
#include <vector>

using std::string;
using std::cin;
using std::vector;
using std::istream;
using std::ostream;
using std::ifstream;
using std::ofstream;
using std::min;

typedef vector<vector<int>> mapType;

int getValue(mapType &map, int x, int y)
{
	const int def = 50000;
	if (x < 0 || y < 0 || x >= (signed)map.size() || y >= (signed)map[0].size())
		return def;
	return map[x][y];
}

bool isSink(mapType &map, int x, int y)
{
	int cur = map[x][y];
	int n = getValue(map, x, y-1);
	int w = getValue(map, x-1, y);
	int e = getValue(map, x+1, y);
	int s = getValue(map, x, y+1);
	return (cur <= n && cur <= w && cur <= e && cur <= s);
}

int traceBasin(mapType &elevations, mapType &map, int x, int y)
{
	if (map[x][y] != -1) {
		// Already in a basin
		return map[x][y];
	} else {
		int n = getValue(elevations, x, y-1);
		int w = getValue(elevations, x-1, y);
		int e = getValue(elevations, x+1, y);
		int s = getValue(elevations, x, y+1);
		int minVal = min(n, min(w, min(e, s)));
		int dx = x;
		int dy = y;

		if (n == minVal) dy--;
		else if (w == minVal) dx--;
		else if (e == minVal) dx++;
		else if (s == minVal) dy++;
		else throw std::exception();

		int result = traceBasin(elevations, map, dx, dy);
		map[x][y] = result;
		return result;
	}
}

void processMap(mapType &map, int n, ostream &out)
{
	out << "Case #" << n << ":\n";
	int w = map.size();
	int h = map[0].size();
	mapType basins(w, vector<int>(h, -1));

	// Find all sinks
	int nSinks = 0;
	for (int y=0; y<h; y++) {
		for (int x=0; x<w; x++) {
			if (isSink(map, x, y)) {
				basins[x][y] = nSinks++;
			}
		}
	}

	// Fill all cells
	for (int y=0; y<h; y++) {
		for (int x=0; x<w; x++) {
			traceBasin(map, basins, x, y);
		}
	}

	// Create a mapping between basins and characters
	vector<char> bName(nSinks, '*');
	char letter = 'a';
	for (int y=0; y<h; y++) {
		for (int x=0; x<w; x++) {
			int basin = basins[x][y];
			char name = bName.at(basin);
			if (name == '*') {
				name = letter++;
				bName[basin] = name;
			}

			out << bName[basin];
			if (x == w-1)
				out << '\n';
			else
				out << ' ';
		}
	}
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out", std::ios_base::out | std::ios_base::binary);

	int nMaps;
	in >> nMaps;
	for (int i=0; i<nMaps; i++) {
		// Read header
		int w, h;
		in >> h;
		in >> w;

		// Read map
		mapType map(w, vector<int>(h, 0));
		for (int y=0; y<h; y++) {
			for (int x=0; x<w; x++) {
				in >> map[x][y];
			}
		}

		processMap(map, i+1, out);
	}

	out.flush();
}
