#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

int sign[45];
char str[45];
int l;
//bool ugly(char *str, int n)
//{
//	if((str[n - 1] - '0') % 2 == 0)
//		return true;
//	if((str[n - 1] - '0') % 5 == 0)
//		return true;
//	int sum = 0;
//	for(int i = 0; i < n; i++)
//		sum += str[i] - '0';
//	if(sum % 3 == 0)
//		return true;
//	
//	return false;
//}

//bool ugly(char *str, int n)
//{
//	return true;
//}

__int64 compute()
{
	__int64 ans = 0;
	__int64 before = 0;
	int beforesign = 1;
	char buf[45];
	int i;
	before = str[0] - '0';
	for(i = 1; i < l; i++)
	{
		if(sign[i - 1] == 0)
		{
			before = before * 10 + str[i] - '0';
		}
		else
		{
			if(beforesign == 1)
				ans = ans + before;
			else
				ans = ans - before;
			beforesign = sign[i - 1];
			before = str[i] - '0';
		}
	}
	if(beforesign == 1)
		ans = ans + before;
	else
		ans = ans - before;
	return ans;
}

int main()
{
	int numCase;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, k;

	__int64 sum;

	scanf("%d", &numCase);
	gets(str);
	for(int cases = 0; cases < numCase; cases++)
	{
		gets(str);
		l = strlen(str);
		sum = 0;
		memset(sign, 0, sizeof(sign));
		
		while(1)
		{

			__int64 ans;
			if(l == 1)
				ans = str[0] - '0';
			else
				ans = compute();
			if(ans % 2 == 0 || ans % 3 == 0 || ans % 5 == 0 || ans % 7 == 0)
				sum++;
			i = l - 2;
			while(i >= 0)
			{
				sign[i]++;
				if(sign[i] <= 2)
					break;
				sign[i] = 0;
				i--;
			}
			if(i < 0)
				break;
		}

		cout << "Case #" << cases + 1 << ": " << sum << endl;
	}

	return 0;
}