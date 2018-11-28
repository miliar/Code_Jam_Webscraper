#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

char str[100];
long long S,msk;
int nq;

void output(long long ans) {
	if(ans==0)return;
	output(ans>>1);
	if(ans&1)putchar('1');
	else putchar('0');
}

int main() {
	int T;
	scanf("%d",&T);
	for(int tc = 1;tc<=T;tc++) {
		printf("Case #%d: ",tc);
		scanf("%s",str);
		S = msk = 0;
		long long bt;
		for(int i = 0;str[i];i++) {
			S<<=1;
			msk<<=1;
			if(str[i]=='1')
				S |= 1;
			else
			if(str[i]=='?')
				msk |= 1;
		}
		nq = 0;
		long long ans = 0,cur,sq;
		for(bt = msk;bt>=0;bt = (bt - 1) & msk) {
			cur = bt ^ S;
			sq = (int)(sqrt(cur) + 1e-9);
			if(sq * sq==cur) {
				ans = cur;
				break;
			}
			if(bt==0)break;
		}
		output(ans);
		puts("");
	}
	return 0;
}
