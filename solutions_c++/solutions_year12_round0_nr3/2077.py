// Google CodeJAM 2012
// Author: Syed Ghulam Akbar

#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NONSTDC_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

int main() {
	int C;
	char source_lin[500];

	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	scanf("%d",&C);
	string input, output;
	char number[20] ;

	for (int test=1;test<=C;test++) {
		long A, B, next, num;
		long count = 0;

		cin >> A >> B;

		for (long i=A; i<=B; i++)
		{
			long start = num = i;
            int numdigits = (int) log10((double)start); // would return numdigits - 1
            int multiplier = (int) pow(10.0, (double)numdigits);
           
			// Roate the number
            while(multiplier > 1)
            {
				long r = num % 10;
				num = num / 10;

				num = num + multiplier * r;

				if (num > i && num <= B)
					count++;

				if(num == start)
					break;
            }
		}

		// Set the answer depending on the found state
		cout << "Case #" << test << ": " << count << endl;
	}

	fclose( out );
}