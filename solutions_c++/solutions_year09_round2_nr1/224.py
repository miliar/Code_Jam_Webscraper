#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <deque>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <sstream>
#include <cctype>

using namespace std;

struct tree_t {
	double p;
	string feature;
	tree_t* left;
	tree_t* right;
};


string x;
char tmp_string[10000];
set<string> feature;

tree_t* parse( int from, int to ) {
	int from1 = -1;
	int to1 = -1;

	for( int i = from; i <= to; ++i ) {
		if( x[i] == '(' ) {
			from1 = i;
			break;
		}
	}
	for( int i = to; i >= from; --i ) {
		if( x[i] == ')' ) {
			to1 = i;
			break;
		}
	}
	assert( from1 != -1 && to1 != -1 );
	tree_t* tmp = new tree_t;
	sscanf( x.c_str()+from1+1, "%lf", &tmp->p );
	tmp->left = tmp->right = 0;
	tmp->feature = "";
	
	for( int j = from1; j <= to1; ++j ) {
		if( 'a' <=  x[j] && x[j] <= 'z' ) {
			sscanf( x.c_str()+j, "%s", tmp_string );
			tmp->feature = string(tmp_string);
			int level = 0;
			int subtree = 0;
			int subtree_from = -1;
			for( int i = j+1; i < to1; ++i ) {
				if( x[i] == '(' ) {
					if( subtree_from == -1 ) {
						subtree_from = i;
					}
					++level;
					subtree = 1;
				} else if( x[i] == ')' ) {
					--level;
				}
				if( level == 0 && subtree ) {
					tmp->left = parse( subtree_from, i );
					tmp->right = parse( i+1, to1-1 );
					break;
				}
			}
			break;
		}
	}
	
	return tmp;
}



double evalr( const tree_t* t ) {
	if( t->feature.size() == 0 ) {
		return t->p;
	}
	if( feature.find( t->feature ) != feature.end() ) {
		return t->p * evalr( t->left );
	}
	return t->p * evalr( t->right );
}

int main() {
	int cases;
	string s;
	string animal;
	int n_animal;
	
	getline( cin, s );
	cases = atoi( s.c_str() );
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		int L;
		getline( cin, s );
		L = atoi( s.c_str() );
		x = "";
		for( int i = 0; i < L; ++i ) {
			getline( cin, s );			
			x += s + " ";
		}
		
		tree_t* root = parse( 0, x.size()-1 );
		
		cout << "Case #" << caseid << ":\n";
		
		getline( cin, s );
		int A = atoi( s.c_str() );
		for( int i = 0; i < A; ++i ) {
			getline( cin, s );
			istringstream str( s );
			str >> animal >> n_animal;
			feature.clear();
			for( int j = 0; j < n_animal; ++j ) {
				str >> s;
				feature.insert( s );
			}
			printf( "%0.20f\n", evalr( root ) );
		}		
		
		
	}
	return 0;
}
