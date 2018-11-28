#include <stdio.h>

int combinations(int A, int B)
{
	int digit, i, j, k, no = 0;
	if(B<10) return 0;
	else if(B<100) digit = 2;
	else if(B<1000) digit = 3;
	else if(B<10000) digit = 4;
	else if(B<100000) digit = 5;
	else if(B<1000000) digit = 6;
	else if(B<10000000) digit = 7;
	if(digit == 2)
	{
		for(i=((int)A/10 > 0) ? (int)A/10 : 1; i<10; i++)
		{
			for(j=i; j<=10; j++)
			{
				if(10*i+j >= 10*j+i) continue;
				if(10*i+j>=A && 10*j+i<=B) no++;
				if(10*j+1>B) break;
			}
		}
		return no;
	}
	for(i=0; i<digit; i++)
	{
		for(i=((int)A/100 > 0) ? (int)A/100 : 1; i<10; i++)
		{
			for(j=0; j<10; j++)
			{
				for(k=1; k<=(int)B/100; k++)
				{
					if(100*i+10*j+k >= 100*k+10*i+j) continue;
					if(100*i+10*j+k>=A && 100*k+10*i+j<=B) no++;
					if(100*k+10*i+j>B) continue;
				}
			}
		}

		for(i=((int)A/100 > 0) ? (int)A/100 : 1; i<10; i++)
		{
			for(j=1; j<10; j++)
			{
				for(k=0; k<10; k++)
				{
					if(100*i+10*j+k >= 100*j+10*k+i) continue;
					if(100*i+10*j+k>=A && 100*j+10*k+i<=B) no++;
					if(100*j+10*k+i>B) continue;
				}
			}
		}
		return no;
	}
}

int main()
{
	int T, A, B, i, j;
	scanf("%d", &T);
	for(i=0; i<T; i++)
	{
		scanf("%d %d", &A, &B);
		printf("Case #%d: %d\n", i+1, combinations(A, B));
	}
}