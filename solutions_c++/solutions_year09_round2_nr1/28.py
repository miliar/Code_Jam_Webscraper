#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

struct el {
	double w;
	string f;
	el *left , *right;
};

el *root;
string a[128];

void damn ( el *root ) {
	char c;
	cin >> c;
	
	root -> left = root -> right = NULL;
	
	cin >> root -> w;
	
	cin >> c;
//	cout << "P" << c << "H" << endl;
	if ( c == ')' ) return;
	root -> f = c;
	while ( cin.get ( c ) , c != '\n' && c != ' ' )
		root -> f = root -> f + c;
	
//	cout << "E" << root -> w << ' ' << root -> f << "T" << endl;
	
	if ( root -> f == ")" ) return;
	root -> left = new el;
	root -> right = new el;
		
	damn ( root -> left );
	damn ( root -> right );
	cin >> c;
}

void read() {
	int lines;
	cin >> lines;
	
	root = new el;
	
	damn ( root );
}

void solve() {
	int cases;
	string bau;
	int n;
	int i;
	double ans;
	
	cin >> cases;
	while ( cases -- ) {
		cin >> bau >> n;
		
	//	cout << bau << ' ' << n << endl;
		
		for (i = 1; i <= n; i++)
			cin >> a[i];
		
		el *p = root;
		ans = 1.;
		while ( p -> left != NULL ) {
			ans *= p -> w;
			for (i = 1; i <= n; i++)
				if ( a[i] == p -> f )
					break;
				
			if ( i <= n )
				p = p -> left;
			else
				p = p -> right;
		}
		
		printf ( "%lf\n" , ans * (p -> w) );
	}
}

int main() {
	int cases , i;
	
	cin >> cases;
	
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d:\n" , i );
		read();
		solve();
	}
	
	return 0;
}
