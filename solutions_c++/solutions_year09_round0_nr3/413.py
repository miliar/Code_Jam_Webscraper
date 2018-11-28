#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int N;
char pat[] = "welcome to code jam";
int patlen = 19;
char cnt[505];
int ans[505][25];
int len;
int main() {
   int i, j, Case = 1, k;
   scanf("%d", &N);
   while (getchar() != '\n');
   while (N --) {
      fgets(cnt, 502, stdin);
      len = strlen(cnt);
      len --;
      cnt[len] = 0;
      for (i = 0; i < len; i ++)
	 for (j = 0; j < patlen; j ++)
	    if (pat[j] != cnt[i])
	       ans[i][j] = 0;
	    else
	       if (j == 0)
		  ans[i][j] = 1;
	       else {
		  ans[i][j] = 0;
		  for (k = 0; k < i; k ++)
		     ans[i][j] += ans[k][j - 1];
		  ans[i][j] %= 10000;
	       }
      int ret = 0;
      for (i = 0; i < len; i ++)
	 ret += ans[i][patlen - 1];
      ret %= 10000;
      printf("Case #%d: ", Case ++);
      if (ret < 1000)
	 printf("0");
      if (ret < 100)
	 printf("0");
      if (ret < 10)
	 printf("0");
      printf("%d\n", ret);
   }
   return 0;
}

