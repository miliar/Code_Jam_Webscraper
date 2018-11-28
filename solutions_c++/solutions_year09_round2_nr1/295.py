#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(Set,i)	( (Set) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )

struct reg {
	string s;
	long double v;
	reg * left , * right;
	reg() {
		s = "";
		left = right = NULL;
	}
};
reg root;
int L;

bool ispar(char * s) {
	int len = strlen(s);
	int i = 0;
	while (isspace(s[len-1]))
		len--;
	while (isspace(s[i]) && i < len)
		i++;
	return ( i == len-1 && s[i] == ')');
}

void input(reg & no ) {
	char t[1000];
	int len,i;
	do {
		fgets(t,1000, stdin);
	//	printf("t: |%s|\n", t);
		L--;
		len = strlen(t)-1;
		while (! isalpha(t[len]) && ! isdigit(t[len]))
			len--;

		t[len+1] = 0;
		i = 0;
		while ( ! isdigit(t[i]) && t[i])
			i++;
		if (!isdigit(t[i]))
			assert( ispar(t) );

	}while (!isdigit(t[i]));

	char tmp[60];
	int ng = sscanf(t+i , "%Lf %s", &no.v, tmp);
	//printf("li %f , |%s| ng: %d\n", no.v , tmp, ng);
	if (ng == 2) {
		no.s = string(tmp);
		no.left = new reg();
		no.right = new reg();
		input(*(no.left));
		input(*(no.right));
	}
}
set<string> c;

double f(reg & no, long double p) {
	p *= no.v;
	if ( no.s == "" )
		return p;
	if (c.find(no.s) != c.end())
		return f( *no.left , p );
	return f(*no.right,p);
}
void solve() {
	scanf("%d\n", &L);
	root.s = "";
	input(root);
	char t[1000];
	while (L-- > 0) {
		fgets(t,1000, stdin);
		assert( ispar(t) );
	}

	int A;
	scanf("%d\n" , &A);
	while (A--) {
		string s;
		int n;
		cin >> s >> n;
		c.clear();
		while (n--) {
			cin >> s;
			c.insert(s);
		}
		printf( "%.7f\n", f(root, 1.0));
	}
}

int main() {
	int C , nc;

	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ":" << endl;;
		solve();
	}	
	return 0;
}
