#include<stdio.h>
#include<algorithm>
using namespace std;

int solve() {
	int N, p[2], t[2], time=0;
	scanf("%d", &N);
	p[0]=p[1]=1;
	t[0]=t[1]=0;
	for(int i=0;i<N;i++) {
		char color[2];
		int button;
		scanf("%s%d", color, &button);
		int id=color[0]=='B';
		time=max(t[id]+abs(p[id]-button), time)+1;
		t[id]=time;
		p[id]=button;
	}
	return time;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		printf("Case #%d: %d\n", cas, solve());
	}
}