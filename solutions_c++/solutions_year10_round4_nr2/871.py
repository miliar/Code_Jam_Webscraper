#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

int need[1024];
int cost[10][512];

int calc(int *need, int n)
{
	if (n == 1) {
		return need[0];
	}

	int ans = 0;
	bool found = false;
	for (int i=0; i<n; ++i) {
		if (need[i] >= 1) {
			need[i]--;
			found = true;
		}
	}

	if (found) ans++;
	ans += calc(need, n/2) + calc(need+n/2, n/2);
	return ans;
}

string calc()
{
	stringstream S;
	int i, j;

	int P;
	cin >> P;

	for (i=0; i<(1<<P); ++i) {
		cin >> need[i];
		need[i] = P - need[i];
	}

	for (i=0; i<P; ++i) {
		for (j=0; j<(1<<(P-1-i)); ++j) {
			cin >> cost[i][j];
		}
	}

	int ans = calc(need, 1<<P);
	S << ans;

	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

