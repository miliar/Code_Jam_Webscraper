/*
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
*/
#include <stdio.h>
char com[36][5], opp[28][5], dat[102];
char stack[102];
int head;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int C, D, N, T;
	scanf("%d",&T);
	while(T-->0){
		int i, j, k;
		scanf("%d",&C);
		for(i=0;i<C;i++) scanf("%s",com[i]);
		scanf("%d",&D);
		for(i=0;i<D;i++) scanf("%s",opp[i]);
		scanf("%d",&N);
		scanf("%s", dat);
		head = 0;
		char x, y;
		for(i=0;i<N;i++){
			stack[head ++] = dat[i];
			if(head >= 2){
				x = stack[head - 1];
				y = stack[head - 2];
				for(j=0;j<C;j++){
					if(x == com[j][0] && y == com[j][1]
					|| y == com[j][0] && x == com[j][1]){
						head -= 2;
						stack[head ++] = com[j][2];
					}
				}
			}
			{
				int i, j, k;
				for(i=0;i<head;i++){
					for(j=i+1;j<head;j++){
						for(k=0;k<D;k++){
							if(stack[i] == opp[k][0] && stack[j] == opp[k][1]
							|| stack[j] == opp[k][0] && stack[i] == opp[k][1]){
								head = 0;
							}
						}
					}
				}
			}
		}

		static int cs = 1;
		printf("Case #%d: [", cs++);
		bool first = true;
		for(i=0;i<head;i++){
			if(!first) printf(", ");
			printf("%c", stack[i]);
			first = false;
		}
		printf("]\n");
	}
	return 0;
}