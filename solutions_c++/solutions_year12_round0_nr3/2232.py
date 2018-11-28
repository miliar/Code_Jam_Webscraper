#include <fstream>
#include <istream>
#include <iostream>
#include <assert.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <set>
#include <math.h>

#define ARRAY_SIZE(array)        ((int)(sizeof(array) / sizeof((array)[0])))

using namespace std;


int rotate(int num, int ndigits, int shift)
{
//	if (shift == 0 || (num % 10 == 0))
//		return num;

	int ret;
	int factor = pow(10, shift);

	int multi = num / factor;
	int mod = num % factor;

	ret = mod * pow(10, (ndigits - shift)) + multi;

	return ret;
}

int resolve(int A, int B)
{
	int ndigits = 0;
	char str[18];
	int ret = 0;

	snprintf(str, ARRAY_SIZE(str), "%d", A);

	ndigits = strlen(str);


//	printf("pair: ");
	for (int n = A; n <= B; n++)
	{
		int m = n;
		std::set<int> recycled;

		for (int j = 0; j < ndigits; j++)
		{
			m = rotate(n, ndigits, j);
			if (m <= n || m > B)
				continue;

			if (recycled.find(m) != recycled.end())
			{
				continue;
			}

			recycled.insert(m);
//			printf("%d < %d, ", n, m);
			ret++;
		}
	}

//	printf("\n");
	return ret;
}


void test_rotate(int n, int ndigits)
{
	int m = 0;

	printf("%d: ", n);
	for (int j = 0; j < ndigits; j++)
	{
		m = rotate(n, ndigits, j);
		printf("%d, ", m);
	}

	printf("\n");
	return;
}


int main(int argc, char *argv[])
{
//	test_rotate(123456789, 9);
//	test_rotate(1000, 4);
//	test_rotate(1001, 4);
//	test_rotate(1010, 4);
//	test_rotate(1100, 4);
//	test_rotate(1110, 4);
//	exit(0);

	assert(argc == 2);

	ifstream ifs(argv[1], ifstream::in);

	int nline = 0;
	char line[1024];

	ifs.getline(line, sizeof(line) / sizeof(line[0]));

	nline = strtol(line, NULL, 10);

//	printf("%d\n", nline);

	for (int i = 1; i <= nline; i++)
	{

		int A = 0;
		int B = 0;

		// read input
		ifs >> A;
		ifs >> B;

		ifs.getline(line, sizeof(line) / sizeof(line[0]));

//		printf("%d %d\n", A, B);

		assert(A <= B);
		assert(1 <= A);
		assert(1 <= B);

		// resolve the case
		int result = resolve(A, B);

		printf("Case #%d: %d\n", i, result);
	}

	return 0;
}
