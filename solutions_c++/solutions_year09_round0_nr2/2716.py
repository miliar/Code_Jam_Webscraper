#include <iostream>
#include <cstdio>
#include <limits>

using namespace std;

typedef struct {
	int m, n;
} node;

node l, r, a ,x;

int main(){
	int m,n;
	string sout;

	while ( scanf("%d %d",&m, &n) != EOF && (m != 1 || n != 1) ) {
		sout = "";
		x.m = m;
		x.n = n;

		l.m = 0;
		l.n = 1;

		r.m = 1;
		r.n = 0;

		a.m = 1;
		a.n = 1;
		
		while ( x.m != a.m || x.n != a.n ){
/*
			int aux;
			printf("Antes:\n");
			printf("x: %d/%d\n", x.m, x.n);
			printf("a: %d/%d\n", a.m, a.n);
			printf("l: %d/%d\n", l.m, l.n);
			printf("r: %d/%d\n", r.m, r.n);
			printf("\n");
*/		
			if ( x.m * a.n < a.m * x.n ) {
				//vai para a esquerda
				//cout << "L" << endl;
				sout += 'L';
				r.m = a.m;
				r.n = a.n;
			} else {
				//vai para a direita
				sout += 'R';
				//cout << "R" << endl;				
				l.m = a.m;
				l.n = a.n;
			}
			a.m = l.m + r.m;
			a.n = l.n + r.n;
			
/*		
			printf("Depois:\n");
			printf("x: %d/%d\n", x.m, x.n);
			printf("a: %d/%d\n", a.m, a.n);
			printf("l: %d/%d\n", l.m, l.n);
			printf("r: %d/%d\n", r.m, r.n);
			printf("\n");
			
			cin >> aux;
*/
		}
		printf("%s\n", sout.c_str());
	}
	return 0;
}


