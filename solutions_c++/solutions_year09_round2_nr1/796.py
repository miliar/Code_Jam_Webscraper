#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

struct tree {
	double x;
	char name[15];
	tree *aa;
	tree *bb;
	tree *pp;
};

int m;
char line[1000000];

bool inside(char a[20], char s[150][20] ) {
	REP(i,m) if ( strcmp(a,s[i]) == 0 ) return true;
	return false;
}

int main()
{
	int T;
	scanf( "%d\n", &T );

	FOR(tcase,1,T) {
		printf( "Case #%d:\n", tcase );

		int n;
		scanf( "%d\n", &n );
		
		gets(line);
		while ( --n ) gets(&line[strlen(line)]);
		
		tree *t = 0, *root = 0;

		char  *p = line;
		double x;
		while ( *p != 0 ) {
			while ( *p == ' ' ) p++; if ( *p == 0 ) break;
			if ( *p == '(' ) {
				p++; while ( *p == ' ' ) p++;
				sscanf( p, "%lf", &x );
				tree *tt = new tree;
				tt->pp = t;
				if ( t == 0 ) t = root = tt, t->aa = t->bb = 0;
				else if ( t->aa == (tree*)-1 ) { t->aa = tt; t = t->aa; }
				else { t->bb = tt; t = t->bb; }
				t->x = x;
				t->name[0] = 0;
			}
			else if ( *p == ')' ) {
				p++;
				t = t->pp;
			}
			else {
				t->aa = t->bb = (tree*)-1;
				sscanf( p, "%s", t->name );
				while ( 'a' <= *p && *p <= 'z' ) p++;
			}
			while ( *p == '.' || *p == ' ' || ('0' <= *p && *p <= '9') ) p++;
		}

		int q;
		char f[150][20];
		scanf( "%d\n", &q );
		while ( q-- ) {
			scanf( "%*s %d", &m );
			REP(i,m) scanf( "%s", f[i] );
			
			double ret = 1.0;

			tree *p = root;
			while ( p->name[0] != 0 ) {
				ret *= p->x;
				if ( inside(p->name, f) ) p = p->aa;
				else p = p->bb;
			}
			
			ret *= p->x;

			printf( "%.7lf\n", ret );
		}
	}

	return 0;
}
