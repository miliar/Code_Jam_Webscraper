#include <iostream>
#include <cmath>
using namespace std;
int hash[255];
int main()
{
	freopen("c:\ A-small.in", "r", stdin);
	freopen("c:\ A-small.out", "w", stdin);
	int t, cse = 1;
	int len, i;
	char str[70], ch;
	int ans[70];
	int sum, num;
	scanf("%d", &t);
	getchar();
	while (t--) {
		memset(hash, -1, sizeof(hash));
		gets(str);
		len = strlen(str);
		ch = str[0];
		hash[ch] = 1;
		num = 2;
		for (i = 1; i < len; i++) {
			ch = str[i];
			if (hash[ch] == -1) {
				hash[ch] = 0;
				ans[i] = 0;
				break;
			}
			ans[i] = 1;
		}
		ans[0] = 1;
		for (; i < len; i++) {
			ch = str[i];
			if (hash[ch] == -1)
			{
					hash[ch] = num++;
					ans[i] = hash[ch];
			} else {
				ans[i] = hash[ch];
			}
		}
		sum = 0;
		if (num == 1) {
			for (i = 0; i < len; i++) {
				sum += pow(2.0, i);
			}
		} else {
			for (int j = len - 1 , i = 0 ; i < len; i++) {
				sum += ans[i] * pow(num * 1.0, j--);				
			}
		}
		printf("Case #%d: %d\n",cse++, sum);
	}
 }