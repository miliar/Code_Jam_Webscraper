#include <stdio.h>
#include <string.h>

const int Max = 1024;
int A[Max];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T,N;
	scanf("%d",&T);
	for (int t = 1;t <= T;t++){
		scanf("%d",&N);
		for (int i = 1;i <= N;i++)
			scanf("%d",&A[i]);
		int R = 0;
		for (int i = 1;i <= N;i++)
			if (A[i] > -1){
				//printf("%d ",i);
				int c = 1;
				for (int j = A[i];j != i;c++){
					//printf("=> %d ",j);
					int k = A[j];
					A[j] = -1;
					j = k;
				}
				//puts("");
				if (c >= 2)
					R += c;
			}
		printf("Case #%d: %d\n",t,R);
	}
	fclose(stdout);
	return 0;
}
