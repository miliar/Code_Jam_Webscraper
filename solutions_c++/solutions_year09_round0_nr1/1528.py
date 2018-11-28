#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std ;

#define fv(i, s, n) for ( int i = s ; i < n ; i++ )
#define fb(i, n) fv (i, 0, n)
#define fe(i, n) fb (i, n.size())
#define pb push_back
#define all(n) n.begin(), n.end()
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)

const char E = 254 ;
const char F = 255 ;

#define lim 1000

struct trie ;
trie *err ;

struct trie
{
	char c ;
	list <trie> l ;
	
	void add ( char *n )
	{
		if ( !c ) return ;
		
		fi (i, l) if ( i->c == n[0] ) { i->add(n + 1) ; return ; }
		l.pb ( trie( n ) ) ;
	}
	
	trie *se ( char t )
	{
		fi (i, l) if ( i->c == t ) return &*i ;
		return err ;
	}
	
	trie ( char *p ) : c(*p) { if ( c ) add(p + 1) ; }
	trie ( char  p ) : c( p) {} ;
	trie() : c( F ) {} ;
} ;

trie as(E) ;

int se ( char *n, trie *p )
{
	if ( p->c == E ) return 0 ;
	if ( *n == 0 ) { return 1 ; }
	if ( *n != '(' ) return se(n + 1, p->se(*n) ) ;
	
	int r = 0 ;
	
	char v[lim] ;
	sscanf (n, "(%[^)])", v) ;

	int h = strlen(v) + 2 ;
	for ( int i = 0 ; v[i] ; i++ ) r += se( n + h, p->se(v[i]) ) ;
	return r ;
}

int main()
{
	ifstream in ("Alien.in") ;
	ofstream out ("Alien.out") ;
	
	trie q ;
	
	int l, d, n ;
	in >> l >> d >> n ;
	
	err = &as ;
	
	fb (i, d)
	{
		char a[20] ; in >> a ;
		q.add (a) ;
	}
	
	fb (i, n)
	{
		char h[lim] ; in >> h ;
		cout << "Case #" << i + 1 << ": " << se(h, &q) << endl ;
	}
	
	return 0 ;
}
