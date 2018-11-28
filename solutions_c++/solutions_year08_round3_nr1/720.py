#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <utility>
#include <functional>

using namespace std;

#define FOR(i, l, u) for(int (i)(l); i < (u); ++(i))
#define FORD(i, u, l) for(int (i)(u); (i) >= (l); --(i))

struct letter {
	int no;
	int freq;
	bool operator < (letter const & rhs) const { return rhs.freq < this->freq; }
};

int main() {
	ifstream fin("prob1.in");
	ofstream fout("prob1.out");
	
	int T, P, K, L;
	fin >> T;
	FOR(c, 0, T) {
		int P;
		fin >> P >> K >> L;
		vector<letter>  freq(L);
		FOR(l, 0, L) {
			fin >> freq[l].freq;
			freq[l].no = l;
		}
		sort(freq.begin(), freq.end());
		FOR(t, 0, freq.size()) {
			cout << freq[t].freq << " ";
		}
		fout << "Case #" << c+1 << ": ";
		if (K > L) { 
			fout << "Impossible\n";
		}
		else {
			int count = 0;
			for(int i = 0; i < L; ++i) {
				count += (i/K + 1)*freq[i].freq;
			}
			fout << count << '\n';
		}
	}
	
	return 0;
}
