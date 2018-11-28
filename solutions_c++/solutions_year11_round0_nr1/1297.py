#include<stdio.h>
#include<queue>

int main() {
	int t,T,i,N,ans,a,b;
	char c;
	std::queue<int> A,B,S;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&N);
		for(i=1;i<=N;i++){
			scanf(" %c %d",&c,&a);
			if(c=='O') 	{A.push(a);S.push(0);}
			else 		{B.push(a);S.push(1);}
		}
		ans = 0;
		a = b = 1;
		while(!S.empty()) {
			ans++;
			if(S.front() == 0 && A.front() == a) {
				A.pop(); S.pop();
				if(!B.empty() && B.front() != b) b += (B.front() < b)?-1:1;
			} else if(S.front() == 1 && B.front() == b) {
				B.pop(); S.pop();
				if(!A.empty() && A.front() != a) a += (A.front() < a)?-1:1;
			} else {
				if(!A.empty() && A.front() != a) a += (A.front() < a)?-1:1;
				if(!B.empty() && B.front() != b) b += (B.front() < b)?-1:1;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
