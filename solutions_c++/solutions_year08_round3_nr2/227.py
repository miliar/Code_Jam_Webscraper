/*
	Probelm :: B
	Microsoft VS 2005
*/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef __int64 i64;

const int MAX = 45;

char num[MAX];
int num3[MAX];

void convert(int n, int len)
{
	memset(num3, 0, sizeof(num3));

	int i, j, k, temp;
	
	i = 0;

	while(n)
	{
		num3[i++] = n%3;
		n = n/3;
	}

	for(j=0, k=len-1; j<len/2; j++, k--)
	{
		temp = num3[k];
		num3[k] = num3[j];
		num3[j] = temp;
	}

	return;
}


i64 calculate(char *str)
{
	int len = strlen(str);
	int end = (int)pow(3.0, (double)(len-1));

	int i, j, prev = 1;
	i64 temp, val = 0;
	i64 res = 0;

	for(i=0; i<end; i++)
	{
		convert(i, len-1);
		
		prev = 1;
		val = 0;
		temp = str[0] - '0';

		for(j=0; j<len-1; j++)
		{
			if(num3[j] == 1)
			{
				if(prev == 1)
				{
					val = val + temp;
					prev = 1;
					temp = str[j+1] - '0';
				}

				else if(prev == 2)
				{
					val = val - temp;
					prev = 1;
					temp = str[j+1] - '0';
				}
			}

			else if(num3[j] == 2)
			{
				if(prev == 1)
				{
					val = val + temp;
					prev = 2;
					temp = str[j+1] - '0';
				}

				else if(prev == 2)
				{
					val = val - temp;
					prev = 2;
					temp = str[j+1] - '0';
				}
			}

			else // if(num3[j] == 0)
				temp = temp * 10 + (str[j+1] - '0');
		}

		if(prev == 1)
		{
			val = val + temp;
			prev = 2;
			temp = 0;
		}

		else if(prev == 2)
		{
			val = val - temp;
			prev = 2;
			temp = 0;
		}

		if(val%2 == 0 || val%3 == 0 || val%5 == 0 || val%7 == 0)
			res++;
	}

	return res;
}

int main(void)
{
	// freopen("..//..//B-small.in", "rt", stdin);
	// freopen("..//..//B-small.out", "wt", stdout);


	int test, t;
	i64 res;

	scanf( " %d" ,&test);

	for(t=1; t<=test; t++)
	{
		scanf( " %s" ,num);

		res = calculate(num);
	
		printf("Case #%d: %I64d\n" ,t ,res);
	}

	return 0;
}