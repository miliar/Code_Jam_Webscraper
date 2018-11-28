#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

#define cin fin
#define cout fout

long long n, k;
long long two[31];

int main()
{
	two[0] = 1;
	for (int i = 1; i < 31; i++)
		two[i] = two[i-1] * 2;

	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n >> k;

		cout << "Case #" << i+1 << ": ";

		if ((k+1) % two[n] == 0) cout << "ON";
		else cout << "OFF";

		cout << endl;
	}

	return 0;
}