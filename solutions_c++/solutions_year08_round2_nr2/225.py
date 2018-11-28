#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

vector<int> primes;

int factorize(int num, int *factors) {
	int nfactors = 0;
	for (int i = 2; i*i <= num; i++) {
		if (num % i == 0) {
			factors[nfactors] = i;
			while (num % i == 0) {
				num /= i;
			}
			nfactors++;
		}
	}
	if (num > 1) {
		factors[nfactors] = num;
	}
	else nfactors--;
	return nfactors;
}


int nums[1005][1005];
int cnt[1005];
int color[1005];

void merge(int A, int B) {
	int mergeto = color[A];
	int mergefrom = color[B];
	for(int i = 0; i < 1005; ++i) {
		if(color[i] == color[B]) color[i] = color[A];
	}
	return;
}


int main(void) {
	int T;
	int C = 1;
	int res = 0;
	int A, B, P;
	scanf("%d", &T);
	while(T--) {
		memset(nums, 0, sizeof(int) * 1005 * 1005);
		memset(cnt, 0, sizeof(int) * 1005);
		res = 0;
		for(int i = 0; i < 1005; ++i) {
			color[i] = i;
		}		
		scanf("%d%d%d", &A, &B, &P);
		for(int i = A; i <= B; ++i) {
			cnt[i] = factorize(i, nums[i]);
		}
		for(int i = A; i <= B; ++i) {
			for(int j = A+1; j <= B; ++j) {
				if(color[i] == color[j]) continue;
				for(int k = 0; k <= cnt[i]; ++k) {
					if(j % nums[i][k] == 0 && nums[i][k] >= P) {
						//cout << "merging " << i << " " << j << " prime = " << nums[i][k] << endl;
						merge(i,j);
						break;
					}
				}
			}
		}
		for(int i = A; i <= B; ++i) {
			if(color[i] == i) res++;
		}
		printf("Case #%d: %d\n", C++, res);	
	}	
	return 0;
}
