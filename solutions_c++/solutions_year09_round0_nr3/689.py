#include <cstdio>
#include <cstring>

char s[] = "welcome to code jam";
char buf[1000000];
const int R = 10000;

int main() {
	int z;
	gets(buf), sscanf(buf,"%d",&z);
	for (int Zz=1;Zz<=z;Zz++) {
		gets(buf);
		int dp[19];
		int ans = 0;
		memset(dp,0,sizeof(dp));
		for (int i=0;buf[i];i++) {
			for (int r=0;s[r];r++) {
				if (buf[i]==s[r])
					if (r==0)
						dp[r]++, dp[r]%=R;
					else if(dp[r-1]!=-1)
						dp[r] += dp[r-1], dp[r]%=R;
			}
		}
		printf("Case #%d: %04d\n", Zz, dp[18]);
	}
	return 0;
}
