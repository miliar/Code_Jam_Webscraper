#include <algorithm>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <vector>

#include <limits.h>
#include <math.h>
#include <stdio.h>

using namespace std;

#define foreach(k, b, N) for (int k = b; k <= N; k++)
#define foreach_r(k, b, N) for (int k = b; k >= N; k--)

char s[150][150];
long double wp[150];
long double owp[150];
long double oowp[150];

int
main()
{
	int cases; 
	long double result = 0;

	cin >> cases;

	foreach(i, 1, cases) {
		int N;
		cin >> N;

		foreach(j, 0, N - 1) {
			string tmp;
			cin >> tmp;
		
			foreach(k, 0, N - 1)
				s[j][k] = tmp.at(k);
		}

		foreach(j, 0, N - 1) {
			int played = 0;
			int won = 0;
			foreach(k, 0, N - 1) {
				if (s[j][k] != '.')
					played++;
				if (s[j][k] == '1')
					won++;
			}
			wp[j] = (long double)won / (long double)played;
		}

		foreach(j, 0, N - 1) {
			int num = 0;
			long double rsum = 0;
			foreach(k, 0, N - 1) {
				int played = 0;
				int won = 0;

				if (k != j && s[j][k] != '.') {
					num++;
					foreach(l, 0, N - 1) {
						if (l != j) { 
							if (s[k][l] != '.')
								played++;
							if (s[k][l] == '1')
								won++;
						}
					}
				}
				
				if (played != 0)
					rsum += (long double)won / (long double)played;
			}
				
			owp[j] = rsum / (long double)num;
	
		}

		foreach(j, 0, N - 1) {
			int num = 0;
			long double rsum = 0;
			foreach(k, 0, N - 1) {
				if (s[j][k] != '.') {
					rsum += owp[k];
					num++;
				}
			}
			
			oowp[j] = rsum / (long double)num;
		}

		setprecision(12);
		printf("Case #%d:\n", i);

		foreach(j, 0, N - 1) {
			result = 0;

			result = 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
			cout << setprecision(12) << result << endl;
		}
	}

	return 0;
}
