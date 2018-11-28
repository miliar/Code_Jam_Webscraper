#include<stdio.h>
#include<string.h>

#define MAX 1001

int T;

int N;
char engine_name[101][100];

int M;
char find_name[MAX][100];

int dy[MAX];

int i,j,k;

FILE *fout=fopen("output.txt","w");

int process()
{
	dy[0]=-1;
	for(i=1;i<=M;i++){
		dy[i]=M+1;
	}

	for(i=1;i<=M;i++){
		for(j=1;j<=N;j++){
			if( !strcmp(find_name[i],engine_name[j]) ) continue;

			for(k=i-1;k>=0;k--){
				if(dy[i] > dy[k]+1)
					dy[i]=dy[k]+1;
				
				if( !strcmp(find_name[k],engine_name[j]) )
					break;
			}
		}
	}

	if(dy[M] < 0) return 0;

	return dy[M];
}

int main(void)
{
	FILE *fin=fopen("input.txt","r");

	fscanf(fin,"%d\n",&T);

	int cnt;
	char tp;

	for(int test=1;test<=T;test++){
		N=M=0;

		fscanf(fin,"%d\n",&N);

		for(i=1;i<=N;i++){
			cnt=0;
			do{
				fscanf(fin,"%c",&tp);
				if(tp=='\n')
					break;

				engine_name[i][cnt]=tp;
				cnt++;
			}while(1);
			engine_name[i][cnt]=0;
		}

		fscanf(fin,"%d\n",&M);
		cnt=0;
		for(i=1;i<=M;i++){
			cnt=0;
			do{
				fscanf(fin,"%c",&tp);
				if(tp=='\n')
					break;

				find_name[i][cnt]=tp;
				cnt++;
			}while(1);
			find_name[i][cnt]=0;
		}

		fprintf(fout,"Case #%d: %d\n",test,process());

		printf("Case #%d: %d\n",test,process());
	}

	return 0;
}