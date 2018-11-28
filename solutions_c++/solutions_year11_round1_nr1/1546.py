#include<vector>
#include<string>
#include<fstream>
#include<algorithm>

using namespace std;

typedef struct
{
	int N;
	int Pd;
	int Pg;
}PROBLEM;

vector<string> split( string& line , const string& sep )
{
	int pos[2];
	pos[0] = pos[1] = 0;
	vector<string> split_line;
	while( ( pos[1] = line.find(sep,pos[0]) ) != string::npos )
	{
		string sub_line = line.substr( pos[0] , pos[1] - pos[0] );
		split_line.push_back(sub_line);
		pos[0] = pos[1] + 1;
	}
	string sub_line = line.substr( pos[0] );
	split_line.push_back(sub_line);
	return split_line;
}

bool read_problem( const char *fname , vector<PROBLEM>& problems )
{
	fstream ifs;
	ifs.open( fname );

	if( !ifs.is_open() ) return false;

	std::string line;
	int T = 0;
	int line_num = 0;
	while( getline( ifs , line ) )
	{
		if( line_num == 0 )
		{
			T = strtoul( line.c_str() , NULL , 10);
		}else
		{
			PROBLEM p;
			auto split_line = split( line , " " );
			if( split_line.size() != 3 ) return false;
			p.N = strtoul( split_line[0].c_str() , NULL , 10 );
			p.Pd = strtoul( split_line[1].c_str() , NULL , 10 );
			p.Pg = strtoul( split_line[2].c_str() , NULL , 10 );
			problems.push_back( p );
		}
		++line_num;
	}
	if( problems.size() != T ) return false;
	return true;
}

long long int solve( PROBLEM& p )
{
	if( ( p.Pd != 0 && p.Pg == 0 ) || ( p.Pd != 100 && p.Pg == 100 ) ) return 0;
	if( p.Pg == 0 && p.Pd == 0 ) return 1;
	if( p.Pd % 2 == 0 && 100 / 2 <= p.N ) return 1;
	if( p.Pd % 4 == 0 && 100 / 4 <= p.N ) return 1;
	if( p.Pd % 5 == 0 && 100 / 5 <= p.N ) return 1;
	if( p.Pd % 10 == 0 && 100 / 10 <= p.N ) return 1;
	if( p.Pd % 20 == 0 && 100 / 20 <= p.N ) return 1;
	if( p.Pd % 25 == 0 && 100 / 25 <= p.N ) return 1;
	if( p.Pd % 50 == 0 && 100 / 50 <= p.N ) return 1;
	if( p.Pd % 100 == 0 && 100 / 100 <= p.N ) return 1;
	return 0;
}

int main(int argc, char *argv[])
{
	int T;
	vector<PROBLEM> problems;
	if( argc != 2 ) return -1;
	if( !read_problem( argv[1] , problems ) ) return -2;

	int count = 0;
	for( auto itr = problems.begin(); itr != problems.end() ; ++itr )
	{
		long long int x;
		PROBLEM problem = *itr;
		
		x = solve(problem);

		if( x )
		{
			printf("Case #%d: Possible\n",++count);
		}else
		{
			printf("Case #%d: Broken\n",++count);
		}
	}

	return 0;
}