#include <stdio.h>
#include <string.h>

int clike[100];
int clikemilk[100][200];
int clikemilktype[100][200];
int min;
int minsolution[10];
int milks, customers;
int solution[10];

void bruteforce( int current){
	if (current<milks){
		solution[current] = 0;
		bruteforce(current+1);
		solution[current] = 1;
		bruteforce(current+1);
		return;
	}
	int i,j,k;
	bool satisfied[100];
	memset(satisfied,0,sizeof(satisfied));

	for(i=0;i<customers;i++)
		for(j=0;j<clike[i];j++)
			if (solution[clikemilk[i][j]] == clikemilktype[i][j] ) satisfied[i] = true;
	j = 0;
	for(i=0;i<customers;i++) if (satisfied[i]) j++;
	if (j == customers) {//Found
		j=0;
		for(i=0;i<milks;i++) j += solution[i];
		if (j<min) { min = j; memcpy(minsolution,solution,sizeof(solution));}
	}

}
void main(void){
	FILE* fin = fopen("Milkshakes.in","rt");
	FILE* fout = fopen("Milkshakes.out","wt");

	int N;
	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		
		fscanf(fin, "%d\n", &milks);
		fscanf(fin, "%d\n", &customers);
		memset(clike,0,sizeof(clike));
		for (int j=0;j<customers;j++) {
			int T,t1;
			fscanf(fin, "%d", &T);

			clike[j] = T;
			for(int k=0;k<T;k++) {fscanf(fin, "%d %d", &t1,&clikemilktype[j][k]);clikemilk[j][k] = t1-1;}
		}

		min = milks+1;
		bruteforce( 0);
		if(min == milks+1)
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",i+1);
		else {
			fprintf(fout,"Case #%d: ",i+1);
			for(int j=0; j<milks; j++)	fprintf(fout,"%d ", minsolution[j]);
			fprintf(fout,"\n");
		}

	}

	fclose(fin);
	fclose(fout);
}