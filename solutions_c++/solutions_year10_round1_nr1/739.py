#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <vector>
#include <map>
#include <list>
#include <cmath>

using namespace std;

bool solve(vector<string>& data, char c, int n, int k, bool flip)
{
	for (int i=0; i<n; i++) {
		int count = 0;
		for (int j=0; j<n; j++) {
			char cur;
			if (flip) cur = data[i][j];
			else cur = data[j][i];

			if (cur == c) {
				count++;
				if (count >= k) return true;
			} else {
				count = 0;
			}
		}
	}
	return false;
}

bool solveDiagonal(vector<string>& data, char c, int n, int k, bool flip)
{
	int tested = 0;
	int total = n*2-1;
	for (int i=0; i<total; i++) {
		int count = 0;
		int yb = i;
		int xb = 0;
		if (yb >= n) {
			xb = yb-n+1;
			yb = n-1;
		}

		for (int j=0; true; j++) {
			char cur;

			int x = xb+j;
			int y = yb-j;
			if (y < 0) break;
			if (x >= n) break;

			if (flip) cur = data[y][n-1-x];
			else cur = data[y][x];

			tested++;

			if (cur == c) {
				count++;
				if (count >= k) return true;
			} else {
				count = 0;
			}
		}
	}
	return false;
}

bool solve(vector<string>& data, char c, int n, int k)
{
	return solve(data, c, n, k, false)
		|| solve(data, c, n, k, true)
		|| solveDiagonal(data, c, n, k, false)
		|| solveDiagonal(data, c, n, k, true);
}

void processCase(istream& in, ostream& out)
{
	int n, k;
	in >> n;
	in >> k;

	// Parse
	char tmp;
	vector<string> data;
	data.resize(n);
	for (int y=0; y<n; y++) {
		data[y].resize(n);
		for (int x=0; x<n; x++) {
			do {
				in >> tmp;
			} while (tmp != '.' && tmp != 'R' && tmp != 'B');
			data[y][x] = tmp;
		}
	}

	// Gravity
	for (int y=0; y<n; y++) {
		int available = n-1;
		for (int x=n; --x>=0; ) {
			char& src = data[y][x];

			if (src != '.') {
				if (available != x) {
					data[y][available] = src;
					src = '.';
				}
				available--;
			}
		}
	}

	bool red = solve(data, 'R', n, k);
	bool blue = solve(data, 'B', n, k);

	// Print result
	string result = red? (blue? "Both" : "Red") : (blue? "Blue" : "Neither");
	out << result.c_str();
}

int main()
{
	ifstream in("A-large.in");
	//ifstream in("testin.txt");
	//ostream& out = cout;
	ofstream out("A-large.out", std::ios_base::out | std::ios_base::binary);

	int nCases;
	in >> nCases;
	char tmp[2];
	in.getline(tmp, 2);
	for (int i=0; i<nCases; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
		out << endl;
	}

	out.flush();
}
