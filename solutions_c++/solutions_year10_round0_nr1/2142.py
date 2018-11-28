#include <iostream>
#include <cmath>

using namespace std;
long long dpTable[30];

void fillTable()	{

	for (int i = 0; i < 30; i++)
		dpTable[i] = (long long) pow(2, i + 1);
	
}

void solve(long long nin, long long kin, int testNum)	{

	bool result;
	double k = kin;

	double temp = (k + 1) / dpTable[nin - 1];
	long long blah = (long long) temp;

	long long power = dpTable[nin - 1];
	power *= blah;

	result = (power == (kin + 1));
	
	cout << "Case #" << testNum << ": " << (result ? "ON" : "OFF") << endl;
}

int main()	{

	long long t;
	cin >> t;

	fillTable();
	
	for (int i = 0; i < t; i++)	{

		long long n,k;

		cin >> n >> k;

		solve(n, k, i + 1);
	}
}