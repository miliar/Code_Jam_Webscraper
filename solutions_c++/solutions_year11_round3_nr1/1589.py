#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>
#include <queue>
#include <deque>
#include <string.h>
#include <set>
#include <stdio.h>

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;
typedef long double ld;

#define FOR(I,z,k) for(int I = z; I < (k); I ++)
#define tr(container, it) \
     for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define all(v) (v).begin(), (v).end()
#define PI 3.14159265
#define tovector(arr, type) vector<type>(arr, arr + sizeof(arr)/sizeof(type))


int main() {
	int t;
	cin >> t;

	FOR(p, 0, t) {
		int r, c;
		cin >> r;
		cin >> c;
		vector<string> tiles;
		FOR(i, 0, r) {
			string x;
			cin >> x;
			tiles.push_back(x);
		}

		bool failed = 0;
		FOR(i, 0, r-1) {
			FOR(j, 0, c-1) {
				if(tiles[i][j] == '#') {
					if (tiles[i][j+1] == '#' && tiles[i+1][j] == '#' && tiles[i+1][j+1] == '#') {
						tiles[i][j] = '/';
						tiles[i][j+1] = '\\';
						tiles[i+1][j] = '\\';
						tiles[i+1][j+1] = '/';
					} else {
						failed = 1;
						break;
					}
				}
			}
			if (failed) {
				break;
			}
		}
		if (!failed) {
			FOR(i, 0, r) {
				FOR(j, 0, c) {
					if(tiles[i][j] == '#') {
						failed = 1;
						break;
					}
				}
				if (failed) {
					break;
				}
			}
		}
		cout << "Case #" << p + 1 << ":" << endl;
		if (failed) {
			cout << "Impossible" << endl;
		} else {
			FOR(i, 0, r) {
				cout << tiles[i]  << endl;
			}
		}
	}
}
