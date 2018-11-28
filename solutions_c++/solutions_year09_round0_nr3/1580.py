// welcome.cpp --  Thu Sep 03 2009
// http://code.google.com/codejam/contest/dashboard?c=90101#s=p2
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MODULUS 10000
#define MAX_LINE_LEN 500

const char *str_patn = "welcome to code jam";
const int len_patn = 19;

char buf[MAX_LINE_LEN+1];
int cnt[len_patn][MAX_LINE_LEN];

int main(int argc, char *argv[]) {
	int nt;
	gets(buf);
	sscanf(buf, " %d", &nt);
	for(int nti = 0; nti < nt; ++nti) {
		gets(buf); // My old friend gets ;-)
		int cols = (int)strlen(buf);

		memset(cnt, 0, sizeof(cnt));

		{
			// Special case for first row
			char ch = str_patn[0];
			cnt[0][0] = (ch == buf[0]);
			for(int c = 1; c < cols; ++c) {
				cnt[0][c] = (cnt[0][c-1] + (ch == buf[c]))%MODULUS;
			}
		}
		
		for(int r = 1; r < len_patn; ++r) {
			char ch = str_patn[r];
			cnt[r][0] = 0;
			for(int c = 1; c < cols; ++c) {
				cnt[r][c] = (cnt[r][c-1] + (ch == buf[c] ? cnt[r-1][c-1] : 0))%MODULUS;
			}
		}

		// Output
		printf("Case #%d: %04d\n", nti+1, cnt[len_patn-1][cols-1]);
		
	}	
	return 0;
}

