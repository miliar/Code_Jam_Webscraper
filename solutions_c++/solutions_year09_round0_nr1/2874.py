#include <cstdio>
#include <stdio.h>
#include <string.h>
using namespace::std;

int main() {
	int l,d,n,i,j,len, k, f;
	char words[50002][17];
	char alien[1000];
	bool tab[30][30];
	int res;
	bool in;

	scanf("%d %d %d", &l, &d, &n);
	
	for(i=0; i<d; i++) {
		scanf("%s", words[i]);
	}

	in = 0;
	j = 0;
	for(f=0; f<n; f++) {
		scanf("%s", alien);
		len = strlen(alien);

		for(j=0;j<30; j++)
			for(i=0;i<30;i++)
				tab[i][j]=0;
		j = 0;
		for(i=0; i<len; i++) {
			if (alien[i] == '(') {
				i++;
				//printf("zbior %d:\n",j);
				while(alien[i]!=')') {
					tab[j][alien[i]-'a'] = 1;
					//printf("%c \n",alien[i]);
					i++;
				}
				j++;
			}
			else {
				//printf("zbior %d:\n %c\n",j,alien[i]);
				tab[j++][alien[i]-'a'] = 1;		
			}

		}
		res = 0;	

		for(j=0; j<d; j++) {
			len = strlen(words[j]);
			for(k=0; k<len; k++) {
				if(!tab[k][words[j][k]-'a'])
					break;
			}
			if ( k == len )
				res++;
		}
		printf("Case #%d: %d\n",f+1, res);	

	}

	return 0;
}

