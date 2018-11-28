#include <stdio.h>
#include <queue>
using namespace std;
queue <int> Q;
queue <int> Q1;
queue <int> Q2;
int main() {
	int N, K, a, i, j, t;
	char c;
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	scanf("%d", &N);
	for(i=0;i<N;i++) {
		scanf("%d", &K);
		for(j=0;j<K;j++) {
			scanf(" %c ", &c);	
			scanf("%d", &a);
			if(c=='O') {Q1.push(a); Q.push(0);}
			else {Q2.push(a); Q.push(1);}			
		}
		t = 0;
		int p1 = 1, p2 = 1;
		while(!Q.empty()) {
			int f = 0;
			if(!Q1.empty()) {
				if(Q1.front()>p1) p1++;
				else if(Q1.front()<p1) p1--;
				else if(Q.front()==0) {
					Q1.pop();f = 1;
				}
			}
			if(!Q2.empty()) {
				if(Q2.front()>p2) p2++;
				else if(Q2.front()<p2) p2--;
				else if(Q.front()==1) {
					Q2.pop();f = 1;
				}
			}
			if(f==1)Q.pop();
			t++;
		}
		printf("Case #%d: %d\n", i+1, t);
	}
	return 0;	
}
