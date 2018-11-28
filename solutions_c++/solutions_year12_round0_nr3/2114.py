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
const int max_ab = 3000000;
int mark[max_ab];
int A, B;
int n_cycle;

void input(void)
{
	int i, j, k;
	cin >> A >> B;
}

void output(int icase)
{
	int i, j, k;
	cout << "Case #" << icase + 1 << ": " << n_cycle << endl;
}

void solve(void)
{
	int i, j, k;
	int mul = 1;
	int d_len = 1;
	k = A / 10;
	for (k = A / 10; k; k /= 10) {
		mul *= 10;
		d_len++;
	}
	//cout << A << " " << mul << " " << d_len << endl;
	n_cycle = 0;
 	memset(mark, 0, sizeof(mark));
	for (k = A; k <= B; k++) {
		if (mark[k]) continue;
		mark[k] = 1;

		int cycle_len = 1;
		int num = k;
		//cout << num << " ";
		for (i = 1; i < d_len; i++) {
			num = num % 10 * mul + num / 10;
			//cout << num << " ";
			if (num >= A && num <= B && !mark[num]) {
				cycle_len++;
				mark[num] = 1;
			}
		}
		//cout << ": " << cycle_len << endl;

		while (cycle_len)
			n_cycle += --cycle_len;
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
