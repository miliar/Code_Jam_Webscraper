#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

int main()
{
	// freopen("b_small.in", "r", stdin);
	// freopen("b_small.out", "w", stdout);
	ifstream fin("b_small.in");
	ofstream fout("b_small.out");
	int test_case;
	cin >> test_case;
	for (int tc=1; tc<=test_case; ++tc) {
		string number;
		cin >> number;
		string orig = number;
		string max = "9999999";
		do {
			if (number > orig && number < max) {
				max = number;
			}
		} while (next_permutation(number.begin(), number.end()));
		if (max == "9999999") {
			sort(orig.begin(), orig.end());
			int i=0;
			while (orig[i] == '0') ++i;
			swap(orig[0], orig[i]);
			max = "";
			max += orig.substr(0, 1) + "0";
			sort(orig.begin() + 1, orig.end());
			max += orig.substr(1, orig.length());
		}
		fout << "Case #" << tc << ": " << max << endl;
		cout << "Case #" << tc << ": " << max << endl;
		
	}

	return 0;
}