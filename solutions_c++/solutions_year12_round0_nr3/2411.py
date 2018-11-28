#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <map>

using namespace std;

#ifdef DEBUG
int compare(const void* e1, const void* e2) {
   char c1 = *(char*)e1;
   char c2 = *(char*)e2;
   return c1 - c2;
}
#endif

int casas_decimais(int i) {
	int count = 1;
	int casa = 10;

	while(i>=casa) {
		count++;
		casa *= 10;
	}

	return count;
}

int rotaciona(int n, int casas) {
	if (casas <= 1)
		return n;

	int casa_maior = (int) pow(10,(casas-1));
	int valor_maior = n/casa_maior;
	
	n = ((n-(valor_maior*casa_maior))*10)+valor_maior;
}

int main() {
	int t, a, b;

	scanf("%d",&t);

	for (int i=1; i<=t; i++) {

		scanf("%d %d",&a,&b);
		int count = 0;

		int casas = casas_decimais(a);
		int lim_inf = (int) pow(10,(casas-1));

		#ifdef DEBUG
			printf("============== CASE %d ============\n A is %d, B is %d\n\n",i,a,b);
			char buff1[casas+1], buff2[casas+1];
		#endif

		while (a < b) {
			map<int,int> already;
			int aux = a;

			for (int k=0; k<casas; k++) {
				aux = rotaciona(aux,casas);
				if (a < aux && aux <= b && aux > lim_inf && already.count(aux) == 0) {
					count++;
					already[aux] = 1;

					#ifdef DEBUG
						printf("%dth pair found!! (%d, %d)\n",count,a,aux);
						sprintf(buff1, "%i", a);
						sprintf(buff2, "%i", aux);
						qsort (buff1, casas, 1, compare);
						qsort (buff2, casas, 1, compare);

						if (strcmp(buff1,buff2))
							printf("FALSE!!!!\n");
					#endif
				}
			}
			a++;
		}

		printf("Case #%d: %d\n",i,count);
	}
}
