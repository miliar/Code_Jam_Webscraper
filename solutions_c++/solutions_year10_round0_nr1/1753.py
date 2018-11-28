#include <stdio.h>
#include <string.h>

#define ON 1
#define OFF 0

int n, k;

int table[] = {1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071,262143,524287,1048575,2097151,4194303,8388607,16777215,33554431,67108863,134217727,268435455,536870911,1073741823};


int solve()
{
	int num = table[n-1];
	int index = ( k - num ) / ( num + 1 ) + 1;
	int an;
	do 
	{
		an = num + (num + 1) * (index - 1);
		index++;
	} while (an < k);

	if(an == k)
		return ON;

	return OFF;

}
int main()
{
	int t, case_num, res;
	scanf("%d", &t);
	for(case_num = 1; case_num <= t; case_num++)
	{
		scanf("%d%d", &n, &k);
		res = solve();
		printf("Case #%d: %s\n", case_num, res == ON ? "ON" : "OFF");
	}
	return 0;
}

