#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

typedef pair<int, int> coord;

int main(int argc, char** argv) {
	ifstream infile(argv[1]);

	int num_cases;
	infile >> num_cases;

	for(int i = 0; i < num_cases; i++) {
		cout << "Case #" << i+1 << ": ";

		long long n, A, B, C, D, x0, y0, M;
		infile >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		vector< pair<int, int> > points(n);
		long long X = x0;
		long long Y = y0;
		for(int j = 0; j < n; j++) {
			points[j] = coord(X,Y);
			cerr << "(" << X << "," << Y << ")" << endl;
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}

		int count = 0;

		for(int j = 0; j < n - 2; j++) {
			for(int k = j+1; k < n - 1; k++) {
				for(int l = k+1; l < n; l++) {
					//double centerx = (double)(points[j].first + points[k].first + points[l].first) / 3;
					//double centery = (double)(points[j].second + points[k].second + points[l].second) / 3;
					long long centerx = (points[j].first + points[k].first + points[l].first);
					long long centery = (points[j].second + points[k].second + points[l].second);
					if(centerx % 3) continue;
					if(centery % 3) continue;
					//cerr << centerx << ", " << centery << endl;
					count++;
				}
			}
		}
		cout << count << endl;
	}
	
	return 0;
}
