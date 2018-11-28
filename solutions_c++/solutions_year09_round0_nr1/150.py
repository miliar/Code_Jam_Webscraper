#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int l, d, n;
	cin >> l >> d >> n;

	ofstream dictf("dict"), patf("pat");

	for (int c = 0; c < d; ++c)
	{
		string s;
		cin >> s;
		dictf << s << endl;
	}

	for (int c = 0; c < n; ++c)
	{
		string s;
		cin >> s;
		patf << s << endl;
	}

	return 0;
}
