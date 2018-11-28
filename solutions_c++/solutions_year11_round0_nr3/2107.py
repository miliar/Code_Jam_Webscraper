#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream inf("inputC.txt");
	ofstream outf("outputC.txt");
	int t;
	inf >> t;
	for (int i = 1; i <= t; i++) {
		int n;
		inf >> n;
		int sum = 0;
		int min;
		int xor = 0;
		inf >> min;
		sum += min;
		xor ^= min;
		for (int j = 1; j < n; j++) {
			int a;
			inf >> a;
			sum += a;
			min = min > a ? a : min;
			xor ^= a;
		}
		cout << "Sum = " << sum << " \t";
		cout << "Min = " << min << " \t";
		cout << "Xor = " << xor << " \t";
		outf << "Case #" << i << ": ";
		cout << (xor == 0 ? sum-min : -1) << endl;
		if (xor == 0)
			outf << sum - min << endl;
		else 
			outf << "NO" << endl;
	}

	inf.close();
	outf.close();

	return 0;
}