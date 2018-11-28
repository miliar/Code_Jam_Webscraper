//Aleksander "kaalex" Kramarz

#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; k++)
	{
		int n, s=0, v, x=0, m=1000000000;
		scanf("%d", &n);
		while(n--)
		{
			scanf("%d", &v);
			if(v<m)
				m=v;
			x^=v;
			s+=v;
		}
		printf("Case #%d: ", k);
		x?printf("NO\n"):printf("%d\n", s-m);
	}
}
