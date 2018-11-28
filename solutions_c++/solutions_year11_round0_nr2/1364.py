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

using namespace std;

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define MAX_P 1000

#define COMBINE_BASE 32

char opposed[MAX_P];
char combine[MAX_P];

vector<int> result;

void run(string invoke)
{
	int i, j, index;
	int next;

	result.resize(0);
	result.reserve(invoke.length());

	FOR(i, invoke.length()) {
		next = invoke[i] - 'A';

		if (result.size()) {
			index = next * COMBINE_BASE + result[result.size() -1];

			if (combine[index]) {
				result[result.size() -1] = combine[index];
				continue;
			}
		
			FOR(j, result.size()) {
				index = next * COMBINE_BASE + result[j];

				if (opposed[index]) {
					result.resize(0);
					break;
				}
			}

			if (!result.size())
					continue;
		}

		result.push_back(next);
	}
}

int solve(int test)
{
	int i;
	int count;
	string invoke_str;
	string combine_str;
	string opposed_str;

	memset(&combine, 0, MAX_P * sizeof(char));
	memset(&opposed, 0, MAX_P * sizeof(char));

	cout << "Case #" << test << ": ";

	cin >> count;

	FOR(i, count) {
		cin >> combine_str;

		combine[(combine_str[0] - 'A') * COMBINE_BASE + (combine_str[1] - 'A')] = combine_str[2] - 'A';
		combine[(combine_str[1] - 'A') * COMBINE_BASE + (combine_str[0] - 'A')] = combine_str[2] - 'A';
	}

	cin >> count;

	FOR(i, count) {
		cin >> opposed_str;

		opposed[(opposed_str[0] - 'A') * COMBINE_BASE + (opposed_str[1] - 'A')] = 1;
		opposed[(opposed_str[1] - 'A') * COMBINE_BASE + (opposed_str[0] - 'A')] = 1;
	}

	cin >> count >> invoke_str;

	run(invoke_str);

	cout << "[";

	FOR(i, result.size()) {
		if (i)
			cout << ", ";
		cout << (char)('A' + result[i]);
	}

	cout << "]" << endl;

	return 0;
}

int main()
{
	int cases = 0;
	int i;

	freopen("B_small_1.in", "r", stdin);
	freopen("B_small_1.out", "w", stdout);
	
	cin >> cases;

	FOR(i, cases) {
		solve(i + 1);
	}
	
	return 0;
}
