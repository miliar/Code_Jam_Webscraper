#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SMAX 100
#define QMAX 1000
#define NLEN 100

int contin_num(int index, int *query, int Q){
	int i;
	
	i = 0;
	while((query[i] != index) && (i < Q)) i++;
	
	return i;
}


int main (int argc, char * const argv[]) {
    FILE *fip, *fop;
	char path[100], c[10];
	char s[SMAX][NLEN], q[QMAX][NLEN];
	int qint[QMAX], stat[SMAX];
    int N, S, Q, i, j, k;
	int count, start, max, imax;

	gets(path);
	fip = fopen(path, "r");
	//fip = fopen("A-small-attempt0.in", "r");
	fop = fopen("./out.txt", "w");
	fscanf(fip, "%d", &N);
	
	k = 1;
	while(k <= N){
		for(i=0; i<QMAX; i++) qint[i] = -1; //dont care
		fscanf(fip, "%d", &S); fgets(c, 10, fip);
		for(i=0; i<S; i++)
			fgets((char *)&s[i], NLEN, fip);
		fscanf(fip, "%d", &Q); fgets(c, 10, fip);
		for(i=0; i<Q; i++){
			fgets((char *)&q[i], NLEN, fip);
			for(j=0; j<S; j++)
				if(!strcmp((const char *)&q[i], (const char *)&s[j])){ qint[i] = j; break; } //numbering
		}

		count = -1; start = 0;
		while(Q-start > 0){
			max = -1; imax = -1;
			for(i=0; i<S; i++) stat[i] = contin_num(i, &qint[start], Q-start);
			for(i=0; i<S; i++) if(stat[i] > max){ max = stat[i]; imax = i; }
			
			start += max;
			count++;
		}
		if(count < 0) count = 0;
		fprintf(fop, "Case #%d: %d\n", k, count);
		k++;
	}
	
	fclose(fip);
	fclose(fop);
	
    return 0;
}

