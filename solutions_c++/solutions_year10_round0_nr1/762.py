#include<stdio.h>
#include<math.h>

int main()
{
	freopen("C:\\Towhid G\\Codes\\Codejam 2010\\Qualifications\\A-small-attempt1.in", "rt", stdin);
	freopen("C:\\Towhid G\\Codes\\Codejam 2010\\Qualifications\\A-small.out", "wt", stdout);
	int inp, kase, n, k;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &k);
		n = pow(2.0, n) - 1;
		printf("Case #%d: ", kase);
		if(k >= n && k % 2)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}
