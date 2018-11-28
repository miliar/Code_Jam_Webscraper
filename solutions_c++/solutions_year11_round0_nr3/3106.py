// qual_3.cpp : Defines the entry point for the console application.
//

#include<stdio.h>
#include<memory.h>
#include<string.h>

int c[1100];
int n;

void bubbleSort()
{
  int i, j, temp;
 
  for (i = (n - 1); i > 0; i--)
  {
    for (j = 1; j <= i; j++)
    {
      if (c[j-1] > c[j])
      {
        temp = c[j-1];
        c[j-1] = c[j];
        c[j] = temp;
      }
    }
  }
}

int calculate(int pivot){
	int i, j, small, big;
	small = 0;
	big = 0;
	for(i=0; i<pivot; i++){
		small = small ^ c[i];
	}
	for(i=pivot; i<n; i++){
		big = big ^ c[i];
	}
	if(small == big){
		big = 0;
		for(i=pivot; i<n; i++){
			big = big + c[i];
		}
		return big;
	}
	return -1;
}

void main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc;
	int i, j, temp;
	bool flag=false;

	fscanf(fp, "%d", &tc);

	for(i=0; i<tc; i++){
		fscanf(fp, "%d", &n);
		for(j=0; j<n; j++){
			fscanf(fp, "%d", &c[j]);
		}
		bubbleSort();
		j=1;
		while(j<n && !flag){
			temp = calculate(j);
			if(temp != -1){
				printf("Case #%d: %d\n", i+1, temp);
				fprintf(ofp, "Case #%d: %d\n", i+1, temp);
				flag = true;
			}
			j++;
		}
		if(flag == false){
			printf("Case #%d: NO\n", i+1);
			fprintf(ofp, "Case #%d: NO\n", i+1);
		}
		flag = false;
	}

}
