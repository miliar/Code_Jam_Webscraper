#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Perfect Game
bool compare(const vector <int> &a, const vector <int> &b)
{
	if (b[1] * a[0] != b[0] * a[1]) {  
		return (b[1] * a[0] < b[0] * a[1]);
	}
	return (a[2] < b[2]);
}

int main()
{
	int cases;
	cin >> cases;
	
	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		vector <vector <int> > LPI(N, vector <int>(3));
		for (int i = 0; i < N; i++) {
			cin >> LPI[i][0];
			LPI[i][2] = i;
		}
		for (int i = 0; i < N; i++) {
			cin >> LPI[i][1];
		}
		sort(LPI.begin(), LPI.end(), compare);
		cout << "Case #" << caseno << ":";
		for (int i = 0; i < LPI.size(); i++) {
			cout << " " << LPI[i][2];
		}
		cout << endl;
	}

	return 0;
}
