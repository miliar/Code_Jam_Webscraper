#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

int main()
{
	int C, D, N;
	int Ci=0, Di=0, Ni=0;
	char Cs[120];
	char Ds[60];
	char Ns[120];
	char str[1000];
	char str1[100];
	FILE *f = fopen("asd.txt", "r"),
		*o = fopen("qwe.txt", "a");
	fgets(str, 1000, f);
	int x=1;
	while( !feof(f) )
	{
		memset(str, 0, 1000);
		fgets(str, 1000, f);
		printf("%s", str);
		char R[120];
		int Ri=0;
		Ci = Di = Ni = 0;
		for(int i=0, j=0, k; i<1000; i++)
		{
			if( j == 0 ) {
				if( str[i] == ' ' ) {
					memset(str1, 0, 100);
					memcpy(str1, str, i);
					C = atoi(str1);
					k = i + 1;
					if( C > 0 )
						j = 1, memset( Cs, 0, 120 );
					else 
						j = 2;
					printf("C: %d\t", C);
				}
			} else if( j == 1 ) {
				if( str[i] == ' ' ) {
					memcpy( Cs+Ci*3, str+k, 3 );
					printf("Cs: %s\t", Cs+Ci*3);
					Ci++;
					if( Ci >= C ) 
						k = i + 1, j = 2;
				}
			} else if( j == 2 ) {
				if( str[i] == ' ' ) {
					memset(str1, 0, 100);
					memcpy(str1, str+k, i-k);
					D = atoi(str1);
					k = i + 1;
					if( D > 0 )
						j = 3, memset( Ds, 0, 60 );
					else 
						j = 4;
					printf("D: %d\t", D);
				}
			} else if( j == 3 ) {
				if( str[i] == ' ' ) {
					memcpy( Ds+Di*2, str+k, 2 );
					printf("Ds: %s\t", Ds+Di*2);
					Di++;
					if( Di >= D )
						k = i + 1, j = 4;
				}
			} else if( j == 4 ) {
				if( str[i] == ' ' ) {
					memset(str1, 0, 100);
					memcpy(str1, str+k, i-k);
					N = atoi(str1);
					j = 5, k = i + 1, memset( Ns, 0, 120 );
					printf("N: %d\t", N);
				}
			} else if( j == 5 ) {
				if( str[i] == 10 ) {
					memset(R, 0, 120);
					memcpy( Ns, str+k, i-k );
					printf("Ns: %s\n", Ns);

					for(int i=0; i < N; i++)
					{
						if( Ri > 0 ) {
							for(int j=0; j<C; j++) {
								if( Ns[i] == Cs[j*3] && R[Ri-1] == Cs[j*3+1] || R[Ri-1] == Cs[j*3] && Ns[i] == Cs[j*3+1] ) {
									R[Ri-1] = Cs[j*3+2];
									for(int i=0; i<Ri-1; i++) {
										if( R[i] == Ds[j*2] && R[Ri-1] == Ds[j*2+1] || R[Ri-1] == Ds[j*2] && R[i] == Ds[j*2+1] ) {
											memset(R, 0, 120);
											Ri = 0;
											goto end;
										}
									}
									goto end;
								}
							}
							for(int j=0; j<D; j++) {
								for(int k=0; k<Ri; k++) {
									if( Ns[i] == Ds[j*2] && R[k] == Ds[j*2+1] || R[k] == Ds[j*2] && Ns[i] == Ds[j*2+1] ) {
										memset(R, 0, 120);
										Ri = 0;
										goto end;
									}
								}
							}
						}
						R[Ri++] = Ns[i];
end:
						;
					}
					memset(str1, 0, 100);
					char R2[400];
					memset(R2, 0, 400);
					for(int i=0; R[i]; i++) {
						R2[i*3+0] = R[i];
						if( R[i+1] )
							R2[i*3+1] = ',', R2[i*3+2] = ' ';
					}
					sprintf(str1, "Case #%d: [%s]\n", x++, R2);
					puts(str1);
					fputs(str1, o);
					system("pause");
				}
			}

		}
	}
	system("pause");
	fclose(f);
	fclose(o);
	return 0;
}