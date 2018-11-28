
#include <stdio.h>
#include <string.h>
#include <iostream.h>


char Server[100][101],Query[101];
int ser[100],que[1000];

int main()
{
	int i,j,k,m,N,S,Q,count,answer;
	char ch;

	scanf("%d",&N);
	for(m=1;m<=N;m++){
		scanf("%d",&S);
		getchar();
		for(i=0;i<S;i++){
			j=0;
			while((ch=getchar())!='\n')
				Server[i][j++]=ch;
			Server[i][j]='\0';
			ser[i]=i;
		}
		scanf("%d", &Q);
		if(Q==0){
			printf("Case #%d: %d\n", m, 0);
			continue;
		}
		getchar();
		for(i=0;i<Q;i++){
			j=0;
			while((ch=getchar())!='\n')
				Query[j++]=ch;
			Query[j]='\0';
			for(k=0;k<S;k++){
				if(strcmp(Server[k],Query)==0){
					que[i]=k;

					break;
				}
			}
		}

		answer=0;
		count=0;
		for(i=0;i<Q;i++){
			if(ser[que[i]]!=-1){
				ser[que[i]]=-1;
				count++;
			}
			if(count==S){
				answer++;
				count=1;
				for(j=0;j<S;j++)ser[j]=j;
				ser[que[i]]=-1;
			}
		}
		printf("Case #%d: %d\n", m, answer);
	}
	return 0;
}

