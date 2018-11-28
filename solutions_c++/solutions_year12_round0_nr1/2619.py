#include<fstream>
#include<string>
#include<stdio.h>


using namespace std;
FILE *f;
FILE *g;

#define maxn 10000

char sir1[ maxn ], sir2[ maxn ];

int main() {
	int n;
	f = fopen ("a-goog.in" , "r");
	g = fopen ("a-goog2.out" , "w");
	
	string val("yhesocvxduiglbkrztnwjpfmaq");
	fscanf(f,"%d\n", &n);
	for( int ii = 1; ii<= n; ++ii) {
		memset(sir1, 0, sizeof(sir1));
		fgets(sir1, maxn, f);
		fprintf(g,"Case #%d: ", ii);
		int p = strlen(sir1);
		for( int i = 0; i < p-1; ++i) {
			if( sir1[i] == ' ') {
				fprintf(g, " ");
				continue;
			}
			fprintf(g,"%c", val[sir1[i]-'a']);
		}
		fprintf(g,"\n");
	}
}
