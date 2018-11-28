/*
 * Google Code Jam 2010. Round 1 - sub-round A
 * (C)Copyright jclin (j i a n c h e n g [at] g_m_a_i_l [dot] c_o_m)
 */
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cassert>

using namespace std;

#define FOR(i,N)	for(int i=0;i<N;++i)

int go() {
	int people, surprise, min;
	int scores[500];

	cin >> people >> surprise >> min;
	FOR(i, people) {
		cin >> scores[i];
	}

	int cases = 0;

	FOR(i, people) {
		int score = scores[i];
		int avg = score/3;
		cerr << "avg=" << avg << endl;

		switch(score % 3) {
			case 0:
				if (avg >= min)
					cases++;
				else {
					if (surprise > 0 && avg > 0 && (avg+1) >= min) {
						cases++;
						surprise--;
					}
				}
				break;
			case 1:
				if (avg >= min || (avg+1) >= min) {
					cases++;
				}
				else if (surprise > 0 && (avg+1) >= min) {
					cases++;
					surprise--;
				}
				break;
			case 2:
				if (avg+1 >= min || avg >= min)
					cases++;
				else if (surprise > 0 && (avg+2) >= min) {
					cases++;
					surprise--;
				}
				break;
			default:
				assert(0);
				break;
		}
	}
	return cases;
}

int main(int ac, char**av)
{
	int N;

	cin >> N;
	FOR(i,N) {
		cout << "Case #" << i+1 << ": " << go() << endl;
	}
	return 0;
}

