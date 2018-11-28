#include <iostream>
#include <conio.h>
#include <string>

using namespace std;

int main(){
	FILE *fi, *fo;
	
	int ntest, n, sum1, sum2, i, min;
	
	fi = fopen("C-large.in", "r");
	fo = fopen("C-large.out", "w");
	
	fscanf(fi, "%d", &ntest);
	int tttest = 0;
	while(ntest--){
		tttest++;
		sum1 = sum2 = 0;
		min = 10000000;
		
		fscanf(fi, "%d", &n);
		for(i = 0; i <n; i ++){
			int temp;
			fscanf(fi, "%d", &temp);
			sum1 = sum1 ^ temp;
			sum2 = sum2 + temp;
			if(min > temp)
				min = temp;
		}

		fprintf(fo, "Case #%d: ", tttest); 
		if(sum1 != 0){
			fprintf(fo, "NO\n");
		}
		else
			fprintf(fo, "%d\n", sum2 - min);
	}
	fclose(fi);
	fclose(fo);
//	getch();
	return 0;
}
