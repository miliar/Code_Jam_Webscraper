#include <cstdio>
#include<string.h>
#include<stdlib.h>
#include<cmath>
#include<algorithm>
using namespace std;

#define DEBUG 0

int len, pt;
char digits[40];

int des(void)
{
	for(int i = len - 2; i >= 0; i--)
		if(digits[i] < digits[i + 1])
			return i;
	return -1;
}

int compare (const void * a, const void * b)
{
  return ( *(char*)a - *(char*)b );
}

int bigger(void)
{
	char d = '9';
	int qt;

	for(int i = pt + 1; i < len; i++)
		if(digits[i] > digits[pt] && digits[i] <= d)
		{
			d = digits[i];
			qt = i;
		}
	return qt;
}



void solve(void)
{
	if(pt == -1)
	{
		qsort(digits, len, sizeof(char), compare);
		if(digits[0] == '0')
		{
			int qt = 1;
			while(digits[qt] == '0')
				qt++;

			char tmp = digits[0];
			digits[0] = digits[qt];
			digits[qt] = tmp;
		}

		for(int i = len - 1; i >= 1; i--)
			digits[i + 1] = digits[i];
		digits[1] = '0';
		digits[len + 1] = '\0';
		len++;
	}
	else
	{
		int qt = bigger();
		char tmp = digits[pt];
		digits[pt] = digits[qt];
		digits[qt] = tmp;

		qsort(digits + pt + 1, len - pt - 1, sizeof(char), compare);
	}
}

int main()
{
	//freopen("B-small.in","r",stdin);
	freopen("B-large.in","r",stdin);

#if !DEBUG
	freopen ("B-large.out","w",stdout);
#endif

	int cases;

	scanf("%d\n", &cases);

	for(int i=1;i<=cases;i++)
	{
		scanf("%s\n", digits);
		len = strlen(digits);
		pt = des();
		solve();




		printf("Case #%d: %s\n", i, digits);

	
	}
	

#if !DEBUG
	fclose (stdout);
#endif

	return 0;
}