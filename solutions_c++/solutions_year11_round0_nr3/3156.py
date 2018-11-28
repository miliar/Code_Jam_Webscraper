#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define DEBUG 0 
int b[20];
int d;

int binario(int A, int digits){
	d = 0;
	int num = A, res;

	int x= 0;
	while(num >= 1){
		res = num % 2;
		if (res == 1){
			num = (num - 1) / 2;
		}else{
			num = num / 2;
		}
		b[d++]=res;
	}
	while(d<digits){
		b[d++]=0;
	}
}

int main(int argc, char* argv[]){
	FILE *fin = fopen(argv[1],"r");
	int casos;
	fscanf(fin,"%d\n",&casos);
	for(int caso=1;caso<= casos;++caso){
		int quantity = 0;
		int candies;
		fscanf(fin,"%d\n",&candies);
		int  *vcandies = (int*)malloc(sizeof(int)*candies);

		for(int i=0;i<candies;++i){
			fscanf(fin,"%d",&vcandies[i]);
		}

		for(int p=1;p<pow(2,candies-1);++p){
			binario(p, candies);
			
			if(DEBUG){
				for(int j=d-1;j>=0;--j){
					fprintf(stdout,"%d",b[j]);
				}
				fprintf(stdout,"\n");
			}
			int sumA=0,sumAreal=0, sumB=0,sumBreal=0;
			for(int op=d-1;op>=0;--op){
				if(b[op]==1){
					sumA^=vcandies[op];
					sumAreal += vcandies[op];
				}
				else{
					sumB^=vcandies[op];
					sumBreal += vcandies[op];
				}
			}
			if(DEBUG)
				printf("sumA %d sumB %d\n",sumA, sumB);
			if(sumA == sumB){
				if(DEBUG)
					printf("sum (%d) sumAreal %d sumBreal %d\n",sumA, sumAreal, sumBreal);
				if(sumAreal >= sumBreal){
					if(sumAreal > quantity)
						quantity = sumAreal;
				}else {
					if(sumBreal > quantity)
						quantity = sumBreal;
				}
			}
		}
		if(quantity != 0)
			fprintf(stdout,"Case #%d: %d\n",caso,quantity);
		else
			fprintf(stdout,"Case #%d: NO\n",caso);
		free(vcandies);
	}

	fclose(fin);

	return 0;
}
