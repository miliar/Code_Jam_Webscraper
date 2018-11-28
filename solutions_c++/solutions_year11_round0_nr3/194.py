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

int x[1000][20];

int nnode;

int sum[20];

int s[2][20];

long ss[2];

long data[20];

long ret;

int main()
{

	int ncase;

	scanf("%d", &ncase);

	for(int case_idx = 1; case_idx <= ncase; case_idx++){

		memset(x, 0, sizeof(x));
		memset(sum, 0, sizeof(sum));

		scanf("%d", &nnode);

		for(int i = 0; i < nnode; i++){
			long a;
			scanf("%ld", &a);

			data[i] = a;

			for(int j = 0; a; j++){

				x[i][j] = a & 1;

				sum[j] += x[i][j];
				a >>= 1;
			}
		}

		for(int i = 0; i < 20; i++){
			if(sum[i] & 1){
				printf("Case #%d: NO\n", case_idx);
				goto end;
			}
		}

		ret = 0;

		long nstate = (long)1 << nnode;

		for(long i = 1; i < nstate - 1; i++){

			memset(s, 0, sizeof(s));
			memset(ss, 0, sizeof(ss));

			long j = i;

			for(int pos = 0; j; pos++){
				int idx = j & 1;
				j >>= 1;

				for(int k = 0; k < 20; k++){
					s[idx][k] += x[pos][k];

				}

				ss[idx] += data[pos];
			}

			for(int k = 0; k < 20; k++){
				if((s[0][k] + s[1][k]) & 1)
					goto bad;
			}

			ret = MAX(ret, MAX(ss[0], ss[1]));

bad:
			;
		}

		printf("Case #%d: %ld\n", case_idx, ret);
end:
		;
	}
	
	return 0;
}

// vi: ts=2 sw=2
