#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

#include <limits.h>

using namespace std;

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define FORD(i,a,b) for((i)=(a);(i)<=(int)(b);(i)++)

#define MAX_N 100

int wins[MAX_N][MAX_N];
double twins[MAX_N];
int tplayed[MAX_N];
double owp[MAX_N];
double oowp[MAX_N];

int solve(int test)
{
	int n;
	int i, j;
	string line;
	char entry;
	int result = 0;
	
	cout << "Case #" << test << ": ";

	cin >> n;

	FOR(i, n) {
		cin >> line;

		twins[i] = tplayed[i] = 0;

		FOR(j, n) {
			entry = line[j];
			wins[i][j] = (entry == '1') ? 1 : (entry == '0') ? 0 : -1;

			if (wins[i][j] != -1) {
				if (wins[i][j] == 1) {
					twins[i] ++;
				}
				tplayed[i]++;
			}
		}
	}

	FOR(i, n) {
		if (!tplayed[i])
			continue;
		
		owp[i] = 0;
		
		FOR(j, n) {

			if (wins[i][j] == 1) {
				if (tplayed[j] != 1)
					owp[i] += twins[j] / (tplayed[j] - 1);
			} else if (wins[i][j] == 0) {
				if (tplayed[j] != 1)
					owp[i] += (twins[j] - 1) / (tplayed[j] - 1);
			}

		}
		
		owp[i] /= tplayed[i];
	}
	
	FOR(i, n) {
		if (!tplayed[i])
			continue;
		
		oowp[i] = 0;		

		FOR(j, n) {

			if (wins[i][j] != -1) {
				oowp[i] += owp[j];
			}
		}
		
		oowp[i] /= tplayed[i];
	}
	
	cout << endl;
	
	//cout.setf(0,ios::floatfield);            // floatfield not set
 	cout.precision(8);

	FOR(i, n) {
		if (!tplayed[i])
			cout << 0 << endl;
		else
			cout << 0.25 * twins[i] / tplayed[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
	}

	return 0;
}

int main()
{
	int cases = 0;
	int i;

	cin >> cases;

	FOR(i, cases) {
		solve(i + 1);
	}
	
	return 0;
}
