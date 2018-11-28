#include <stdio.h>
#include <string.h>

#include <set>
#include <map>
#include <vector>

//#define DEBUG



static int pow( int x, int n )
{
	int result = x;
	
	if( n == 0 )
		return 1;
	
	for( int i = 1; i < n; i++ )
	{
		result *= x;
	}
	
	return result;
}


static long long each_line( const char *in )
{
	std::set<char> base_count;	
	std::map<char, int> replace_map;
	std::vector<int> message;
	
	int base_n;
	
	const int num[] = { 1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38 };
	int num_count = 0;
	
	int length = strlen(in);
	
	for( int i = 0; i < length; i++ )
		base_count.insert(in[i]);

	base_n = (int)base_count.size();

	if( base_n == 1 )
		base_n = 2;

#ifdef DEBUG
	
	puts(in);
	printf("There are %d characters\n", (int)base_count.size() );
	printf("There are %d characters\n", base_n );
	
	
#endif	
	
	// create map
	for( int i = 0; i < length; i++ )
	{
		std::map<char, int>::iterator p = replace_map.find(in[i]);
		
		// a new character
		if( replace_map.end() == p )
		{
			int n = num[num_count++];
			replace_map.insert( std::pair<char, int>( in[i], n ) );

#ifdef DEBUG
			printf("DEBUG : %c -> %d\n", in[i], n );
#endif	
			
			
			continue;
		}
	}
	
	// create replaced number
	for( int i = 0; i < length; i++ )
	{
		std::map<char, int>::iterator p = replace_map.find(in[i]);
		
		if( replace_map.end() != p )
		{
			message.push_back(p->second);
		}
	}
	
	int c = 0;
	long long sum = 0;
	for( std::vector<int>::reverse_iterator it = message.rbegin(); it != message.rend(); it++ )
	{
		int zz = *it * pow( base_n, c++ );
		
#ifdef DEBUG
		printf("%d\n", zz );
#endif	
		sum += zz;
	}
#ifdef DEBUG
	puts("---------------------");
#endif	

	return sum;
}


int main( int c, char *v[] )
{	
#ifdef DEBUG
	printf( "%lld\n", each_line("102345678") );
	return 0;
#endif	
	
	if( c != 1 && c != 2 )
	{
		fprintf(stderr, "args must be 1 or 2\n");
		return EXIT_FAILURE;
	}
	
	FILE *in;
	
	if( c == 1 )
		in = fopen( "input.txt", "rt" );
	else 
		in = fopen( v[1], "rt" );
	
	
	if( in == NULL )
	{
		fprintf(stderr, "file not found : %s\n", v[1]);
		return EXIT_FAILURE;
	}
	
	char line[1024];
	int T;
	
	fgets( line, sizeof(line), in );
	sscanf( line, "%d", &T );
	
//	printf("T = %d\n", T );
	
	for( int i = 0; i < T; i++ )
	{
		fgets( line, sizeof(line), in );
		
		for( int j = 0; j < sizeof(line); j++ )
			if( line[j] == 0x0a || line[j] == 0x0d )
			{
				line[j] = '\0';
				break;
			}
		
		printf( "Case #%d: %lld\n", i + 1, each_line(line) );
	}
}