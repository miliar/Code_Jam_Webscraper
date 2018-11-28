#include <fstream>

using namespace std;

ifstream fin ("input.txt");
ofstream fout("output.txt");

#define MAX 1010

int t;
int n;
int a[MAX];

int main() {
	fin >> t;

	for (int tCount = 0; tCount < t; ++tCount) {
	        fout << "Case #" << tCount+1 << ": ";
		
		fin >> n;

		int minEl = 1000000000;
		int sum = 0;

		for (int i = 0; i < n; ++i) {
			fin >> a[i];
			if (a[i] < minEl)
				minEl = a[i];
			sum = sum ^ a[i];
		}


		if (sum == 0) {
			for (int i = 0; i < n; ++i)
				sum += a[i];
			sum -= minEl;
			fout << sum << endl;
		}
		else {
			fout << "NO" << endl;
		}
	}		
	
	return 0;
}