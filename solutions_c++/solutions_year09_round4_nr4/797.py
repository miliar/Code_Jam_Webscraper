#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

double d(vector <int> a, vector <int> b)
{
	return (sqrt((double)(a[0] - b[0]) * (a[0] - b[0]) +
		     (double)(a[1] - b[1]) * (a[1] - b[1])) +
		a[2] + b[2]) / 2.0;
}

double WateringPlants(vector <vector <int> > plants)
{
	if (plants.size() == 3) {
		return min(min(max(d(plants[0], plants[1]), (double)plants[2][2]),
			       max(d(plants[0], plants[2]), (double)plants[1][2])),
			   max(d(plants[1], plants[2]), (double)plants[0][2]));
	} else {
		double ret = 0;
		for (int i = 0; i < plants.size(); i++) {
			ret = max(ret, (double)plants[i][2]);
		}
		return ret;
	}
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		vector <vector <int> > plants(N, 3);
		for (int i = 0; i < N; i++) {
			cin >> plants[i][0];
			cin >> plants[i][1];
			cin >> plants[i][2];
		}

		double ret = WateringPlants(plants);

		cout << setiosflags(ios::fixed) << setprecision(6);
		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
