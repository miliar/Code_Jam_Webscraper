#include <iostream>
#include "stdio.h"
using namespace std;

//#define DBGOUT printf
 void DBGOUT(...) { } 

char digits[128] = "";
int	nDigits = 0;

int getDigitValue(char c)
{
	for (int i = 0; i< nDigits; i++)
	{
		if (digits[i] == c)
			return i;
	}
}

long long getValue(char* lbuf)
{
	int base = 0;
	long long  value = 0;

	nDigits=0;
	memset(digits, 0, 128);

	digits[0] = lbuf[0];
	nDigits++;
	for (int i = 1; i < strlen(lbuf); i++)
	{
		if (strchr(digits, lbuf[i]) == 0)
		{
			digits[nDigits++] = lbuf[i];
		}
	}

	DBGOUT("digits:%s\n", digits);
	DBGOUT("ndigits:%d\n", nDigits);

	base = nDigits;
	if (base == 1)
	{
		digits[1] = '0';
		base = nDigits = 2;
	}

	if (nDigits > 1)
	{
		// swap 0, 1 digits
		char t = digits[0];
		digits[0] = digits[1];
		digits[1] = t;
	}


	DBGOUT("digits:%s\n", digits);
	DBGOUT("base=%d\n", base);
	value = 0;

	for (int i = 0; i < strlen(lbuf); i++)
	{
		value *= base;
		value += getDigitValue(lbuf[i]);
		DBGOUT("%c=%d v=%d\n", lbuf[i], getDigitValue(lbuf[i]),value);
	}

	return value;
}


int main()
{
	int case_cnt;
	char lbuf[128];
	long long ret;

	scanf("%d", &case_cnt);

	for (int i = 0; i < case_cnt; i++)
	{
		scanf("%s", lbuf);

		DBGOUT("read[%s]\n", lbuf);
		if (strlen(lbuf) == 1)
			ret = 1;
		else
			ret = getValue(lbuf);

		cout << "Case #" << i + 1 << ": " << ret << endl;
	}
}

