#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <math.h>

int main(int argc, char*argv[])
{
	int T;
	int N;
	int btn[100];
	int Od[100];
	int Bd[100];
	int x=1;
	char str[1000];
	char str1[100];
	memset(str, 0, 1000);
	FILE *f = fopen("asd.txt", "r"),
		*o = fopen("qwe.txt", "a");
	fgets(str, 1000, f), memset(str, 0, 1000);
	while( !feof(f) ) {
		memset(str, 0, 1000);
		fgets(str, 1000, f);
		printf("%s\n", str);
		for( int i=0, j=0, k, b=0, m=0, n=0; i < 1000; i++ ) {
			if( j == 0 ) {
				if( str[i] == ' ' ) {
					memset(str1, 0, 100);
					memcpy(str1, str, i);
					N = atoi(str1);
					printf("N: %d\n", N);
					j = 1;
					memset(btn, 0, 100);
					memset(Od, 0, 100);
					memset(Bd, 0, 100);
				}
			}
			else if( j == 1 ) {
				if( str[i] == ' ' ) {
					if( str[i-1] == 'O' )
						btn[b] = 0xF00;
					j = 2;
					k = i + 1;
					printf("%c ", str[i-1]);
				}
			}
			else if( j == 2 ) {
				if( str[i] == ' ' || str[i] == 10 || str[i] == 0 ) {
					int temp=0;
					int r=0, s=0;
					memset(str1, 0, 100);
					memcpy( str1, str+k, i-k );
					btn[b] += atoi(str1);
					if( btn[b] & 0xF00 )
						Od[m++] = ~(~atoi(str1)|0xF00), printf("Od[%d]: %d\n", m-1, Od[m-1]);
					else
						Bd[n++] = atoi(str1), printf("Bd[%d]: %d\n", n-1, Bd[n-1]);
					printf("btn[%d]: %d (%s)\n", b, btn[b], str1);
					if( str[i] == 10 || str[i] == 0 ) {
						j = 0;
					system("pause");
						for(int O=1, B=1, i=0, j=0; i<N; temp++) {
							printf("i: %d\tN: %d\ttemp: %d\tO: %d\tB: %d\tOd: %d\tBd: %d\t%c\n",
								i, N, temp, O, B, Od[r], Bd[s], (btn[i]&0xF00)?'O':'B');
							if( O < Od[r] )
								O++;
							else if( O > Od[r] )
								O--;
							else if( btn[i] & 0xF00 ) {
								r++, i++;
								j=1;
							}
							if( B < Bd[s] )
								B++;
							else if( B > Bd[s] )
								B--;
							else if( !(btn[i] & 0xF00) && j ==0 ) {
								s++, i++;
							} j = 0;
						if( (temp+1) % 20 == 0)
							system("pause");
						}
						sprintf(str1, "Case #%d: %d\n", x++, temp);
						printf(str1);
						fputs(str1, o);
					}
					else
						j = 1;
					b++;
					if( str[i] == 0 )
						break;
				}
			}
		}
		system("pause");
	} 
	fclose(f);
	fclose(o);
}