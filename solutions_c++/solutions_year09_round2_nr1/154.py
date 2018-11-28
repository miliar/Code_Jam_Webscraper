#include <cstdio>
#include <set>
#include <string>

using namespace std;

struct Rule {
	double p;
	bool isSimple;
	string feature;
	Rule * yes;
	Rule * no;
};

Rule * readRules() {
	Rule * r = new Rule();
	scanf( "%*[^(](" );
	
	scanf( "%lf", & r->p );
	
	scanf("%*[^a-z)]");
	
	char s[50];
	if ( scanf( "%[a-z]", s) == 1 ) {
		// has subrules
		r->isSimple = false;
		//printf("%s\n", s);
		r->feature = string(s);
		
		r->yes = readRules();
		r->no  = readRules();
	} else
		r->isSimple = true;
	
	scanf( "%*[^)])" );
	
	return r;
}

void printRule( Rule * r, int tabs ) {
	for(int i=0;i<tabs;i++)putchar('\t');
	printf("(%0.3lf", r->p);
	if ( r->isSimple )
		printf(")\n");
	else {
		printf(" %s\n", r->feature.c_str());
		printRule( r->yes , tabs + 1);
		printRule( r->no  , tabs + 1);
		for(int i=0;i<tabs;i++)putchar('\t');
		printf(")\n");
	}
}

double prob( const set<string> & features, Rule * rule ) {
	if ( rule->isSimple )
		return rule->p;
	else {
		if ( features.find( rule->feature ) != features.end() )
			return rule->p * prob( features, rule->yes );
		else
			return rule->p * prob( features, rule->no );
	}
}

int main() {
	int N;
	scanf( "%d", &N );
	
	for ( int testCase = 1; testCase <= N; testCase++ ) {
		int L;
		scanf( "%d", &L );
		Rule * rules = readRules();

		//printRule( rules, 0 );
		
		printf( "Case #%d:\n", testCase );

		int A;
		scanf("%*[^0-9]");
		scanf( "%d", &A );
		for ( int i = 0; i < A; i++ ) {
			set<string> features;
			char name[50];
			int nFeatures;
			
			scanf( "%s", name );
			scanf( "%d", & nFeatures );
			
			for ( int k = 0; k < nFeatures; k++ ) {
				char s[50];
				scanf( "%s", s );
				
				features.insert(string(s));
			}
			
			double p = prob( features, rules );
			
			printf( "%.7lf\n", p );
		}
	}
	
	return 0;
}
