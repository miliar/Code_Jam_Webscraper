#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int cnt[20];

void Compute()
{
	memset(cnt, 0, sizeof(cnt));
	string str;
	getline(cin, str);
	int len = str.length();
	for(int i=len-1; i>-1; i--)
	{
		switch(str[i])
		{
		case 'm':
			cnt[19]++;
			cnt[6] = (cnt[6] + cnt[7]) % 10000;
			break;
		case 'a':
			cnt[18] = (cnt[18] + cnt[19]) % 10000;
			break;
		case 'j':
			cnt[17] = (cnt[17] + cnt[18]) % 10000;
			break;
		case ' ':
			cnt[16] = (cnt[16] + cnt[17]) % 10000;
			cnt[11] = (cnt[11] + cnt[12]) % 10000;
			cnt[8] = (cnt[8] + cnt[9])  % 10000;
			break;
		case 'e':
			cnt[15] = (cnt[15] + cnt[16]) % 10000;
			cnt[7] = (cnt[7] + cnt[8]) % 10000;
			cnt[2] = (cnt[2] + cnt[3]) % 10000;
			break;
		case 'd':
			cnt[14] = (cnt[14] + cnt[15]) % 10000;
			break;
		case 'o':
			cnt[5] = (cnt[5] + cnt[6]) % 10000;
			cnt[10] = (cnt[10] + cnt[11]) % 10000;
			cnt[13] = (cnt[13] + cnt[14]) % 10000;
			break;
		case 'c':
			cnt[4] = (cnt[4] + cnt[5]) % 10000;
			cnt[12] = (cnt[12] + cnt[13]) % 10000;
			break;
		case 't':
			cnt[9] = (cnt[9] + cnt[10]) % 10000;
			break;
		case 'l':
			cnt[3] = (cnt[3] + cnt[4]) % 10000;
			break;
		case 'w':
			cnt[1] = (cnt[1] + cnt[2]) % 10000;
			break;
		}
	}
}

int main() 
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    int cases;
	scanf("%d\n", &cases);
	int i;
	for(i=1; i<=cases; i++)
	{
		Compute();
		printf("Case #%d: %04d\n", i, cnt[1]);
	}
	return 0;
}