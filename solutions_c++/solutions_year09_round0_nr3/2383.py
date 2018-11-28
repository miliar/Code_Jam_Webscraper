#include <stdio.h>
#include <stdlib.h>
#include <string>

//#define DEBUG

#ifdef DEBUG
#endif

using namespace std;

const string welcome = "welcome to code jam";

int answer;


void recursive( string s, int index )
{
	if( welcome.length() <= index )
	{
#ifdef DEBUG
		puts("end of recursive");
#endif
		answer++;
		return;
	}

#ifdef DEBUG	
	printf("recursive : \"%s\", index = %d\n", s.c_str(), index );
#endif
	
	
	
	
	
	
	while(true)
	{
		char c = welcome[index];
#ifdef DEBUG
		printf("looking for %c\n", c);
#endif
		int pos = s.find(c);
		if( pos != string::npos )
		{
			recursive( s.substr( pos + 1 ), index + 1 );
			s[pos] = '*';
		}
		else
		{
			break;
		}		
	}

}

int main()
{
	FILE *in = fopen("input.txt", "rt");
	char line[8192];
	int N;
	
	if(in == NULL)
		return EXIT_FAILURE;
	
	
	fgets(line, sizeof(line), in);
	sscanf(line, "%d", &N );
	
#ifdef DEBUG
	printf("N = %d\n", N );
#endif
	
	for( int i = 0; i < N; i++ )
	{
		string characters;
		string formatted = "";
		
		fgets(line, sizeof(line), in);
		for( int i = 0; i < sizeof(line); i++ )
			if( line[i] == '\n' )
				line[i] = '\0';
		
		
		characters = line;
#ifdef DEBUG
		puts(characters.c_str());
#endif
		
		answer = 0;
		recursive(characters, 0);

		answer %= 1000;
		printf("Case #%d: %04d\n", i + 1, answer );
		answer = 0;		
	}
	
	
}