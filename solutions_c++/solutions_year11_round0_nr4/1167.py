#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i=0;i<t;i++) {
		int n;
		int bpos = 1, opos = 1;
		int btime = 0, otime = 0;
		cin >> n;

		vector<int> array;
		vector<int> array2;
		for (int j=0;j<n;j++) {
			int d;
			cin >> d;
			array.push_back(d);
			array2.push_back(d);
		}
		std::sort(array2.begin(),array2.end());
		int p = 0;
		for (int j=0;j<n;j++) {
			if (array[j] != array2[j]) p++;
		}


		cout << "Case #" << (i+1) << ": " << p << ".000000" << endl;

	
	}

	return 0;
}
