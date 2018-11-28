#include <stdio.h>
#include <list>
#include <vector>
using namespace std;

template<class T> inline void swap( T &a, T &b ) { T tmp = a; a = b; b = tmp; }


FILE*	of = NULL;
FILE*	sf = NULL;

#define	FolderName_max 200

class Folder {
public:

	Folder	( char* _name ) {
		strcpy( name, _name );
	}

	char name[FolderName_max];

	list<Folder>	sub;

	Folder*	find( const char* sz ) {
		list<Folder>::iterator it = sub.begin();

		for( ; it != sub.end(); it++ ) {
			if( strcmp( it->name, sz ) == 0 ) return &*it;
		}
		return NULL;
	}

};

Folder	root("/");

int folder_count = 0;

int mk_folder( char* name ) {
//	printf(" name= %s\n", name );

	if( name == 0 ) return 0;

	vector< char* > sub;

	char *p = name+1;
	for(;;) {
		char* n = strchr( p, '/' );
		if( !n ) {
			sub.push_back( p );
			break;
		}
		*n = 0;
		sub.push_back( p );
		p = n+1;
	}

	Folder* f = &root;
	unsigned i;
	for( i=0; i<sub.size(); i++ ) {
//		printf("%s\n", sub[i] );

		Folder * p = f->find( sub[i] );
		if( p ) {
//			printf("found %s\n", p->name );
			f = p;
		}else{
//			printf("          create %s\n", sub[i] );
			folder_count++;
			f->sub.push_back( Folder( sub[i] ) );
			f = &f->sub.back();
		}

	}

	return 0;
}

int do_case( int case_id ) {
	int N, M;

	root.sub.clear();

	folder_count = 0;

	fscanf( sf, "%d %d", &N, &M );


	int i;
	for( i=0; i<N; i++ ) {
		char sz[FolderName_max];
		fscanf( sf, "%s", sz );
		mk_folder( sz );
	}

	int old = folder_count;

//	printf("----------- \n");

	for( i=0; i<M;i++ ) {
		char sz[FolderName_max];
		fscanf( sf, "%s", sz );
		mk_folder( sz );
	}

	int result = folder_count - old;

	fprintf( of, "Case #%d: %d\n", case_id+1, result );
	return 0;
}


int main() {
	char* in_filename = "A-large.in";
	char	out_filename[128];

	sprintf( out_filename, "%s.out", in_filename );

	sf = fopen( in_filename,  "r" );	if( !sf ) return -1;
	of = fopen( out_filename, "w" );	if( !of ) return -1;

	int i;
	int n_case;
	fscanf( sf, "%d", &n_case );

	for( i=0; i<n_case; i++ ) {
		do_case(i);
	}

	fclose( sf );
	fclose( of );

	printf("--program end--\n" );
	getchar();
	return 0;
}