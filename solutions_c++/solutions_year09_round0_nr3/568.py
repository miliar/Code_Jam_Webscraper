#include "stdio.h"
#include "string.h"

char * get_str(int a) {
	int a0, a1, a2, a3;
	char * res = new char [5];
	a0 = a%10;
	a1= (a/10) % 10;
	a2 = (a/100) %10;
	a3 = (a/1000) % 10;
	res[0] = a3 + '0';
	res[1] = a2 + '0';
	res[2] = a1 + '0';
	res[3] = a0 + '0';
	res[4] = '\0';
	return res;
}

int main( int argc,char *argv[] ) {
	FILE *fin, *fout;
	fin = fopen ( argv[1], "r" );
	if ( ! fin ) return 0;
	fout = fopen ( argv[2], "w" );
	if ( ! fout ) return 0;
	char welcome[20] = "welcome to code jam";
	int N;
	fscanf(fin, "%d\n", &N);
	int i,j,jj;
	char line[501];
	char c;
	int head[19];
	char * result;
	for (i=0; i<N; i++) {
		j=0;
		while( !feof(fin) && (c=fgetc(fin))!='\n') {
			line[j] = c;
			j++;
		}
		line[j]='\0';
		jj = j;
		for(j=0; j<19; j++) {
			head[j] = 0;
		}
		for (j=0; j<jj; j++) {
			switch (line[j]) {
				case 'w':
					head[0] ++;
					break;
				case 'e':
					head[1] = head[0] + head[1];
					head[1] %=10000;
					head[6] =head[5] + head[6];
					head[6] %=10000;
					head[14] = head[13] + head[14];
					head[14] %=10000;
					break;
				case 'l':
					head[2] = head[2] + head[1];
					head[2] %=10000;
					break;
				case 'c':
					head[3] = head[3] + head[2];
					head[3] %= 10000;
					head[11] = head[10] + head[11];
					head[11] %=10000;
					break;
				case 'o':
					head[4] = head[4] + head[3];
					head[4] %=10000;
					head[9] = head[9] + head[8];
					head[9] %=10000;
					head[12] = head[12] + head[11];
					head[12] %=10000;
					break;
				case 'm':
					head[5] = head[5] + head[4];
					head[5] %=10000;
					head[18] = head[18] + head[17];
					head[18] %=10000;
					break;
				case ' ':
					head[7] = head[7] + head[6];
					head[7] %=10000;
					head[10] = head[10] + head[9];
					head[10] %=10000;
					head[15] = head[15] + head[14];
					head[15] %=10000;
					break;
				case 't':
					head[8] = head[7] + head[8];
					head[8] %=10000;
					break;
				case 'd':
					head[13] = head[13] + head[12];
					head[13] %=10000;
					break;
				case 'j':
					head[16] = head[16] + head[15];
					head[16] %=10000;
					break;
				case 'a':
					head[17] = head[17] + head[16];
					head[17] %=10000;
					break;
				default:
					break;
			}
		}
		result = get_str(head[18]);
		fprintf(fout, "Case #%d: %s\n", i+1, result);
	}
	fclose ( fin );
	fclose (fout);
	return 1;
}