#include <stdio.h>
#include <string.h>

int N;

char str[501];
int size;
const char needle[] = "welcome to code jam\0"; // 19
#define L 19

int memo[20][501];

// n needle
// s str
int f(int n, int s)
{
	if (n == L) return 1;
    if (memo[n][s] != -1) return memo[n][s];
    //putchar('.');
    int ret = 0;

	for(int i = s; i < size; i++) {
        if (needle[n] == str[i]) {
            //putchar(needle[n]);
            ret += f(n + 1, i + 1);
            ret %= 10000;
        }
    }
    memo[n][s] = ret;
    return ret;
}

int main()
{
    char c;
	scanf("%d\n", &N);

	for(int i = 1; i <= N; i++) {
		int j = 0;
		while((c = getchar()) != '\n')
			str[j++] = c;
		str[j] = '\0';
		size = j;

        memset(memo, -1, sizeof memo);
		printf("Case #%d: %04d\n", i, f(0, 0));
        //printf("\n%s\n%s\n", needle, str);
	}

	return 0;
}

