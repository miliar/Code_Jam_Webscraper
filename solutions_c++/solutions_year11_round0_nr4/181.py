#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");

	int T = 0;
	f >> T;
	for (int i = 0; i < T; ++i) {

		//read input
		int N = 0;
		f >> N;
		vector<int> v(N+1);
		for (int j = 1; j <= N; ++j)
			f >> v[j];

		set<int> ind;
		int counted = 0;
		int ci = 0;
		for (int j = 1; j <= N; ++j) {
			if (v[j] == j) {
				counted++;
				ind.insert(j);
			} else
				ci = j;
		}

		int res = 0;
		if (counted != N) {
			int cyclelen = 0;
			while (counted < N) {
				if (ind.find(v[ci]) == ind.end()) {
					ind.insert(v[ci]);
					counted++;
					cyclelen++;
					ci = v[ci];
				} else {
					res += cyclelen;
					cyclelen = 0;
					for (int j = 1; j <= N; ++j)
						if (ind.find(j) == ind.end()) {
							ci =  j;
							break;
						}
				}
			}
			res += cyclelen;
		}

		
		cout << "Case #" << i+1 << ": " << res << ".000000" << endl;
		of << "Case #" << i+1 << ": " << res << ".000000" << endl;
	}
	f.close();
	of.close();
	cin.get();
}