#include<stdio.h>
#include<string.h>

int main() {
	const char ptn[]="Xwelcome to code jam";
	int N, len=strlen(ptn)-1;
	scanf("%d\n", &N);
	for(int i=1;i<=N;i++) {
		int cnt[24];
		memset(cnt, 0, sizeof(cnt));
		cnt[0]=1;
		char str[512];
		gets(str);
		for(int j=0;str[j];j++)
			for(int k=len;k>0;k--)
				if(str[j]==ptn[k])
					cnt[k]=(cnt[k]+cnt[k-1])%10000;
		printf("Case #%d: %04d\n", i, cnt[len]);
	}
}