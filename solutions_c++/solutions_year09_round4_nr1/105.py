#include<stdio.h>
#include<algorithm>
using namespace std;

int len[40];
int solve() {
	int N;
	scanf("%d", &N);
	for(int i=0;i<N;i++) {
		char str[64];
		scanf("%s", str);
		len[i]=0;
		for(int j=0;str[j];j++)
			if(str[j]=='1')
				len[i]=j;
	}

	int res=0;
	for(int i=0;i<N;i++) {
		int j;
		for(j=i;len[j]>i;j++);
		for(int k=j;k>i;k--) {
			swap(len[k-1], len[k]);
			res++;
		}
	}
	return res;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0;i<T;i++) {
		printf("Case #%d: %d\n", i+1, solve());
	}
}