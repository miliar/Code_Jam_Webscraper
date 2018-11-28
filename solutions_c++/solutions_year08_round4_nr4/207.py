#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

#define INF 1000000000

using namespace std;

char str[1010];
char res[1010];
int perm[5];

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		int k, n;
		cin >> k;
		scanf("%s", str);
		n = strlen(str);
		for(int i = 0; i < k; ++i) perm[i] = i;
		int min_n = INF;
		do
		{
			for(int i = 0; i < n / k; ++i)
				for(int j = 0; j < k; ++j) res[i * k + j] = str[i * k + perm[j]];
			int num = 0;
			char pre = 0;
			for(int i = 0; i < n; ++i)
			{
				if(res[i] != pre) ++num;
				pre = res[i];
			}
			min_n = min(min_n, num);
		}while(next_permutation(perm, perm + k));
		printf("Case #%d: ", tt);
		printf("%d\n", min_n);
	}
	return 0;
}