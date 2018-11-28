#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <set>
using namespace std;

#define		DEBUG	0

int		CAS = 0, T;
int		num;
int		digits[10], len;
int		cur[10], clen;
FILE	*in, *out;

int		next()
{
	memset(digits, 0, sizeof(digits));
	int n = num;

	while (n)
	{
		digits[n % 10]++;
		n /= 10;
	}

	for (int i=num+1; ;i++)
	{
		n = i;
		memset(cur, 0, sizeof(cur));
		while (n)
		{
			cur[n % 10]++;
			n /= 10;
		}
		bool		flag = true;
		for (int j=1; j<10; j++)
			if (cur[j] != digits[j])
			{
				flag =false;
				break;
			}
		if (flag)	return i;
	}
}

int main()
{
	int		i, j, k;
	

	in = (DEBUG) ? stdin : fopen("D:/round1/2.in", "rt");
	out =(DEBUG) ? stdout : fopen("D:/round1/2.out", "wt");

	fscanf(in, "%d", &T);
	while (T--)
	{
		fscanf(in, "%d", &num);
		//fprintf(out, "Case #%d: ", ++CAS);
		int		ans = next();
		fprintf(out, "Case #%d: %d\n", ++CAS, ans);
	}

	return 0;
}