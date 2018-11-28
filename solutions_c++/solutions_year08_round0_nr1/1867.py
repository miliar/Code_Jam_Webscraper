#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	int		S, Q, N, n, i, j, k, T, max;
	int		eng[100][1000];
	char	ser[105][105], quer[1005][105];
	FILE	*fout;
	fout = fopen("Aout.txt", "w");
	n = 1;
	scanf("%d", &N);
	while(n <= N){
		scanf("%d\n", &S);
		for(i = 0; i < S; i ++){
			gets(ser[i]);
		}
		/*for(i = 0; i < S; i ++){
			printf("%d : %s\n", i, ser[i]);
		}*/
		scanf("%d\n", &Q);
		for(i = 0; i < Q; i ++){
			gets(quer[i]);
		}
		for(i = 0; i < S; i ++){
			for(j = 0; j < Q; j ++){
				eng[i][j] = 0;
			}
		}
		for(i = Q - 1; i >= 0; i --){
			for(j = 0; j < S; j ++){
				if(strcmp(quer[i], ser[j]) != 0){
					if(i == Q - 1)
						eng[j][i] = 1;
					else
						eng[j][i] = eng[j][i + 1] + 1;
				}
				else
					eng[j][i] = 0;
			}
		}
		/*for(i = 0; i < S; i ++){
			for(j = 0; j < Q; j ++){
				printf("%d ", eng[i][j]);
			}
			printf("\n");
		}*/
		T = -1;
		max = -1;
		for(i = 0; i < Q;){
			for(j = 0; j < S; j ++){
				if(eng[j][i] > max){
					max = eng[j][i];
				}
			}
			//printf("i = %d max = %d\n", i, max);
			i = i + max;
			max = -1;
			T ++;
		}
		if(Q == 0)
			T = 0;
		//printf("Case #%d: %d\n", n, T);
		fprintf(fout, "Case #%d: %d\n", n, T);
		n ++;
	}
	//system("pause");
	return 0;
}
