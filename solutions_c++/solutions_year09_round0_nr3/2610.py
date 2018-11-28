#include <cstdio>
#include <cstring>

char const *pattern = "welcome to code jam";

int calc(char *str, int len)
{
     int f[19], i, j;
     memset(f, 0, sizeof(f));
     for (i = 0; i < len; ++i) {
	  if (str[i] == 'w')
	       ++f[0];
	  for (j = 1; j < 19; ++j) { // 19 is the length of the pattern
	       if (str[i] == pattern[j])
		    f[j] = (f[j] + f[j-1]) % 10000;
	  }
     }
     
     return f[18];
}

int main()
{
     int n, i, ans;
     scanf("%d\n", &n);
     char str[501];
     for (i = 1; i <= n; ++i) {
	  scanf("%[^\n\r]\n", str);
	  ans = calc(str, strlen(str));
	  printf("Case #%d: %04d\n", i, ans);
     }
     
     return 0;
}
