#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main() {
	int t, n, arr[100], v1, v2, v3, tmp, MAX;
	ifstream fin("input_c.txt");
	ofstream fout("ans_c.txt");
	
	fin >> t;
	for (int x = 1; x <= t; x++) {
		fin >> n;
		for (int i = 0; i < n; i++)
			fin >> arr[i];
		int no = (int)(pow(2, n+0.0) + 0.5);
		MAX = -1;
		for (int i = 0; i < no; i++) {
			v1 = v2 = v3 = 0;
			for (int j = 0; j < n; j++) {
				tmp = (i / (int)(pow(2, j+0.0) + 0.5)) % 2;
//				fout << tmp;
				if (tmp)
					v1 = v1 ^ arr[j];
				else {
					v2 = v2 + arr[j];
					v3 = v3 ^ arr[j];
				}
			}
			if (v1 == v3 && v1 != 0 && v2 > MAX)
				MAX = v2;
//			fout << ' ' << v1 << ' ' << v2 << ' ' << v3 << endl;
		}
		fout << "Case #" << x << ": ";
		if (MAX == -1)
			fout << "NO\n";
		else
			fout << MAX << "\n";
	}
}
