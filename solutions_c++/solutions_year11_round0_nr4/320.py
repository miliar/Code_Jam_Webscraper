#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		int n;
		cin >> n;
		int count = 0;
		for(int j = 0; j < n; ++j) {
			int v;
			cin >> v;
			if(v != j+1) {
				++count;
			}
		}
		cout << "Case #" << (i+1) << ": " << fixed << setprecision(6) << 1.0*count << endl;
	}
	return 0;
}

