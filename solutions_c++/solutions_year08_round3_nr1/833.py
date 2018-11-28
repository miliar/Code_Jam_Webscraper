//
// Round 1, Task A.
//


#define _USE_MATH_DEFINES	1

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>


void solve();

using namespace std;



int main()
{
	ifstream inf("in.txt");
	cin.rdbuf(inf.rdbuf());
	ofstream ouf("out.txt");
	cout.rdbuf(ouf.rdbuf());

	solve();

	return 0;
}


void solve()
{
	int T;
	cin >> T;

	static char p[100000];

	for (int t = 1; t <= T; ++t)
	{
		int P, K, L;
		cin >> P >> K >> L;

		vector<int> freq;
		for (int l = 0; l < L; ++l)
		{
			int f;
			cin >> f;
			freq.push_back(f);
		}
		sort(freq.begin(), freq.end());

		int rez = 0;
		int lag = 1;
		int iter = L - 1;

		while (iter >= 0)
		{
			for (int i = 0; i < K  &&  iter >= 0; ++i, --iter)
				rez += lag * freq[iter];
			++lag;
		}

		cout << "Case #" << t << ": " << rez << endl;
	}
}