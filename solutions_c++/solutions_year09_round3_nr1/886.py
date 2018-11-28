#include <cstdio>
#include <string.h>
#include <algorithm>

using namespace::std;


bool isDigit(char a)
{
	if ((a >= '0') && (a <='9'))
			return 1;
	return 0;
}
int main() {
	int i,j,k,t,l,index;
	int tab[30],digits[11],match[12], letters[30];
	long long res;
	char wyraz[100];
	int przydzial[100];
	int *m, poczatek=1, v;
	scanf("%d",&t);
	for(i=0; i<t;i++) {
		scanf("%s",wyraz);
		l = strlen(wyraz);
		
		for(j=0;j<10;j++)
			match[j]=digits[j] = -1;	

		for(j=0;j<30;j++)
			tab[j]=-1;
		poczatek = 1;
		for(j=0; j<l; j++) {
			if (isDigit(wyraz[j])) {
				index = wyraz[j] - '0';
				if (digits[index]<0) {
					for(k=poczatek;k<10;k++)
						if (match[k]<0)
							break;
					match[k]=wyraz[j];
					digits[index]=k;
				}
				przydzial[j]=digits[index];
			}
			else {
				index = wyraz[j]-'a';
				if (tab[index] < 0) {
					for(k=poczatek;k<10;k++)
						if (match[k]<0)
							break;
					match[k]=wyraz[j];
					tab[index]=k;
				}
				przydzial[j]=tab[index];
			}
			poczatek = 0;
		}
		m = max_element(przydzial,przydzial+l);
		k = 1;
		res = 0;
		v = *m+1;
		for(j=l-1;j>=0;j--) {
			res += przydzial[j]*k;
			k*=v;	
		}
		printf("Case #%d: %lld\n",i+1,res);
	}
	
	return 0;
}

