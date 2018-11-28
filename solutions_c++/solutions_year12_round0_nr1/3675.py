// 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'
// "a zoo" will become "y qee".

/* 3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv


Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
*/

#include <iostream>
#include <fstream>

using namespace std;

fstream fin;
fstream fout;
int case_num = 0;

class translator
{
public:
	char map[26];
public:
	void in( char *gl, char *en );
	void tran( char *in );
};

void translator::in( char *gl, char *en )
{
	int lenGl = strlen(gl);
	int lenEn = strlen(en);

	if( lenGl != lenEn )
		return;

	for( int i=0; i<lenGl; i++ )
	{
		if( gl[i] >= 'a' && gl[i] <= 'z' )
			this->map[ gl[i] - 'a' ] = en[i];
	}
}

void translator::tran( char *in )
{
	int lenIn = strlen(in);

	char *out = new char[lenIn+1];

	memset( out, 0, lenIn+1 );

	if( out == NULL )
		return;

	for( int i=0; i<lenIn; i++ )
	{

		if( in[i] == ' ' )
			out[i] = ' ';
		else
			out[i] = map[ in[i] - 'a' ];
	}

	fout << "Case #" << ++case_num << ": " << out << endl;

	delete out;
}


int main()
{
	translator t;
	memset( t.map, 0, _countof(t.map) );

	char *out = NULL;

	t.in( "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand" );
	t.in( "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities" );
	t.in( "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up" );
	t.in( "qz" , "zq" );
	
	char buf[256] = {0, };
	

	fin.open( "A-small-attempt1.in", ios_base::in );
	fout.open("a.out" , ios_base::out );

	//t.tran( "ejp mysljylc kd kxveddknmc re jsicpdrysi" );

	fin.getline(buf, 256);

	int count = 0;
	count = atoi(buf);

	for(int i=0; i<count; i++)
	{
		fin.getline(buf, 256);
		t.tran(buf);
	}

	return 0;
}