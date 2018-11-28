
#include <string.h>
#include <stdio.h>

int main() {

	unsigned int n;
	scanf("%d", &n);
	
	bool *tab = new bool[100];
	char **search = new char*[100];
	for (int i = 0; i < 100; i++)
		search[i] = new char[100];

	char **query = new char*[1000];
	for (int i = 0; i < 1000; i++)
		query[i] = new char[100];

	fprintf(stderr, "przetwarzanie! \n");
	for (int i = 0; i < n; i++) {

		unsigned int s, cases;

		scanf("%d", &s);
		fprintf(stderr, "s: %d \n",s);
		for (int j = 0; j < s; j++) {
			scanf(" %[ 0123456789a-zA-Z]s",search[j]);
			fprintf(stderr, "\t sarch[ %d ]: %s \n", j, search[j]);
		}
		
		scanf("%d", &cases);
		fprintf(stderr, "c: %d \n", cases);
		for (int j = 0; j < cases; j++) 
			scanf(" %[ 0123456789a-zA-Z]s", query[j]);

		// mamy wczytane wszystko co trzeba juz do pamieci, zerujemy tablice prawdy
		unsigned int marked = 0; 
		
		for (int j = 0; j < s; j++)
			tab[j] = false;

		int changes = 0;
		// przetwarzamy liniowo wejscie
		for (int j = 0; j < cases; j++) {
			fprintf(stderr, " query[ %d ]: %s \n", j, query[j]);
			int last = 0; 
			bool found = false;
		 	for (int k = 0; (k < s) && (!found); k++) 
				if (strcmp(query[j], search[k]) == 0) {
					found = true;
					if (!tab[k]) {
						tab[k] = true;
						marked++;
					}
					last = k;
				}

			if (marked == s) {
				marked = 1;
				for (int k = 0; k < s; k++)
					tab[k] = false;
				tab[last] = true;

//				if (j != (cases-1)) 
				changes++;
			}
					

		}
		if (changes < 0) changes = 0; 
		printf("Case #%d: %d\n", i+1, changes);

	}

	return 0;
}
