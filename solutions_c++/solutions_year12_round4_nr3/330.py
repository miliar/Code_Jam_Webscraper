#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include <queue>
#include <set>
using namespace std;

#define MINV 0
#define MAXV 10e9

int main(int argc, const char * argv[])
{
	ifstream ifs( "input.txt" );
    int T = 0;
    ifs >> T;
    for (int i = 0; i < T; i++) {
		int N;
		ifs >> N;
		vector<int> lookH;
		for (int j = 0; j < N-1; j++) {
			int p;
			ifs >> p;
			lookH.push_back(p-1);
		}
		set<int> scalefactors;
		vector<pair<long, long> > peaks;
		for (int j = 0; j < N; j++) {
			peaks.push_back(make_pair(MINV, MAXV));
		}
		peaks[0] = make_pair(100, 100);
		for (int j = 0; j < N; j++) {
			double inc = 1;
			for (int k = j+1; k < N; k++) {
				inc = max(inc, (double)(peaks[k].first-peaks[j].first)/(k-j));
			}
			for (int k = j+1; k < N; k++) {
				if (k != lookH[j]) {
					peaks[k].second = min((double)peaks[k].second, floor(inc*(k-j)+peaks[j].first));
				}else {
					peaks[k].first = max((double)peaks[k].first, ceil(inc*(k-j)+peaks[j].first));
				}

			}
		}
		
		bool impossible = false;
		for (int j = 0; j < N; j++) {
			if (peaks[j].first > peaks[j].second) {
				impossible = true;
				break;
			}
		}
		
		if (impossible) {
			cout << "Case #" << i+1 << ": Impossible";
		}else {
			cout << "Case #" << i+1 << ": ";
			for (int j = 0; j < N; j++) {
				cout << peaks[j].first <<  " ";
			}
			
		}
		cout << endl;
	}
}