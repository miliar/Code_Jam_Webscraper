#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int WorldCup2010(int P, vector <int> M, vector <int> prices)
{
	int ret = 0;
	for (int r = 0; r < P; r++) {
		for (int i = 0; i < 1 << r; i++) {
			int s = i * (1 << (P - r));
			int e = s + (1 << (P - r));
			int flag = false;
			for (int j = s; j < e; j++) {
				if (P - M[j] > 0) {
					for (int k = s; k < e; k++) {
						M[k]++;
					}
					ret++;
					break;
				}
			}
		}
	}
	return ret;
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int P;
		cin >> P;
		vector <int> M(1 << P);
		for (int i = 0; i < 1 << P; i++) {
			cin >> M[i];
		}
		vector <int> prices((1 << P) - 1);
		for (int i = 0; i < (1 << P) - 1; i++) {
			cin >> prices[i];
		}

		int ret = WorldCup2010(P, M, prices);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
