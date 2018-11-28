#include <cstdio>
#include <map>
#include <cstdlib>
#include <string>
#include <utility>
using namespace std;

#define MAX_LINE	(10000)
#define MAX_S		(200)

#define CHOLERNIE_DUZO	(1<<29)

static char line[MAX_LINE+10];
static void readline() {
	fgets(line, MAX_LINE, stdin);
	line[MAX_LINE+1] = 0;
	char *z = line;
	while(*z && *z!='\r' && *z!='\n')
		z++;
	*z = 0;
}

int main() {
	int _N;
	readline(); sscanf(line, "%d", &_N);
	for(int _Ni=1;_Ni<=_N;_Ni++) {
		/*
		 * WCZYTAJ WYSZUKIWARKI
		 */
		std::map<std::string, int> SE;
		int S; readline(); sscanf(line,"%d",&S);
		for(int i=0;i<S;i++) {
			readline();
			SE[std::string(line)] = i;
		}

		/* warunki początkowe */
		int _arr1[MAX_S], _arr2[MAX_S];
		int *arrIn = _arr1, *arrOut = _arr2;
		for(int i=0;i<S;i++)
			arrIn[i] = 0;

		/*
		 * WCZYTAJ ZAPYTANIA
		 */
		int Q; readline(); sscanf(line,"%d",&Q);
		for(int i=0;i<Q;i++) {
			/* wczytaj zapytanie */
			readline();
			if(SE.find(std::string(line))==SE.end()) {
				fprintf(stderr, "NIE ZNALEZIONO >%s<\n",line);
				abort();
			}
			int q = SE[std::string(line)];
			/* wylicz */
			for(int i=0;i<S;i++)
				arrOut[i] = std::min(arrIn[i],1+arrIn[q]);
			arrOut[q] = CHOLERNIE_DUZO;
			/* zamień */
			swap(arrIn, arrOut);
		}

		/*
		 * WYNIK KOŃCOWY
		 */
		int result = CHOLERNIE_DUZO;
		for(int i=0;i<S;i++)
			result = std::min(result, arrIn[i]);

		printf("Case #%d: %d\n", _Ni, result);
	}
	return 0;
}

