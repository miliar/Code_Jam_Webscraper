#include <iostream>
#include <cmath>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <iomanip>

using namespace std;

int main ()
{
	int i;
//	int s ;
	cin >> i;
	for (int j = 1; j <= i; j ++)	{
		long long n, k, s;
		cin >> n >> k;
		cout << "Case #" << j << ": ";
		if (k == 0)	cout << "OFF" << endl;
		else	{
			s = pow(2, n);
			if ((k + 1) % s == 0)	cout << "ON" << endl;
			else	cout << "OFF" << endl;
		}
	}
	return 0;
}
//	n	f	f		f
//	f	n	f		f
//	n	n	f		f
//	f	f	n		f
//	n	f	n		f
//	f	n	n		f
//	n	n	n		n
