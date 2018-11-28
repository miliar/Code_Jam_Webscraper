#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

char term[8];

int xs[2], ts[2];

int main()
{

	int ncase;

	scanf("%d", &ncase);

	map<string, int> itable;

	itable["O"] = 0;
	itable["B"] = 1;

	for(int test_idx = 1; test_idx <= ncase; test_idx++){

		int N, x;

		scanf("%d", &N);
		
		xs[0] = xs[1] = 0;
		ts[0] = ts[1] = 0;

		int t = 0;

		for(int i = 0; i < N; i++){

			scanf("%s", term);
			scanf("%d", &x);

			int idx = itable[string(term)];

			t = MAX(t + 1, ABS(x - xs[idx]) + ts[idx] + 1);

			xs[idx] = x;
			ts[idx] = t;

		}


		printf("Case #%d: %d\n", test_idx, t - 1);

	}
	
	return 0;
}

// vi: ts=2 sw=2
