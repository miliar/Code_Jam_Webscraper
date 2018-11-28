#include <stdio.h>
#define swap(x,y) {int t=x;x=y;y=t;}

const int T = 100;
const int A = 1000000;
const int B = 1000000;

int check(int, int);

main()
{
	int t, a1, a2, b1, b2;
	int ans;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		ans=0;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		for (int j=a1;j<=a2;j++)
			for (int k=b1;k<=b2;k++)
				if (check(j,k))
					ans++;
		printf("Case #%d: %d\n", i, ans);
	}
}

int check(int a, int b)
{
	if (a<b)
		swap(a,b)
	
	if (b==0)
		return 1;
	if (!check(a%b,b))
		return 1;
	if (a%b+b!=a && !check(a%b+b,b))
		return 1;
	return 0;
}
