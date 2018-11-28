#include "stdio.h"
#include "string.h"

int main (int argc,char *argv[] ) {
	FILE *fin, *fout;
	fin = fopen ( argv[1], "r" );
	if ( ! fin ) return 0;
	fout = fopen ( argv[2], "w" );
	int T;
	fscanf(fin, "%d\n", &T);
	int i, j;
	int len, num;
	int index, base;
	long long int min;
	long long int power;
	char digit[62];
	int map[36];
	for (i=0; i<T; i++) {
		for(j=0; j<36; j++) {
			map[j] = -1;
		}
		fscanf(fin, "%s\n", digit);
		len = strlen(digit);
		num = 0;
		for (j=0; j<len; j++) {
			index = digit[j];
			if (index>='0'&&index<='9') {
				index = index - '0';
			} else {
				index = index - 'a' + 10;
			}
			if (map[index] == -1) {
				if (num == 0) {
					map[index] = 1;
				} else {
					if(num == 1) {
						map[index] = 0;
					} else {
						map[index] = num;
					}
				}
				num ++;
			}
		}
		if (num==1) {
			base = 2;
		} else {
			base = num;
		}
		min = 0;
		power = 1;
		for (j=len-1; j>=0; j--) {
			index = digit[j];
			if (index>='0'&&index<='9') {
				index = index - '0';
			} else {
				index = index - 'a' + 10;
			}
			min = min + ((long long int) map[index]) * power;
			//if (min<0) printf("%ld\n", min);
			power = power * base;
		}
		fprintf(fout,"Case #%d: %lld\n", i+1, min);
	}

	fclose ( fin );
	if ( ! fout ) return 0;
	fclose (fout);
	return 1;
}