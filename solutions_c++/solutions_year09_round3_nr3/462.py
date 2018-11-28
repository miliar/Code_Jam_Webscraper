#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

const char input[] = "codejam33.in";
const char output[] = "codejam33.out";

int main()
{
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
	
	int n;
	scanf("%d", &n);
	
	int i;
	for(i = 1; i <= n; ++i)
	{
		int p, q;
		scanf("%d %d", &p, &q);
		int j;
		int *v = new int[q+1];
		for(j = 0; j < q; ++j)
			scanf("%d", &v[j]);
		
		int rez = 9999999;
		do
		{
			int *use = new int[p+1];
			for(j = 1; j <= p; ++j) use[j] = 0;
			int nr = 0;
			
			for(j = 0; j < q; ++j)
			{
				int k;
				for(k = v[j] - 1; k && !use[k]; --k) ++nr;
				for(k = v[j] + 1; k <= p && !use[k]; ++k) ++nr;
				use[v[j]] = 1;
			}
			
			if(nr < rez)  rez = nr;
		}
		while(next_permutation(v, v+q));
		printf("Case #%d: %d\n", i, rez);
	}
	return 0;
}
