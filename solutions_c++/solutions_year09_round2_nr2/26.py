#include<iostream>
using namespace std;

char str[1000];

int N;

int spc() {
	for(int i=N-1;i>0;--i)
		if(str[i-1]<str[i]) return false;
	return true;
}

int cnt[20];

int run() {
	scanf("%s", str);
	N=strlen(str);
	if(spc()) {
		int p = 999;
		str[p] = 100;
		for(int i=0;i<N;++i)
			if(str[i]>'0' && str[i] < str[p]) {
				p = i;
			}
		putchar(str[p]);
		str[p] = '0';
		sort(str,str+N);
		puts(str);
		return 1;
	}
	
	memset(cnt,0,sizeof(cnt));
	for(int i=0;i<N;++i)
		cnt[str[i]-'0'] ++;
	int i;
	for(i=N-1;i>0;--i)
		if(str[i-1]<str[i]) break;
	int j;
	for(int p=0;p<i-1;++p) putchar(str[p]), --cnt[str[p]-'0'];
	for(j=str[i-1]-'0'+1;!cnt[j];++j);
	putchar('0'+j);
	cnt[j] --;
	for(int p=0;p<10;++p)
		while(cnt[p]>0) putchar('0'+p), cnt[p]--;
	puts("");
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int test; scanf("%d", &test);
	for(int no=1;no<=test;++no) {
		printf("Case #%d: ",no);
		run();
	}
}
