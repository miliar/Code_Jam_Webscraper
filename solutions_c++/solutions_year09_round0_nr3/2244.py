#include <stdio.h>
#include <string.h>
#include <cstdlib>

using namespace std;

int ncase, N;
char cad[600];

#define LENW 19
int stat[LENW+1];
char *welcome="welcome to code jam";

int main() {
	scanf(" %d", &N);
	for (ncase=0; ncase<N; ncase++) {
		memset(stat, 0, sizeof(stat));
		stat[LENW]=1;

		scanf(" %[^\n]", cad);
		for (int i=strlen(cad)-1; i>=0; i--) {
			for (int j=0; j<LENW; j++) if (cad[i]==welcome[j]) {
				stat[j]=(stat[j]+stat[j+1])%10000;
				//printf("%s\n", cad+i);
				//for (int k=0; k<LENW; k++) printf("%c %d\n", welcome[k], stat[k]);

			}
		}
		printf("Case #%d: %04d\n", ncase+1, stat[0]);

	}
	return 0;
}
