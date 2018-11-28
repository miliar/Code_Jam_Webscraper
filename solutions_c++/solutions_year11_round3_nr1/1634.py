#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<algorithm>

using namespace std;

typedef struct
{
	long long int R;
	long long int C;
	char BOARD[50][50];

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
			auto split_line = split(line," ");
			p.R = _strtoi64( split_line[0].c_str() , NULL , 10 );
			p.C = _strtoi64( split_line[1].c_str() , NULL , 10 );
			
			for( int i = 0 ; i< p.R ; ++i )
			{
				getline( ifs , line );
				for( int j = 0 ; j< p.C ; ++j )
				{
					p.BOARD[i][j] = line.at(j);
				}
			}
			problems.push_back( p );
		}
		++line_num;
	}
	if( problems.size() != T ) return false;
	return true;
}


bool solve( PROBLEM& p , vector<string>& ans )
{
	for( int i = 0 ; i < p.R - 1 ; ++i )
	{
		for( int j = 0 ; j < p.C - 1 ; ++j )
		{
			if( p.BOARD[i][j] == '#' && p.BOARD[i+1][j] == '#' && 
				p.BOARD[i][j+1] == '#' && p.BOARD[i+1][j+1] == '#' )
			{
				 p.BOARD[i][j] = '/';
				 p.BOARD[i+1][j] = '\\';
				 p.BOARD[i][j+1] = '\\';
				 p.BOARD[i+1][j+1] = '/';
			}
		}
	}
	
	for( int i = 0 ; i < p.R; ++i )
	{
		for( int j = 0 ; j < p.C ; ++j )
		{
			if( p.BOARD[i][j] == '#' ) 
			{
				return false;
			}
		}
		ans.push_back( string( p.BOARD[i],p.C ) );
	}
	return true;
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
		bool x;
		vector<string> ans;
		PROBLEM problem = *itr;
		
		x = solve(problem,ans);

		printf("Case #%d:\n",++count);
		if( x )
		{
			for( auto itr = ans.begin() ; itr != ans.end() ;++itr)
			{
				printf("%s\n",itr->c_str());
			}
		}else
		{
				printf("Impossible\n");
		}
	}

	return 0;
}