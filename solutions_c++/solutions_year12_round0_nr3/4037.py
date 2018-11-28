#include<cstdio>
#include<cmath>
#include<iostream>
using namespace std;

int A,B;
int recycle(int a)
{
    int num = a, i;
    int dig = 0;
    while(num > 0)
    {
	num /= 10;
	dig++;
    }
    int count = 0;
    int rem = 0;
    int div = 0;
    int power = 1;
    for(i = 0;i < dig-1; i++, power++)
    {
	int p = pow(10, power);
	rem = a%p;
	div = a/p;
	num = rem*pow(10,(dig-power))+div;


	if(a == num)
	    break;
	if(num > a && num >= A && num <=B)
	    count++;
    }
    return count;
}

int main()
{
    int t;
    scanf("%d", &t);
    int j = 1;
    while(t--)
    {
	scanf("%d%d", &A, &B);
	int count = 0;
	for(int i = A; i < B; i++)
	{
	    count += recycle(i);
	}
	printf("Case #%d: %d\n", j, count);
	j++;
    }
    return 0;
}
