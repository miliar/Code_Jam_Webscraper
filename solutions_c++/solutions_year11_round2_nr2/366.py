#include <iostream>
#include <iomanip>

#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <complex>
#include <cmath>
#include <map>
#include <numeric>
#include <set>
#include <iterator>
#include <bitset>

using namespace std;

//ostream_iterator<int> spout(cout, " ");

typedef pair<int, int> pii;
typedef vector<pii> vpii;

int C, D;
vpii vendor;

void parseCase(istream &inp)
{
	vendor.clear();

	inp >> C >> D;
	D *= 2;
	for (int j = 0; j < C; ++j)
	{
		int p, v;
		inp >> p >> v;
		p *= 2;
		vendor.push_back(pii(p,v));
	}
}

bool possible(int T)
{
	int iter = vendor[0].first - T - D;

	for (int j = 0; j < C; ++j)
	{
		if (iter > vendor[j].first + T)
			return false;

		iter = max(iter+D, vendor[j].first - T);

		iter += D*(vendor[j].second-1);

		if (iter > vendor[j].first + T)
			return false;
	}

	return true;
}

double answer()
{
	sort(vendor.begin(), vendor.end());

	int t = 0, thi = 1024;

	while (t != thi)
	{
		int tm = (t + thi) / 2;
		if (possible(tm))
			thi = tm;
		else
			t = tm+1;
	}

	return double(t) / 2;
}

#ifndef ANS_NOMAIN
int main()
{
	int T;
	cin >> T;
	cout << fixed << setprecision(1);
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		parseCase(cin);
		cout << "Case #" << caseNum << ": " << answer() << endl;
	}

	return 0;
}
#endif
