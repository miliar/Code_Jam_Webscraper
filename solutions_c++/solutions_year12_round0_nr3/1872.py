#include <stdio.h>

int pow[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int array[10];

int bits(int a)
{
	int i=0;
	while (a)
	{
		a/=10;
		++i;
	}
	return i;
}

int move(int a, int bits)
{
	int i = a%10;
	
	a /= 10;
	a += i*pow[bits-1];
	return a;
}

int main()
{
	int n;
	int a, b, count, countchong;
	int a_bit, b_bit;
	int i, j, k ,l ,m, ii;
	int min, max;
	
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d", &n);
	for (i = 1; i <= n; ++i)
	{
		count = 0;
		scanf("%d%d", &a, &b);
		a_bit = bits(a);
		b_bit = bits(b);
		for (j = a_bit; j <= b_bit; ++j)
		{
			min = (a > pow[j-1])?a:pow[j-1];
			max = (b < (pow[j]-1))?b:(pow[j]-1);
			for (k = min; k <= max; ++k)
			{
				l = k;
				array[0] = 0;
				for (m = 1; m < j; ++m)
				{
					l = move(l,j);
					if (l>=min && l<=max && l!=k)
					{
						for (ii = 1; ii <= array[0]; ++ii)
						{
							if (l==array[ii])
							  break;
						}
						if (ii>array[0])
						{
						  ++count;
							array[++array[0]] = l;
						}
				  }	
				}
			}
		}
		printf("Case #%d: %d\n", i, count/2);
	}
	return 0;
}
