#include <cstdio>
#include <cmath>

#define max(a,b) (((a)>(b))?(a):(b))

int main()
{
	freopen("inp.txt", "r", stdin);
	freopen("outp.txt", "w", stdout);
	int n,t;
	int x[111];
	char s[111][11];
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		scanf("%d", &n);
		int o=1, b=1;
		int res=0;
		char pc = 0;
		int temp = 0, val;
		for (int j=0;j<n;j++)
		{
			scanf("%s%d", s[j], &x[j]);			
			if (s[j][0]=='O')
			{
				if (s[j][0] != pc)
					val = max(abs(x[j]-o)-temp, 0);
				else
					val = abs(x[j]-o);
				o=x[j];
			}
			else if (s[j][0]=='B')
			{
				if (s[j][0] != pc)
					val = max(abs(x[j]-b)-temp, 0);
				else
					val = abs(x[j]-b);
				b=x[j];
			}
			if (s[j][0] != pc)
				temp = 0;
			temp += val+1;
			res += val+1;				
			pc = s[j][0];
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}