#include <cstdio>
#include <cstring>
using namespace std;

#define MAXL 512

int dp[32][MAXL], L;
char in[MAXL], w[20] = "welcome to code jam";

int calc(int p, int s) {
	int i, r;

   if (p == 19) return 1;
	else if (dp[p][s] == -1) {
		r = 0;
      for (i=s; i<L; i++) {
		   if (in[i] == w[p]) {
			   r = (r+calc(p+1, i+1))%10000;
			}
		}
		dp[p][s] = r;
	}
   return dp[p][s];
}

int main() {

int N, n;

scanf("%d\n", &N);

for (n=1; n<=N; n++) {

gets(in); L = strlen(in);

memset(dp, -1, sizeof(dp));
printf("Case #%d: ", n);
if (calc(0,0) < 10) printf("0");
if (calc(0,0) < 100) printf("0");
if (calc(0,0) < 1000) printf("0");
printf("%d\n", calc(0,0));

}

return 0;
}
