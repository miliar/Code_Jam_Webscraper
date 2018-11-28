#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int others[100];

int solve(int oth, int low, int upp) 
{
	for (int i = low; i <= upp; ++i) {
		int j;
		for (j = 0; j < oth; ++j) {
			if (others[j] % i != 0 && i % others[j] != 0) {
				break;
			}
		} // for (int i = low; i <= upp; ++i) {for (int j = 0; j < oth; ++j)
		if (j == oth) {
			return i;
		}
	}
	return 0;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int oth, low, upp;
		cin >> oth >>low >>upp;
		for (int i = 0; i < oth; ++i) {
			cin >> others[i];
		}
		int result = solve(oth, low, upp);
		if (result == 0) {
			cout << "Case #" <<curCase << ": " << "NO" <<endl;
		}
		else {
			cout << "Case #" <<curCase << ": " << result <<endl;
		}
	}
}