#include <fstream>
#include <iostream>

struct Cell {
	int height;
	int color;
	void init(std::istream & is) { is >> height; color = 99; }
	void initMax() { height = 20000; color = 99; }
	bool visited() const { return color != 99; }
};

struct Map {
	Map(std::istream & is) 
	{
		nSinks = 0;
		is >> h;
		is >> w;

		cells = new Cell[(w+2)*(h+2)];

		int offset = 0;
		for (int i = 0; i < w+2; i++) cells[offset++].initMax();
		for (int row = 0; row < h; row++) 
		{
			cells[offset++].initMax();
			for (int col = 0; col < w; col++) cells[offset++].init(is);
			cells[offset++].initMax();
		}
		for (int i = 0; i < w+2; i++) cells[offset++].initMax();
	}
	~Map() { delete[] cells; }
	void testMin(int offset, std::pair<int, int> & x) {
		int hh = cells[offset].height;
		if (hh < x.second) {
			x.first = offset;
			x.second = hh;
		}
	}

	void solve(int offset) {
		int stack[10001];
		int sp = 0;

		stack[sp] = offset;
		while (sp<10001) {
			offset = stack[sp];
			Cell & c = cells[stack[sp]];
			if (c.visited()) break;

			std::pair<int, int> min(0, c.height);
			testMin(offset-w-2, min);
			testMin(offset-1, min);
			testMin(offset+1, min);
			testMin(offset+w+2, min);

			if (min.first == 0) {
				c.color = nSinks++;
				break;
			}
			stack[++sp] = min.first;
		}
		int color = cells[stack[sp]].color;
		for (int i = 0; i < sp; i++) cells[stack[i]].color = color;
	}

	void solve() {
		for (int row = 1; row < h+1; row++) {
			for (int col = 1; col < w+1; col++) {
				int offset = row*(w+2)+col;
				solve(offset);
			}
		}
	}
	void print(int testCase) {
		std::cout << "Case #" << testCase << ":\n";
		for (int row = 1; row < h+1; row++) {
			for (int col = 1; col < w+1; col++) {
				int offset = row*(w+2)+col;
				std::cout << (char)('a' + cells[offset].color) << ' ';
			}
			std::cout << "\n";
		}
	}
private:
	int w, h;
	int nSinks;
	Cell * cells;
};

int main(int argc, char* argv[])
{
	if (argc < 2) {
		std::cout << "Need input filename\n";
		return 1;
	}
	std::fstream fs(argv[1]);
	int nMaps;
	fs >> nMaps;
	for (int i = 0; i < nMaps; i++) {
		Map m(fs);
		m.solve();
		m.print(i+1);
	}

	return 0;
}

