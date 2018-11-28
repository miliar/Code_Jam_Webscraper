#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <boost/foreach.hpp>

using namespace std;
using namespace boost;

char INPUT[60000];
int tmp[60000];
int K;

int main()
{
	int caseN;
	scanf("%d", &caseN);
	int *TMP = tmp+1;
	tmp[0] = -1;
	for(int cc=0; cc<caseN;cc++){
		scanf("%d", &K);
		scanf("%s", INPUT);
		int len = strlen(INPUT);
		int P[10];
		int ans = 100000000;
		for(int i=0;i<K;i++)
			P[i] = i;
		do{
			int count = 0;
			for(int i=0;i<len;i+=K){
				for(int j=0;j<K;j++){
					TMP[i+j] = INPUT[i + P[j]];
					if(TMP[i+j] != TMP[i+j-1]){
						count++;
					}
				}
			}
			if(ans > count)
				ans = count;
		}while(next_permutation( P, P + K));
		printf("Case #%d: %d\n", cc+1, ans);
	}
	return 0;
}
