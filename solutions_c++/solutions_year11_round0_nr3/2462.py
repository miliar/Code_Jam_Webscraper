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
	int T;
	cin >> T;
	FOR(i, 0, T) {
		int N;
		cin >> N;
		vector<int> list;
		int largest = -1;
		int smallest = 1e7;
		int sum = 0;
		FOR (j, 0, N) {
			int C;
			cin >> C;
			if (C > largest) {
				largest = C;
			}
			if (C < smallest) {
				smallest = C;
			}
			sum += C;
			list.push_back(C);
		}
		double ll = log(largest)/log(2);

		int no = false;
		for (int b = ll + 1; b >= 1; b--) {
			int count = 0;
			FOR(i, 0, list.size()) {
				int set = (list[i] >> (b -1)) & 1;
				if (set) {
					count ++;
				}
			}
			if (count & 1) {
				no = true;
				break;
			}
		}

		cout << "Case #" << i + 1 << ": ";
		if (no) {
			cout << "NO";
		} else {
			cout << sum - smallest;
		}
		cout << endl;
	}
}
