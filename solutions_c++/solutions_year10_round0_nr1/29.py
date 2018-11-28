#include <cstdio>

void testcase(int t) {
	int N,K;
	scanf("%d%d",&N,&K);
	K %= 1<<N;
	int mask = K%(1<<N);
	printf("Case #%d: %s\n",t,mask==(1<<N)-1 ? "ON" : "OFF");
}

int main() {
	int T;
	scanf("%d",&T);
	for(int i = 1;i <= T;++i)
		testcase(i);
}
