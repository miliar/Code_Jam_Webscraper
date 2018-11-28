#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <cmath>

using namespace std;
const int inf = INT_MAX / 4;

const int max_googler = 100;
int googler[max_googler];
int n_googler;
int n_surprise;
int p;
int n_greater;

void input(void)
{
	int i, j, k;
	cin >> n_googler >> n_surprise >> p;
	for (i = 0; i < n_googler; i++)
		cin >> googler[i];
}

void output(int icase)
{
	int i, j, k;
	cout << "Case #" << icase + 1 << ": " << n_greater << endl;
}

void solve(void)
{
	int i, j, k;

	n_greater = 0;
	for (i = 0; i < n_googler; i++) {
		if (p && !googler[i]) continue;
		
		if (p * 3 - 2 <= googler[i]) {
			n_greater++;
			continue;
		}
		
		if (p * 3 - 4 <= googler[i]) {
			if (n_surprise > 0) {
				n_greater++;
				n_surprise--;
			}
		}
	}
}

int main()
{
	int n_case;
	cin >> n_case;
	for (int i = 0; i < n_case; i++) {
		input();
		solve();
		output(i);
	}
	return 0;
}
