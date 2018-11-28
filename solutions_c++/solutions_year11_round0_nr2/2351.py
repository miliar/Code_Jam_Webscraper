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
	int N;
	cin >> N;
	FOR(i, 0, N) {
		int C;
		cin >> C;
		map<pair<char, char>, char> comb;
		FOR (j, 0, C) {
			char c1, c2, c3;
			cin >> c1;
			cin >> c2;
			cin >> c3;
			comb[pair<char, char>(c1, c2)] = c3;
			comb[pair<char, char>(c2, c1)] = c3;
		}
		int D;
		cin >> D;
		map<pair<char, char>, int> oppos;
		FOR (j, 0, D) {
			char c1, c2;
			cin >> c1;
			cin >> c2;
			oppos[pair<char, char>(c1, c2)] = 1;
			oppos[pair<char, char>(c2, c1)] = 1;
		}
		int N;
		cin >> N;
		vector<char> list;
		FOR(j, 0, N) {
			char c;
			cin >> c;
			char d = 0;
			if (list.size() > 0) {
				d = list[list.size()-1];
			}
			if (comb.count(pair<char, char>(c, d)) > 0) {
				c = comb[pair<char, char>(c, d)];
				list[list.size()-1] = c;
			} else {
				list.push_back(c);
			}

			FOR(k, 0, list.size()) {
				if (oppos[pair<char, char>(list[k], c)]) {
					list.clear();
					break;
				}
			}
		}

		cout << "Case #" << i + 1 << ": [";
		FOR(j, 0, list.size()) {
			cout << list[j];
			if (j != list.size()-1) {
				cout << ", ";
			}
		}
		cout << "]" << endl;
	}
}
