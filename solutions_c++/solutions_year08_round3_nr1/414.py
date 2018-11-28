//============================================================================
// Name        : simple_template.cpp
// Author      : aza
// Version     :
// Copyright   : Your copyright notice
//============================================================================


#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

#include <gmp.h>


using namespace std;

int n;

vector<int> data;


int main()
{
	unsigned int numCase;
	cin >> numCase;
	unsigned long i;
	for (i = 0; i < numCase; i++)
	{
		int P, K, L;
		long long res = 0;
		int z;

		cin >> P >> K >> L;

		data.clear();
		for (z = 0; z < L; z++) {
			int a;
			cin >> a;
			data.push_back(a);
		}

		sort(data.begin(), data.end(), greater<int>());

		int key, place;
		key = 1;
		place = 1;
		bool impossible = false;

		for (z = 0; z < L ; z++) {
			res += place * data[z];

			if (z == (L-1))
				break;

			key++;
			if (key > K) {
				place++;
				key = 1;
				if (place > P) {
					impossible = true;
					break;
				}
			}

		}
		if (impossible) {
			printf("Case #%i: Impossible\r\n", (i+1));
		} else {
			printf("Case #%i: %lli\r\n", (i+1), res);
		}
	}
	return 0;
}
