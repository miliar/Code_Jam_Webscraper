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

using namespace std;

long ncase, idx, N, K;

int main()
{
	scanf("%ld", &ncase);

	for(idx = 1; idx <= ncase; idx++){

		scanf("%ld %ld", &N, &K);

		printf("Case #%ld: ", idx);
		long t = 1 << N;

		if(K % t == t - 1){
			printf("ON\n");
		}
		else
			printf("OFF\n");
	}

	
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */
