#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;

uint64_t gcd(uint64_t a, uint64_t b)
{
	while (b)
	{
		uint64_t t = b;
		b = a % b;
		a = t;
	}
	return a;
}

void fairwarning(int n, const vector<uint64_t> &t)
{
	uint64_t d = t[1] > t[0] ? t[1] - t[0] : t[0] - t[1];
	for(int i = 2; i < n; i++)
	{
		d = gcd(d, t[i] > t[i - 1] ? t[i] - t[i - 1] : t[i - 1] - t[i]);
	}
	uint64_t r = t[0] % d;
	if (!r)
		cout << "0" << endl;
	else
		cout << (d - r) << endl;
}

int main()
{
	int c;
	cin >> c;
	if (!cin) return -1;
	
	for (int i = 0; i < c; i++)
	{
		int n;
		cin >> n;
		if (!cin) return -1;
		vector<uint64_t> t(n, 0);
		
		for (int j = 0; j < n; j++)
			cin >> t[j];
		if (!cin) return -1;

		cout << "Case #" << (i + 1) << ": " << flush;
		fairwarning(n, t);
	}
}
