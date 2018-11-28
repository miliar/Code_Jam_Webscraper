#include <iostream>
#include <algorithm>
using namespace std;

char num[65];
bool mark[256];
int main()
{
	int tcase, j;
	freopen("a2.txt", "r", stdin);
	freopen("ao.txt", "w", stdout);
	long long n;
	scanf("%d", &tcase);
	for(int i = 1; i <= tcase; i++)
	{
		scanf("%s", num);
		memset(mark, false, sizeof(mark));
		int len = strlen(num);
		for(int j = 0; j < len; j++)
			mark[num[j]] = true;
		int b = 0;
		for( j = 0; j <= 'z'; j++)
			if(mark[j]) b++;
		if(b == 1) b+= 1;
		char t[65];
		strcpy(t, num);
		int base[256];
		memset(base, -1, sizeof(base));
		int st = 0;
		base[t[0]] = 1;
		j = 1;
		while(t[j] == t[j-1] && j < len) j++;
		base[t[j]] = 0;
		st = 1;
		for(; j < len; j++)
		{
			if(base[t[j]] != -1) continue;
			else {
				st++;
				base[t[j]] = st;
			}
		}
		n = 0;
		for( j = 0; j < len; j++)
		{
			n *= b;
			n += base[t[j]];
		}
		printf("Case #%d: %lld\n",i,  n);
	}
}
