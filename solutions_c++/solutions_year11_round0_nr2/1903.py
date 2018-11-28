#include<stdio.h>
#include<stdlib.h>
int C,D,N;
char str[200];
char combine[26][30];
char oppose[26][30];
int oppoN[26];
int count[26];
char stack[200];
int stackN;
int main(){
	int T;
	int t1,t2;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		for(int i=0;i<26;i++){
			for(int j=0;j<26;j++){
				combine[i][j] = -1;
				oppose[i][j] = 0;
			}
			count[i] = 0;
			oppoN[i] = 0;
		}
		scanf("%d",&C);
		for(int i=0;i<C;i++){
			scanf("%s",str);
			combine[str[0] - 'A'][str[1] - 'A'] = str[2] - 'A';
			combine[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++){
			scanf("%s",str);
			t1 = str[0] - 'A';
			t2 = str[1] - 'A';
			oppose[t1][oppoN[t1]] = t2;
			oppose[t2][oppoN[t2]] = t1;
			oppoN[t1]++;
			oppoN[t2]++;
		}
		stackN = 0;
		scanf("%d",&N);
		scanf("%s",str);
		stackN = 0;
		int now = 0;
		int pre;
		int com;
		for(int i=0;i<N;i++){
			now = str[i] - 'A';
			stack[stackN] = now;
			stackN++;
			count[now]++;

			while(1){
				if(stackN == 1){
					break;
				}
				now = stack[stackN - 1];
				pre = stack[stackN - 2];
				com = combine[pre][now];
				if(com != -1){
					count[com]++;
					stackN--;
					stack[stackN-1] = com;
					count[now]--;
					count[pre]--;
					continue;
				}
				now = stack[stackN - 1];
				for(int j=0;j<oppoN[now];j++){
					if(count[oppose[now][j]] != 0){
						for(int k=0;k<26;k++)count[k] = 0;
						stackN = 0;
						break;
					}else{
						continue;
					}
				}
				break;
			}
		}
		printf("Case #%d: [",t + 1);
		for(int i=0;i<stackN;i++){
			if(i != 0)printf(", ");
			printf("%c",stack[i] + 'A');
		}
		printf("]\n");
	}
	return 0;
}
