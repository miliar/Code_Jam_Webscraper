#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define LMAX 100

void sort(int *dep, int *arr, int L){
	int i, j, tmp1, tmp2;
	
	for(j=0; j<L; j++){
		for(i=j; i<L; i++){
			if(arr[j] > arr[i]){
				tmp1 = arr[j]; tmp2 = dep[j];
				arr[j] = arr[i]; dep[j] = dep[i];
				arr[i] = tmp1; dep[i] = tmp2;
			}
		}
	}
}


int main (int argc, char * const argv[]) {
    FILE *fip, *fop;
	char path[100];
	char str1[5], str2[5];
	int depA[LMAX], arrA[LMAX], depB[LMAX], arrB[LMAX];
	int stat[LMAX], train[LMAX];
    int L, N,T, NA, NB, A, B;
	int i, j, k, l, n, odd, even, one, mul;
	int m;

	gets(path);
	fip = fopen(path, "r");
    //fip = fopen("B-small-attempt2.in", "r");
	fop = fopen("./out.txt", "w");
	fscanf(fip, "%d", &N);
	
	k = 1;
	while(k <= N){
		fscanf(fip, "%d", &T);
		fscanf(fip, "%d%d", &NA, &NB);

		for(i=0; i<NA; i++){
			fscanf(fip, "%s%s", str1, str2);
			depA[i] = ((str1[0]-'0')*10 + (str1[1]-'0'))*60 + ((str1[3]-'0')*10 + (str1[4]-'0'));
			arrA[i] = ((str2[0]-'0')*10 + (str2[1]-'0'))*60 + ((str2[3]-'0')*10 + (str2[4]-'0')) + T;
		}
		for(i=0; i<NB; i++){
			fscanf(fip, "%s%s", str1, str2);
			depB[i] = ((str1[0]-'0')*10 + (str1[1]-'0'))*60 + ((str1[3]-'0')*10 + (str1[4]-'0'));
			arrB[i] = ((str2[0]-'0')*10 + (str2[1]-'0'))*60 + ((str2[3]-'0')*10 + (str2[4]-'0')) + T;
		}

		
		A = NA; B = NB;
		
		sort(depA, arrA, NA);
		sort(arrB, depB, NB);
		for(i=0; i<NA; i++)
			for(j=0; j<NB; j++)
				if(depB[j] >= arrA[i]){ B--; depB[j] = 0; arrA[i] = 50*60; }
		sort(arrA, depA, NA);
		sort(depB, arrB, NB);
		for(i=0; i<NB; i++)
			for(j=0; j<NA; j++)
				if(depA[j] >= arrB[i]){ A--; depA[j] = 0; arrB[i] = 50*60; }
			
	

		fprintf(fop, "Case #%d: %d %d\n", k, A, B);
		k++;
	}
	
	fclose(fip);
	fclose(fop);
	
    return 0;
}

