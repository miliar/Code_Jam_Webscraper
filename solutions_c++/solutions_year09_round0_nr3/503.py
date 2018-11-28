/**********************************************************************
Author: littlekid@whu
Created Time:  2009-9-3 15:04:07
File Name: 
Description: 
**********************************************************************/
#include <iostream>
#include <cctype>
#include <cstring>
using namespace std;

const char STD_STR[] = "welcome to code jam";
const int LEN = 19;

int main() 
{
	int N;
	int ans = 0, len = 0;
	char word[1000];
	int f[1000];
	freopen("F:\\ACM\\gcj2009\\QR\\c.in", "r", stdin);
	freopen("F:\\ACM\\gcj2009\\QR\\c.out", "w", stdout);
	scanf("%d\n", &N);
	for (int ca = 1; ca <= N; ++ca) {
		ans = 0; len = 0;
		char ch;
		while (true) {
			scanf("%c", &ch);
			if (ch == '\n') break;
			word[ len++ ] = ch;
		}
		word[len] = '\0';
//		cout << word << endl;///
		
		memset(f, 0, sizeof(f));
		for (int pos = 0; pos < len; ++pos) {
			if (word[pos] == STD_STR[0]) {
				f[pos] = 1;
			}	
		}
		for (int ix = 1; ix < LEN; ++ix) {
			for (int pos = len-1; pos >= 0; --pos) {
				f[pos] = 0;
				if (word[pos] != STD_STR[ix]) {
					continue;
				}
				for (int i = 0; i < pos; ++i) {
					f[pos] += f[i];
					if (f[pos] > 10000) f[pos] %= 10000;	
				}
			}
		}
		for (int pos = 0; pos < len; ++pos) {
			ans += f[pos];
			ans %= 10000;	
		}
		printf("Case #%d: %04d\n", ca, ans);	
	}
    return 0;
}

