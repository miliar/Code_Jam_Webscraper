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

long long x[1000];
long long d[1000];

long long GCD(long long a, long long b){

	if(a < b)	SWAP(a, b);

	//a >= b
	while(b){
		a %= b;

		SWAP(a, b);

	}

	return a;
}


int main()
{
	int ncase;

	scanf("%d", &ncase);

	for(int i = 1; i <= ncase; i++){

		int nnode;

		scanf("%d", &nnode);

		int ndiff = 0;
		for(int j = 0; j < nnode; j++){
			scanf("%lld", &x[j]);

			if(j && x[j] - x[j - 1]){
				d[ndiff++] = ABS(x[j] - x[j - 1]);
				//printf("diff: %lld\n" ,d[ndiff - 1]);
			}
		}

		long long G = d[0];

		for(int j = 1; j < ndiff; j++){

			G = GCD(G, d[j]);
		}
		//printf("G = %lld\n", G);

		long long ret = (G - x[0] % G) % G;

		printf("Case #%d: %lld\n", i, ret);


	}

	
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */
