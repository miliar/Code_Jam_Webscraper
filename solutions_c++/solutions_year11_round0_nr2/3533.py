#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <iostream>
using namespace std;
int main () {
	int c, d, t, n, i, j, k, m, cnt, mm;
	bool entro;
	char str[302], lst[102], aux[4], beg[4], end, swap;
	map<string, char> C; map<string, char>::iterator it;
	string D[64], now;
	FILE *p = fopen("B-large.in","r");

	fscanf(p, "%d", &t);

	for (i = 0; i != t; i++) {
		C.clear();
		fscanf(p, " %d", &c);
		for (j = 0; j != c; j++) {
			fscanf(p, " %s", aux);
			beg[0] = aux[0];
			beg[1] = aux[1];
			beg[2] = '\0';
			end = aux[2];
	//		end[1] = '\0';
			C[string(beg)] = end;
			beg[0] = aux[1];
			beg[1] = aux[0];
			C[string(beg)] = end;
		}
/*		printf("mapa da iteracao %d:\n", i);
		for (it = C.begin(); it != C.end(); it++)
			cout << (*it).first << " -> " << (*it).second << endl;
*/
		fscanf(p, " %d", &d);
		k = 0;
		for (j = 0; j != d; j++) {
			fscanf(p, " %s", aux);
			D[k++] = (string)aux;
			swap = aux[1];
			aux[1] = aux[0];
			aux[0] = swap;
			D[k++] = (string)aux;
		}
		d = k;
/*		printf("Lista dos rec:\n");
		for (j = 0; j != d; j++)
			cout << D[j] << endl;
*/
		fscanf(p, " %d %s", &n, str);
//		printf("str: %s\n", str);
		lst[0] = str[0];
		k = 1;
		for (j = 1; str[j]; ++j) {
			entro = false;
			lst[k] = str[j];
			aux[0] = lst[k-1];
			aux[1] = lst[k];
			aux[2] = '\0';
//			printf("aux[%d]: %s\n", j, aux);
			it = C.find( (string)aux);
			//k++ ?
			if ( it != C.end()) {
		//		printf("achou nos C!\n");
				lst[k-1] = (*it).second;
				continue;
			}
			cnt = 0;
		//	printf("Nao achou nos C...\n");

			aux[1] = lst[k];
			for (mm = 0; mm != k; mm++) {
				aux[0] = lst[mm];
				aux[2] = '\0';
			//	printf("Procurando %s nos D\n", aux);
				for (m = 0; m != d; m++) {
					if (D[m].compare( (string)aux) == 0) {
					//	printf("mas achou nos D!\n");
						if (str[j+1]) {
							lst[0] = str[++j];
							k = 1;
					//		printf("e colokou lst[0] = %c, next: %c\n", lst[0], str[j+1]);
							entro = true;
							goto end_;
						}
						else {
							k = 0;
							goto end;
						}
					}
				}
			}
end_:
			if (entro == false) k++;
		}
end:
		cnt = 0;
		printf("Case #%d: [", i+1);
		for (j = 0; j != k; j++) {
			str[cnt++] = lst[j];
			str[cnt++] = ',';
			str[cnt++] = ' ';
		}
		if (k > 0) str[cnt-2] = '\0';
		else str[0] = '\0';
		printf("%s]\n", str);
//	puts("\n")	;
	}
	return 0;
}
