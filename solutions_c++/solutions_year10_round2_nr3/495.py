#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define IFILE "D:\\jam\\A.in"
#define OFILE "D:\\jam\\A.out"
#define BASE 100003

__int64 bin[600][600];

__int64 strange[600][600];

__int64 binc(__int64 k, __int64 n) {
	if (bin[k][n] != -1)
		return bin[k][n];
	else {
		if (k > n)
			return 0;
		if (k < 0)
			return 0;
		if ((k == 0) || (k == n)) return 1;
			__int64 result = (binc(k-1,n-1) + binc(k,n-1)) % BASE;
		bin[k][n] = result;
		return result;
	}
}

__int64 stra(__int64 n, __int64 count) {
	if (count >= n) return 0;
	if (count == 1) return 1;
	if (strange[n][count] != -1)
		return strange[n][count];
	else {
		__int64 result = 0;
		for (__int64 j = 1; j < count; j ++) {
			result = (result + stra(count, j) * binc(count-j-1,n-count-1) ) % BASE;
		}
		strange[n][count] = result;
		return result;
	}
}

int main() {
	__int64 T;
	__int64 n;
	ifstream input;
	ofstream output;
	input.open(IFILE);
	output.open(OFILE);

	for (__int64 i = 0; i < 600; i++)
		for (__int64 j = 0; j < 600; j++)
			strange[i][j] = bin[i][j] = -1;
	input >> T;

	for (__int64 i = 1; i <= T; i++) {
		input >> n;
		__int64 sum = 0;
		for (__int64 j = 1; j < n; j++)
			sum = (sum + stra(n,j)) % BASE;
		output << "Case #" << i << ": " << sum << endl;
	}


	input.close();
	output.close();
	
	return 0;
}
