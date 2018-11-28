#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <set>
#include <sstream>
using namespace std;

int T;
int b[16];
string s;

inline int make( int n, int base ){
	int n1, k;
	set<int> st;
	while( 1 ){	
		n1 = n;
		k = 0;
		while( n1 ){
		//cout << n1 << endl;
			k += (n1%base)*(n1%base);
			n1 /= base;
			}
		n = k;
		//cout << n << " " << base << endl;
		if( st.find(n)!=st.end() ) return -1;
		st.insert(n);
		if( n<2 ) return 1;
		}
	return n;
	}

void input () {
	scanf ("%d\n",&T);
	for(int i=0; i<T; ++i) {
		getline ( cin, s );
		b[0] = 0;
		stringstream in(s);
		int q;
		while( in>>q ) b[++b[0]] = q;
		for(int k=2; ; ++k){
			bool key = true;
			//printf ("checking: %d\n",k);
			for(int j=1; j<=b[0]; ++j) {
				int p = make(k,b[j]);
				if( p!=1 ) { key=false; break; }
				}
			if( key ) { printf ("Case #%d: %d\n",i+1,k); break; }
			}
		}
}

int main (void) {
	input ();
}
