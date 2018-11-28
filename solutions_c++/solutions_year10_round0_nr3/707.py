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

int ncase, nnode;
long x[1000], R, K;
long tsum[1000];

int next[1000];
int last[1000];
long long acc[3000];

int main()
{
	

	scanf("%d", &ncase);

	for(int idx = 1; idx <= ncase; idx++){
		scanf("%ld %ld %d", &R, &K, &nnode);

		for(int i = 0; i < nnode; i++){
			scanf("%ld", &x[i]);
		}


		long sum = x[0];
		int j = 1 % nnode;
		for(int i = 0; i < nnode; i++){

			if(i && i == j){
				sum = x[i];
				j++;
				j %= nnode;
			}

			while(sum + x[j] <= K && j - i){
				sum += x[j];
				j++;
				j %= nnode;
			}

			next[i] = j;
			tsum[i] = sum;


			sum -= x[i];

			//printf("next(%d) = %d, sum = %ld\n", i, j, tsum[i]);
		}


		long long ret = 0;

		for(int i = 0; i < nnode; i++){
			last[i] = -1;
		}

		long i = 0;
		int cur = 0, found = 0;
		while(i < R){
			if(last[cur] < 0 || found){
				ret += tsum[cur];

				last[cur] = i;
				cur = next[cur];
				if(!found) acc[i] = ret;
				i++;
			}
			else{
				found = 1;

				ret += tsum[cur];

				long idiff = i - last[cur];
				long long adiff = ret - acc[last[cur]];
				long m = MAX(0, (R - i - 1) / idiff);
				i += (m * idiff);
				ret += (adiff * m);
				ret -= tsum[cur];

			}
		}

		printf("Case #%d: %lld\n", idx, ret);

	}
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */
