#include <algorithm>
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

char p[100][100];

int
main()
{
	int cases; 
	int result = 0;

	cin >> cases;

	foreach(i, 1, cases) {
		int R, C;

		cin >> R >> C;

		foreach(j, 0, R - 1) {
			string tmp;
			cin >> tmp;

			foreach(k, 0, C - 1) {
				p[j][k] = tmp.at(k);	
			}
		}

		foreach(j, 0, R - 2) {
			foreach(k, 0, C - 2) {
				if (p[j][k] == '/' || p[j][k] == '\\' ||
						p[j][k + 1] == '/' || p[j][k + 1] == '\\' || 
						p[j + 1][k] == '/' || p[j + 1][k] == '\\' || 
						p[j + 1][k + 1] == '/' || p[j + 1][k + 1] == '\\') continue;

				if (p[j][k] == '#' && 
						p[j][k + 1] == '#' && 
						p[j + 1][k] == '#' && 
						p[j + 1][k + 1] == '#') {
					p[j][k] = '/';
					p[j][k + 1] = '\\';
					p[j + 1][k] = '\\';
					p[j + 1][k + 1] = '/';
				}
			}
		}

		foreach(j, 0, R - 1) {
			foreach(k, 0, C - 1) {
				if (p[j][k] == '#')
					goto nope;
			}
		}

		printf("Case #%d:\n", i);
		foreach(j, 0, R - 1) {
			foreach(k, 0, C - 1) {
				printf("%c", p[j][k]);
			}
			cout << endl;
		}

		continue;
nope:		
		printf("Case #%d:\nImpossible\n", i);
	}

	return 0;
}
