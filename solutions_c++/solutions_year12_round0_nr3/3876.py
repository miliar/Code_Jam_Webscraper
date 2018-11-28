#include <iostream>
#include <cstdio>

int main()
{
	int m[8] = {1,10,100,1000,10000,100000,1000000,10000000};
	int flag[10];
	int t,a,b,sum,dig,flagsum;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	for (int i = 0;i < t;i++)
	{
		sum = 0;
		scanf("%d %d",&a,&b);
		int temp = a;
		dig = 0;
		while (temp > 0)
		{	
			temp = temp / 10;
			dig++;
		}
		for (int j = a;j <= b;j++)
		{
			temp = j;
			flagsum = 0;
			for (int k = 0;k < dig - 1;k++)
			{	
				
				temp = (temp % 10) * m[dig - 1] + temp / 10;
				if ((a <= temp) && (temp <= b) && (temp > j))
				{	
					bool op = false;
					for (int l = 0;l < flagsum;l++)
						if (temp == flag[l])
							op = true;
					if (!op)
					{	
						flag[flagsum++] = temp;
						sum++;
					}
				}
			}

		}
		printf("Case #%d: %d\n",i + 1,sum);

	}
	return 0;
}
