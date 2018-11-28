#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

struct Group {
	unsigned long long n;
	Group* next;

	Group(unsigned long long n_) : n(n_) { }
};

class ThemePark {
public:
	unsigned long long solve(unsigned long long R , unsigned long long k, unsigned long long N, const Group* g)
	{
		int i, j;
		unsigned long long euros = 0;
		for (unsigned long long i = 0; i < R; i++) {
			unsigned long long s = 0;
			for (unsigned long long j = 0; j < N; j++) {
				if (s + g->n > k) break;
				s += g->n;
				g = g->next;
			}
			euros += s;
		}
		return euros;
	}
};

int main()
{
//	fstream fs("test.in", ios_base::in);
	fstream fs("C-large.in", ios_base::in);
	string line;
	stringstream ss;

	ThemePark tp;

	getline(fs, line);
	ss.str(line);
	unsigned long long T, R, k, N, n;
//	vector<unsigned long long> g(N);
	ss >> T;
	ss.clear();  ss.str("");
	int cnt = 0;

	for (int i = 0; i < T; i++) {
		Group* g;
		getline(fs, line);
		ss.str(line);
		ss >> R >> k >> N;
		ss.clear();  ss.str("");

		getline(fs, line);
		ss.str(line);
		ss >> n;
		g = new Group(n);
		Group* start_g = g;
		for (int j = 1; j < N; j++) {
			ss >> n;
			g->next = new Group(n);
			g = g->next;
		}
		g->next = start_g;
		g = g->next;
		ss.clear();  ss.str("");

		cout << "Case #" << ++cnt << ": " << tp.solve(R, k, N, g) << endl;
	}

	return 0;
}
