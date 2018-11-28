#include <iostream>
#include <string>
#include "BigIntegerLibrary.hh"

using namespace std;

BigInteger find_gcd(BigInteger a, BigInteger b)
{
	BigInteger rem;
	if (a ==0) {
		return b;
	} else if (b == 0){
		return a;
	}

	if (a < b) {
		if (b % a == 0) return a;
		return find_gcd(a, b % a);
	} else {
		if (a % b == 0) return b;
		return find_gcd(a % b, b);
	}
}

BigInteger inBigInteger()
{
	string input;
	cin >> input;
	return stringToBigInteger(input);
}

int main()
{
	BigInteger ti, ti_1, gcd, answer, temp;
	unsigned int C, N, i, j;
	try {
		cin >> C;
		for (j = 0; j < C; j++) {
			cin >> N;
			ti_1 = inBigInteger();
			ti = inBigInteger();
			gcd = (ti > ti_1) ? (ti - ti_1) : (ti_1 - ti);
			ti_1 = ti;
			for (i = 2; i < N; i++) {
				ti = inBigInteger();
				gcd = find_gcd(gcd, (ti > ti_1) ? (ti - ti_1) : (ti_1 - ti));
				ti_1 = ti;
			}
			if(gcd == 0)
			{
				answer = 0;
			}
			else {
				temp = ti % gcd;
				if (temp == 0) {
					answer = 0;
				} else {
					answer = gcd - temp;
				}
			}
			cout << "Case #" << j + 1 << ": " << bigIntegerToString(answer) << ((j == C - 1) ? "" : "\n");
		}
	}
	catch(const char *a)
	{
		cout << endl << "Exception" << a << "\n" << bigIntegerToString(gcd) << endl << ti << endl << ti_1;
	}
	return 0;
}
