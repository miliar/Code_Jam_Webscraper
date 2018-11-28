#include <stdio.h>
#include <string.h>

int n,ss,p;
int S[35], NS[35];
int s[210];
bool used[210];
void Build() {
	S[0] = -1;	NS[0] = 0;
	S[1] = -1;	NS[1] = 1;
	S[29] = -1;	NS[29] = 10;
	S[30] = -1;	NS[30] = 10;
	for(int i=2;i<=28;++i) {
		int x = i%3;
		if( x == 0 ) {
			NS[i] = int(i/3);
			S[i] = int(i/3)+1;
		} else if(x == 1) {
			NS[i] = int(i/3)+1;
			S[i] = int(i/3)+1;
		} else {
			NS[i] = int(i/3)+1;
			S[i] = int(i/3)+2;
		}
	}
	
	/*for(int i=0;i<=30;++i)
		printf("%d %d\n",S[i],NS[i]);*/
		
}

int main() {
	int t, cases=0;
	Build();
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d%d%d",&n,&ss,&p);
		for(int i=0;i<n;++i)
			scanf("%d", s+i);
		memset(used, 0, sizeof(used));
		int sum = 0;
		for(int i=0;i<n;++i) {
			if(NS[s[i]] >= p) {
				++sum;
			} else if( ss > 0 && S[s[i]] >= p ) {
				++sum;
				--ss;
			}
		}
		printf("Case #%d: %d\n",++cases,sum);
	}
	
	return 0;
}
