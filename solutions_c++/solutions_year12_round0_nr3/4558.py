#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int sumof(int);
bool order(int, int);
bool order2(int, int);

int main()
{
	int input;
	int num1[50],num2[50];
	int results[50];
	bool r3;
	scanf("%d", &input);
	for(int i = 0; i<input; i++)
	{
		scanf("%d", &num1[i]);
		scanf("%d", &num2[i]);
		results[i] = 0;
	}
	for(int  i = 0; i<input; i++)
	{
		//printf("Hello1");
		while(num1[i] < num2[i])
		{
			//printf("Hello");
			int temp = num2[i];
			for(true ;num2[i]>num1[i]; num2[i]--)
			{
				//printf("Hello");
				int r1 = sumof(num1[i]);
				int r2 = sumof(num2[i]);
				if(num1[i]/100 <=0)
				{
					r3 = order2(num1[i], num2[i]);
				}
				else
				{
					r3 = order(num1[i], num2[i]);
				}
				if((r1==r2) && r3)
				{
					results[i]++; 
				}
			}
			num1[i]++;
			num2[i] = temp;
		}
	}
	for(int i = 0 ; i<input; i++)
	{
		printf("Case #%d: %d\n", i+1, results[i]);
	}
}

int sumof(int a)
{
	int res = 0;
	while(a > 0)
	{
		//printf("Hello");
		int r6 = a%10;
		res += r6;
		a = a/10;
	}
	return res;
}

bool order(int a, int b)
{
	int temp = a;
	int temp2 = (((a%100) * 10) + (a/100));
	if(temp2 == b)
		return true;
	else
	{
		while( temp2 != a)
		{
			int temp3 = temp2 ;
			temp2 = (((temp3%100) * 10) + temp3/100);
			if(temp2 == b)
				return true;
		}
	}
	return false;
}

bool order2(int a, int b)
{
	int temp = a;
	int temp2 = (((a%10) * 10) + (a/10));
	if(temp2 == b)
		return true;
	else
	{
		while( temp2 != a)
		{
			int temp3 = temp2;
			temp2 = (((temp3%10) * 10) + temp3/10);
			if(temp2 == b)
				return true;
		}
	}
	return false;
}
