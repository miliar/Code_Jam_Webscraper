#include <iostream>
#include <gmpxx.h>
#include <vector>

using namespace std;

mpz_class get_gcd(mpz_class l, mpz_class r)
{
	while((l = (l % r)) != 0)
		swap(l, r);
	return r;
}

int main(int argc, char *argv[])
{
	int count = 0;
	cin >> count;
	mpz_class gcd, last, temp;
	for(int i = 0; i != count; ++i)
	{
		int entries = 0;
		cin >> entries >> last;
		for(int j = 1; j != entries; ++j)
		{
			cin >> temp;
			if(last - temp != 0)
			{
				if(gcd == 0)
					gcd = abs(last - temp);
				else
					gcd = get_gcd(gcd, abs(last - temp));
				last = temp;
			}
		}
		cout << "Case #" << (i + 1) << ": " << gcd - ((last - 1) % gcd) - 1;
		cout << endl;
		gcd = 0;
	}
	return 0;
}
