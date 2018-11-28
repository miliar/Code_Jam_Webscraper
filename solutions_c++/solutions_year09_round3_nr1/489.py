#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define		DEBUG	1

int		CAS = 0, T;

char	num[100];
int		len;
long long 	base;
long long	ans;

int main()
{
	int		i, j, k;
	
	if (!DEBUG)
	{
		freopen("D:/round1/1.in", "r", stdin);
		freopen("D:/round1/1.out", "w", stdout);
	}

	scanf("%d", &T);	
	while (T--)
	{
		scanf("%s", num);
		len = strlen(num);
	
		set<char>	box;

		for (i=0; i<len; i++)
		{
			box.insert(num[i]);
		}
		base = box.size();
		if (base <= 1)	base = 2;

		int		cnt = 0;
		ans = 0;
		long long	dig;
		map<char, int>	getNum;
		
		for (i=0; i<len; i++)
		{
			if (i == 0)
			{
				getNum[num[i]] = 1;
			}
			else if (getNum.find(num[i]) == getNum.end())
			{
				if (cnt == 1)	cnt++;
				getNum[num[i]] = cnt;
				cnt++;				
			}

			ans = ans * base + (long long)getNum[num[i]];
		}
		printf("Case #%d: ", ++CAS);
		cout << ans << endl;
	}

	return 0;
}