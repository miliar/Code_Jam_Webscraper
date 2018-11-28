
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

int N;
int M;
int Num;

class node
{
  public:
	std::vector<node *> childs;
	char path[200];
	int path_len;
  public:
	node ()
		: path_len( 0 )
		{ memset( path, 0, sizeof(path) ); }
	void set_path ( char * p )
		{
			memset( path, 0, sizeof(path) );
			strcpy( path, p );
			path_len = strlen( path );
		}
};

void create_path( char * buf, node * cur, bool inc )
{
	char tmp[200];
	int i;

	if ( strcmp( buf, cur->path ) == 0 )
		return;

	memset( tmp, 0, sizeof(tmp) );
	char * s = strchr( buf + cur->path_len, '/' );
	memcpy( tmp, buf, s-buf+1 );

	for ( i = 0; i < cur->childs.size(); i++ )
	{
		if ( strcmp( cur->childs[i]->path, tmp ) == 0 )
			return create_path( buf, cur->childs[i], inc );
	}

	node * p = new node;
	p->set_path( tmp );
	cur->childs.push_back( p );
	if ( inc )
		Num++;

	return create_path( buf, cur->childs.back(), inc );
}

void clear_path( node * cur )
{
	for ( int i = 0; i < cur->childs.size(); i++ )
		clear_path( cur->childs[i] );
	delete cur;
	return;
}


int test_round( ifstream& ifs, int case_no )
{
	int i;
	char buf[200];

	ifs >> N;
	ifs >> M;

	node * root = new node;
	root->set_path( "/" );

	for ( i = 0; i < N; i++ )
	{
		memset( buf, 0, sizeof(buf) );
		ifs >> buf;
		strcat( buf, "/" );
		create_path( buf, root, false );
	}

	Num = 0;
	for ( i = 0; i < M; i++ )
	{
		ifs >> buf;
		strcat( buf, "/" );
		create_path( buf, root, true );
	}

	clear_path( root );

	cout << "Case #" << case_no << ": " << Num << endl;

	return( 0 );
}

int main ( int argc, char * argv[] )
{
	int case_num;
	int i;

	if ( argc != 2 )
	{
		cout << "Usage: gtest <filename>" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	if (!ifs )
	{
		cout << "File does not exist" << endl;
		return( -1 );
	}

	ifs >> case_num;

	for ( i = 0; i < case_num; i++ )
	{
		if ( test_round( ifs, i+1 ) != 0 )
			return -1;
	}

	return( 0 );
}
