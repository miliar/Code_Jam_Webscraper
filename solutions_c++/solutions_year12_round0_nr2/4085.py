#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	FILE *fpin,*fpout;
	int T, N, S, p, count=0, score, i, j;
	

	fpin=fopen("B-small-attempt0.in","r");
	fpout=fopen("B-small.out","w");
	if(fpin==NULL)
		exit(10);
	fscanf(fpin,"%d",&T);
	for(i=0;i<T;i++){
		fscanf(fpin, "%d", &N); //number of googlers
		fscanf(fpin, "%d", &S); //number of surprizing triplets
		fscanf(fpin, "%d", &p); // at least p winning number
		for(j=0;j<N;j++){
			fscanf(fpin, "%d", &score);
			if(score>=3*p)
				count++;
			else if(score>p){
				score=score-p;
					if(score>=(2*(p-1)))
						count++;
					else if(S>0 && score>=(2*(p-2)))
					{
						S--;
						count++;
					}
			}
		}
		fprintf(fpout, "Case #%d: %d\n", i+1, count);
		count=0;
	}
}