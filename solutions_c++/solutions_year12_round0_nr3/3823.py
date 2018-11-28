#include <stdio.h>
#include <cstring>
#include <cmath>

int main() {
	FILE *fin = fopen("C-large.in","r");
	FILE *fout = fopen("out.txt","w");

	int T;
	fscanf(fin,"%d\n",&T);

	for (int t=1; t<=T; t++) {
		int A, B;
		fscanf(fin,"%d %d",&A,&B);

        int count = 0;
        int pwr10 = 1;
        while (pwr10*10 <= A) {
            pwr10 *= 10;
        }
        for (int i=A; i<B; i++) {
            if (i >= pwr10*10) {
                pwr10 *= 10;
            }
            int temp = i;
            for (int j=1; j<pwr10; j*=10) {
                int digit = temp%10;
                temp = digit*pwr10 + (temp/10);
                if (temp == i) break; //avoid repeats
                if (temp >= pwr10 && temp > i && temp <= B) {
                    count++;
                    //printf("%d %d\n", i, temp);
                }
            }
        }

    	fprintf(fout,"Case #%d: %d\n",t,count);
	}
}
