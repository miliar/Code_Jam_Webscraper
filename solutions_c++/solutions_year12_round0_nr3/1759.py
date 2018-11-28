#include<cstdio>

int T,A,B,ans;

int main()
{
	scanf("%d",&T);
	for(int I = 1;I <= T;I++)
	{
		scanf("%d%d",&A,&B);
		ans = 0;
		for(int i = A;i <= B;i++)
		{
			int t = i;
			int p = 1;
			while(p <= t) p *= 10;
			p /= 10;
			do
			{
				int a = t % 10;
				t /= 10;
				t += a*p;
				if (a && t <= B && t > i) ans++;
			} while(t != i);
		}
		printf("Case #%d: %d\n",I,ans);
	}
	return 0;
}
