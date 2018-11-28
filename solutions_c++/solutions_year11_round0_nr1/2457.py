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
		int n;
		cin >> n;
		vector<ii> orange; // turn, button
		vector<ii> blue; // turn, button
		int o_pos = 1;
		int b_pos = 1;
		FOR (j, 0, n) {
			char c;
			int s;
			cin >> c;
			cin >> s;
			if (c == 'O') {
				int change = abs (s - o_pos);
				o_pos = s;
				orange.push_back(ii(j, change));
			} else {
				int change = abs (s - b_pos);
				b_pos = s;
				blue.push_back(ii(j, change));
			}
		}
		int oo = 0;
		int b = 0;
		int t = 0;

		while (oo < orange.size() && b < blue.size()) {
			if (orange[oo].first < blue[b].first) {
				t += orange[oo].second + 1;
				blue[b].second -= orange[oo].second + 1;
				if (blue[b].second < 0) blue[b].second = 0;
				oo ++;
			} else {
				t += blue[b].second + 1;
				orange[oo].second -= blue[b].second + 1;
				if (orange[oo].second < 0) orange[oo].second = 0;
				b ++;
			}
		}
		while (oo < orange.size()) {
			t += orange[oo].second + 1;
			oo ++;
		}
		while (b < blue.size()) {
			t += blue[b].second + 1;
			b ++;
		}
		cout << "Case #" << i + 1 << ": " << t << endl;
	}
}
