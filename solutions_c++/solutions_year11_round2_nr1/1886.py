#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<algorithm>

using namespace std;

typedef struct
{
	unsigned long long int N;
	char SCORE[100][100];
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
			p.N = _strtoui64( line.c_str() , NULL , 10 );
			for( int i = 0 ; i< p.N ; ++i )
			{
				getline( ifs , line );
				for( int j = 0 ; j < p.N ; ++j )
				{
					p.SCORE[i][j] = line.at(j);
				}
			}
			problems.push_back( p );
		}
		++line_num;
	}
	if( problems.size() != T ) return false;
	return true;
}

map<int,double> wpMap;

double WP(int i , PROBLEM& p)
{
	auto ret = wpMap.find(i);
	if( ret != wpMap.end() ) return ret->second;
	int win = 0;
	int lose = 0;
	for( int t = 0 ; t < p.N ; ++t )
	{
		if( p.SCORE[i][t] == '1' )
		{
			++win;
		}else if( p.SCORE[i][t] == '0' )
		{
			++lose;
		}
	}
	wpMap.insert(make_pair(i,(double)win / (win+lose)));
	return (double)win / (win+lose);
}

map<pair<int,int>,double> wpMap2;
double WP(int i , int j , PROBLEM& p)
{
	auto ret = wpMap2.find(make_pair(i,j));
	if( ret != wpMap2.end() ) return ret->second;

	int win = 0;
	int lose = 0;
	for( int t = 0 ; t < p.N ; ++t )
	{
		if( j != t )
		{
			if( p.SCORE[i][t] == '1' )
			{
				++win;
			}else if( p.SCORE[i][t] == '0' )
			{
				++lose;
			}
		}
	}
	wpMap2.insert(make_pair(make_pair(i,j),(double)win / (win+lose)));
	return (double)win / (win+lose);
}

map<int,double> owpMap;
double OWP(int i , PROBLEM& p)
{
	auto ret = owpMap.find(i);
	if( ret != owpMap.end() ) return ret->second;

	int count = 0;
	double sum = 0.0;
	for( int t = 0 ; t < p.N ; ++t )
	{
		if( p.SCORE[i][t] == '1' || p.SCORE[i][t] == '0' )
		{
			sum += WP(t,i,p);
			++count;
		}
	}
	owpMap.insert(make_pair(i,sum/(double)count));
	return sum/(double)count;
}

map<int,double> oowpMap;
double OOWP(int i, PROBLEM& p )
{
	int count = 0;
	double sum = 0.0;
	for( int t = 0 ; t < p.N ; ++t )
	{
		if( p.SCORE[i][t] == '1' || p.SCORE[i][t] == '0' )
		{
			sum += OWP(t,p);
			++count;
		}
	}
	oowpMap.insert(make_pair(i,sum/(double)count));
	return sum/(double)count;
}

double GetRPI(int i , PROBLEM& p)
{
	//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
	return 0.25 * WP(i,p) + 0.5 * OWP(i,p) + 0.25 * OOWP(i,p);
}

vector<double> solve( PROBLEM& p )
{
	vector<double> ans;
	for( int i = 0 ; i < p.N ; ++i )
	{
		double x = GetRPI(i,p);
		ans.push_back(x);
	}
	wpMap.clear();
	wpMap2.clear();
	owpMap.clear();
	oowpMap.clear();
	return ans;
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
		vector<double> x;
		PROBLEM problem = *itr;
		
		x = solve(problem);

		printf("Case #%d:\n",++count);
		for( auto itr = x.begin() ; itr != x.end() ; ++itr )
		{
			printf("%0.12f\n",*itr);
		}
	}

	return 0;
}