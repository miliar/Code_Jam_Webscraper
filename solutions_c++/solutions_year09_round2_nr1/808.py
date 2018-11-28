//

#include <stdlib.h>
#include <iostream>
#include <map>
#include <string>

using namespace std;
using namespace __gnu_cxx;

map<string,int> features;
int featureCount = 0;

struct Tree {
	
	double value;
	bool leaf;
	int feature;
	Tree *left, *right;
	
	Tree( double value ) {
		
		this->value = value;
		leaf = true;
	}
};

void constructTree( Tree **root ) {
	
	scanf( " ( " );
	double val = -1;
	scanf( "%lf", &val );
	
	*root = new Tree( val );
	
	scanf( " " );
	
	char next = getc( stdin );
	
	if( next == ')' ) {
		
		return;
	}
	
	ungetc( next, stdin );
	
	(*root)->leaf = false;
	
	const char *feature = new char[11];
	scanf( " %s ", feature );
	features[feature] = featureCount;
	(*root)->feature = featureCount;
	++ featureCount;
	
	constructTree( &((*root)->left) );
	constructTree( &((*root)->right) );
	
	scanf( " ) " );
}

double calc( Tree *root, int *features, int n ) {
	
	if( root->leaf ) {
		
		return root->value;
	}
	
	for( int i = 0; i < n; i ++ ) {
		
		if( features[i] == root->feature ) {
			
			return root->value * calc( root->left, features, n );
		}
	}
	
	return root->value * calc( root->right, features, n );
}

int main() {
	
	Tree *root;
	
	int N;
	scanf( "%d", &N );
	
	for( int i = 1; i <= N; i ++ ) {
		
		int L;
		scanf( "%d", &L );
		
		featureCount = 0;
		features.clear();
		constructTree( &root );
		
		printf( "Case #%d:\n", i );
		
		int A;
		scanf( "%d", &A );
		
		for( int j = 0; j < A; j ++ ) {
			
			char *animal = new char[11];
			scanf( "%s", animal );
			
			int n;
			scanf( "%d", &n );
			
			int *thesefeatures = new int[n];
			char *feature = new char[11];
			
			for( int k = 0; k < n; k ++ ) {
				
				scanf( "%s", feature );
				
				if( features.find( feature ) == features.end() ) {
					
					thesefeatures[k] = -1;
				}
				
				else {
					
					thesefeatures[k] = features[feature];
				}
			}
			
			//sort( thesefeatures, thesefeatures+n );
			printf( "%.8lf\n", calc( root, thesefeatures, n ) );
		}
		
	}
	
	return 0;
}
