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

int main()
{
	int ncase, N, j;
	scanf("%d", &ncase);

	for(int case_idx = 1; case_idx <= ncase; case_idx++){
		scanf("%d", &N);

		double ret = 0;

		for(int i = 0; i < N; i++){
			scanf("%d", &j);
			j--;
			if(j - i)	ret++;
		}

		printf("Case #%d: %lf\n", case_idx, ret);
	}
	
	return 0;
}

// vi: ts=2 sw=2
