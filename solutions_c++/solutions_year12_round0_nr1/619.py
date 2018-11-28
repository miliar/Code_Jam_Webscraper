/*
 * Author: Fish@UESTC_Oblivion
 * Created Time:  2012/04/14 09:31:52
 * Project: 
 *    Type: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 105;
char mp[27] = "yhesocvxduiglbkrztnwjpfmaq";
char s[MaxN];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 1;
	
	scanf("%d", &T);
	gets(s);
	while (T--) {
		printf("Case #%d: ", cas++);
		gets(s);
		for (int i = 0; s[i]; i++) {
			if (s[i] != ' ') {
				putchar(mp[s[i] - 'a']);
			} else {
				putchar(' ');
			}
		}
		putchar('\n');
	}
	
	return 0;
}
