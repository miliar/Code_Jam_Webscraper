// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; ++i) 
	{
		int rows(0), cols(0);
		cin >> rows >> cols;

		vector<vector<char> > a;
		a.resize(rows);
		for (int j = 0; j < rows; ++j) {
			a[j].resize(cols);
			for (int k = 0; k < cols; ++k)
				cin >> a[j][k];
		}

		for (int j = 0; j < rows-1; ++j) {
			for (int k = 0; k < cols-1; ++k) {
				if (a[j][k] == '#' && a[j][k+1] == '#' && a[j+1][k] == '#' && a[j+1][k+1] == '#') {
					a[j][k] = '/';
					a[j][k+1] = '\\';
					a[j+1][k] = '\\';
					a[j+1][k+1] = '/';
				}
			}
		}

		bool bp = true;
		for (int j = 0; j < rows; ++j)
			for (int k = 0; k < cols; ++k)
				if (a[j][k] == '#') {
					bp = false;
					break;
				}

		cout << "Case #" << i+1 << ":" << endl;

		if (bp)
		{
			for (int j = 0; j < rows; ++j) {
				for (int k = 0; k < cols; ++k)
					cout << a[j][k];
				cout << endl;
			}
		}
		else
			cout << "Impossible" << endl;
	}

	return 0;
}

