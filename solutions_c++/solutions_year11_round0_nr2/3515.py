#include <iostream>
using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>

typedef struct Combine_Pair {
	char base;
	char nbase;
}cpair;

const int C_SIZE = 36;
const int D_SIZE = 28;
const int N_SIZE = 100;


int main (void)
{
	int T, C, D, N, len, flag;
	int i,j,k,l, p;
	char a,b,c;
	cpair Cpair[26][C_SIZE];
	char Opair[26][D_SIZE];
	int Cpc[26], Opc[26];
	char elms[N_SIZE], answer[N_SIZE];

	for (i=0;i<26;i++) {
		Cpc[i]=0;Opc[i]=0;
	}


	scanf ("%d",&T);

	for (i=1;i<=T;i++) {

		for (j=0;j<26;j++) {
			Cpc[j] = Opc[j] = 0;
		}

		printf("Case #%d: ",i);
		scanf ("%d ", &C);
		for (j=0;j<C;j++) {
			scanf("%c%c%c ", &a,&b,&c);
			p = a-'A';
			Cpair[p][Cpc[p]].base = b;
			Cpair[p][Cpc[p]++].nbase = c;
			p = b-'A';
			Cpair[p][Cpc[p]].base = a;
			Cpair[p][Cpc[p]++].nbase = c;
		}
		scanf ("%d ", &D);
		for (j=0;j<D;j++) {
			scanf("%c%c ", &a,&b);
			p = a-'A';
			Opair[p][Opc[p]++] = b;
			p = b-'A';
			Opair[p][Opc[p]++] = a;
		}
		scanf ("%d ", &N);
		fgets (elms, N+1, stdin);
		answer[0]=elms[0];
		for (j=1,len=1;j<N;j++) {
			for(flag=1;len>0 && flag!=0;) {
				flag = 0;
				p = answer[len-1]-'A';
				for (k=0;k<Cpc[p];k++) {
					if (Cpair[p][k].base == elms[j]) {
						elms[j] = Cpair[p][k].nbase;
						len--;
						flag++;
						break;
					}
				}
			}
			answer[len++] = elms[j];
			for (k=0;k<len;k++) {
				p = answer[k]-'A';
				for (l=0;l<Opc[p];l++) {
					if (Opair[p][l] == elms[j]) {
						j++;
						if (j!=N) {
							len = 1;
							answer[0] = elms[j];
						} else { len= 0; }
						goto LABEL;
					}
				}
			}
LABEL: ;
		}
		if (len > 0) {
			printf("[");
			for (j=0;j<len-1;j++) {
				printf("%c, ", answer[j]);
			}
			printf("%c]\n",answer[j]);
		} else { printf("[]\n"); }
	}
			

	return 0;
}


