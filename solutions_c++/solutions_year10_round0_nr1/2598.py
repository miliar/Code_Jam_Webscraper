#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int hasPower[32];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int g = 0; g < tests; g++){
		long long n,k;
		scanf("%lld %lld",&n,&k);
		/*vector<int> state(n);
		memset(hasPower,0,sizeof(int) * 32);
		hasPower[0] = 1;
		int j = 0;
		for (int i = 0; i < k; i++){			
			for (j = 0; j < n; j++)
				if (hasPower[j] == 1)
					state[j] ^= 1;
			memset(hasPower,0,sizeof(int) * 32);
			hasPower[0] = 1;
			for (j = 1; j < n; j++){
				if (state[j-1] == 0)
					break;
				else
					hasPower[j] = 1;
			}			
		}*/
		/*if (j == n && state[n-1] == 1)
				printf("Case #%d: ON\n",g+1);
			else
				printf("Case #%d: OFF\n",g+1);*/
		long long len;
		len = (long long)pow(2.,(double)n) - 1;
		/*string s = "a";
		char kur = 'b';
		for (int i = 1; i <= n; i++){
			s = s + kur + s;
			kur++;
		}*/
		
		k %= (len + 1);
		if (k == len)
			printf("Case #%d: ON\n",g+1);
		else
			printf("Case #%d: OFF\n",g+1);
	}
	return 0;
}