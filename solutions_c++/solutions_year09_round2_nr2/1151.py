#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>

using namespace std;

int main()
{
//	freopen("b-small-attempt3.in", "rt", stdin);
//	freopen("b-small.out", "wt", stdout);

	freopen("b-large.in", "rt", stdin);
	freopen("b-large.out", "wt", stdout);
	char ns[25];
	int inp, kase, n, i;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%s", ns);
/*		i = 0;
		while(n)
		{
			ns[i++] = n % 10;
			n /= 10;
		}
*/
		int tot = strlen(ns);
/*		for(i = 0; i < tot / 2; i++)
		{
			int temp = ns[i];
			ns[i] = ns[tot - i - 1];
			ns[tot - i - 1] = temp;
		}
		*/
		printf("Case #%d: ", kase);
		if(next_permutation(ns, ns + tot))
		{
			for(i = 0; i < tot; i++)
			{
				printf("%c", ns[i]);
			}
		}
		else
		{
			sort(ns, ns + tot);
			int cnt = 0;
			while(ns[cnt] == '0')
				cnt++;
			printf("%c0", ns[cnt]);
			for(i = 0; i < cnt; i++)
			{
				printf("0");
			}
			for(i = cnt + 1; i < tot; i++)
			{
				printf("%c", ns[i]);
			}	
		}
		printf("\n");
	}
	return 0;
}
