#include <iostream>
#include <math.h>
using namespace std;
__int64 hash[130], anum[130];
char num[130];
int mmax;
int main ()
{
	int test, len, cas = 1;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf ("%d", &test);
	while (test --){
		
		memset(hash, -1, sizeof (hash));
		memset(anum, 0, sizeof (anum));
		scanf ("%s", num);
		len = strlen(num);
		anum[0] = 1;
		hash[num[0]] = 1;
		mmax = 1;
		__int64 k = 0;
		for (int i = 1; num[i]; i ++){
			if (hash[num[i]] != -1){
				anum[i] = hash[num[i]];
				if (hash[num[i]] > mmax)
					mmax = hash[num[i]];
			}
			else{
				if(k == 1)
					k = 2;
				anum[i] = k;
				hash[num[i]] = k;
				if (k > mmax)
					mmax = k;
				k ++;
			}
		}
		__int64 ans = 0;
		__int64 m = mmax + 1;
		for (int i = len - 1, j = 0; i >= 0; i --, j ++){
			ans += (__int64)pow ((double)m, j) * anum[i];
		}
		printf("Case #%d: %I64d\n", cas ++ , ans);
	}
}