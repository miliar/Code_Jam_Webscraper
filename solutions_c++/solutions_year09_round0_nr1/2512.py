#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;


class pattern_match
{
public:
	pattern_match( string in );
	~pattern_match(){};
	
	bool match( string in );

private:
	int num;
	string character[15];
	
};



pattern_match::pattern_match( string in )
{
	int index = 0;
	
	for( int i = 0; i < in.length(); i++ )
	{
		char c[2];
		c[1] = '\0';
		c[0] = in[i];
		
		// is alphabet?
		if( 'a' <= c[0] && c[0] <= 'z' || 'A' <= c[0] && c[0] <= 'Z' )
		{
			character[index++] = c;
			continue;
		}
		
		if( c[0] == '(' )
		{
			c[0] = in[++i];
			
			character[index] = "";
			while( c[0] != ')' )
			{
				if( c[0] != ')' )
					character[index].append(c);
				c[0] = in[++i];
			}			
			index++;
			continue;
		}
		
		if( c[0] == '\0' || c[0] == 0x0a || c[0] == 0x0d )
			break;
		
		printf("Unknown token : %c(%x)", c[0], c[0] );
		exit(EXIT_FAILURE);
	}

//	printf("num = %d\n", index);
	num = index;

//	for( int i = 0; i < num; i++ )
//		puts( character[i].c_str() );

}



bool pattern_match::match( string in )
{
	for( int i = 0; i < in.length(); i++ )
	{
		char c[2];
		c[0] = in[i];
		c[1] = '\0';
		int loc = character[i].find( c );
		if( loc != string::npos )
			continue;
		else 
			return false;
	}
	
	return true;
}




int main()
{
	FILE *input = fopen("input.dat", "rt");
	char line[1024];
	int L, D, N;
	
	/* -------------------------------------------------------------
	 
	------------------------------------------------------------- */
	if( input == NULL )
		return EXIT_FAILURE;

	fgets(line, sizeof(line), input);
	sscanf( line, "%d %d %d", &L, &D, &N);
	printf("L = %d, D = %d, N = %d\n", L, D, N);

	/* -------------------------------------------------------------
	 
	 ------------------------------------------------------------- */
	vector<string> words;
	
	puts("");
	puts("word");
	for( int i = 0; i < D; i++ )
	{
		fgets(line, sizeof(line), input);
		
		for( int i = 0; i < sizeof(line); i++ )
			if( line[i] == '\n' )
				line[i] = '\0';
		
		words.push_back(line);
	}
	
	for( vector<string>::iterator it = words.begin(); it != words.end(); it++ )
	{
		printf("%s\n", it->c_str() );
	}
	

	/* -------------------------------------------------------------
	 
	 ------------------------------------------------------------- */
	puts("");
	puts("pattern");
	for( int i = 0; i < N; i++ )
	{
		int count = 0;
		
		fgets(line, sizeof(line), input);
		pattern_match m( line );
		
		for( vector<string>::iterator it = words.begin(); it != words.end(); it++ )
		{
			if( m.match( *it ) == true )
				count++;
		}
		printf("Case #%d: %d\n", i + 1, count );
		
	}
	
	puts("");
	return EXIT_SUCCESS;
}



