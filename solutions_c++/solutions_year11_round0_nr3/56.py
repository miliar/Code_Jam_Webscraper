#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

fstream in, out;

int t, n;

int candy[1000];

int compare(const void*a, const void *b)
{
	return *(int*)b - *(int*)a;
}

int main() {
	in.open("probc.in", fstream::in);
	out.open("probc.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		in >> n;
		
		for (int j = 0; j < n; j++) {
			in >> candy[j];
		}
		qsort(candy, n, sizeof(int), compare);

		int asdf = 0;
		for (int k = 0; k < n; k++) {
			asdf = asdf ^ candy[k];
		}
		bool ispossible = true;
		for (int l = 0; l < 20; l++) {
			if (asdf % 2 == 1) {
				ispossible = false;
			} else {
				asdf /= 2;
			}
		}

		if (!ispossible) {
			out << "Case #" << i + 1 << ": NO" << endl;
		} else {
			int ans = 0;
			for (int x = 0; x < n - 1; x++) {
				ans += candy[x];
			}
			out << "Case #" << i + 1 << ": " << ans << endl;
		}
	}
    
	in.close();
	out.close();

	return 0;
}
