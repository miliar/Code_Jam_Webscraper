#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

bool v1compare(long long a, long long b) {
	return a < b;
}

bool v2compare(long long a, long long b) {
	return b < a;
}

int main()
{
	int T, N;
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	vector<long long> v1;
	vector<long long> v2;
	fin >> T;

	for (int i = 0; i < T; i++) {
		v1.clear();
		v2.clear();

		fin >> N;
		
		for (int j = 0; j < N; j++) {
			int vi;
			fin >> vi;
			v1.push_back(vi);
		}

		for (int j = 0; j < N; j++) {
			int vi;
			fin >> vi;
			v2.push_back(vi);
		}

		sort(v1.begin(), v1.end(), v1compare);
		sort(v2.begin(), v2.end(), v2compare);

		long long product = 0;
		for (int j = 0; j < N; j++) {
			product += (v1[j] * v2[j]);
		}

		fout << "Case #" << i+1 << ": " << product;
		if (i != T-1)
			fout << endl;
	}
	return 0;
}