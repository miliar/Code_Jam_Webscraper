#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <fstream>

// Thanks for http://d.hatena.ne.jp/EmK/20071015
#define foreach(i,v) \
for(bool i##_bool2=true;i##_bool2;i##_bool2=false)\
for(const __typeof(v)& i##_foreach_##i=v;i##_bool2;i##_bool2=false)\
for(__typeof((i##_foreach_##i).begin())i##_iter=(i##_foreach_##i).begin(),i##_end=(i##_foreach_##i).end();\
i##_iter!=i##_end;i##_iter++)\
for(bool i##_bool=true;i##_bool;\
i##_bool = (i##_bool?i##_end=i##_iter,advance(i##_end,1),false:false))\
for(const __typeof(*i##_iter)& i=*i##_iter ; i##_bool ; i##_bool=false)

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;


int main( int c, char *v[] )
{
	string input;
	
	if( c == 1 )
		input = "sample.txt";
	else
		input = v[1];
	
	
	std::ifstream in( input.c_str() );
	std::ofstream out( (input + "_out.txt").c_str() );
	
	int T = 0;
	in >> T;
	
	for( int t = 0; t < T; t++ )
	{
		string result = "Draw";
		vector<string> line(4);
		
		in >> line[0];
		in >> line[1];
		in >> line[2];
		in >> line[3];
		
		vector<string> check;
		vector<string> checkO;
		string s;
		
		check.push_back(line[0]);
		check.push_back(line[1]);
		check.push_back(line[2]);
		check.push_back(line[3]);

		for( int i = 0; i < 4; i++ )
		{
			s.clear();
			s.push_back(line[0][i]);
			s.push_back(line[1][i]);
			s.push_back(line[2][i]);
			s.push_back(line[3][i]);
			check.push_back(s);
		}
		
		s.clear();
		s.push_back(line[0][0]);
		s.push_back(line[1][1]);
		s.push_back(line[2][2]);
		s.push_back(line[3][3]);
		check.push_back(s);
		
		s.clear();
		s.push_back(line[3][0]);
		s.push_back(line[2][1]);
		s.push_back(line[1][2]);
		s.push_back(line[0][3]);
		check.push_back(s);
		
		checkO = check;
		bool endflag = true;
		
		// check for X
		for( vector<string>::iterator it = check.begin(); it != check.end(); it++ )
		{
			for( string::iterator sit = it->begin(); sit != it->end(); sit++ )
			{
				if( *sit == 'T' )
					*sit = 'X';
				
				if( *sit == '.' )
					endflag = false;
			}
			
			if( *it == "XXXX" )
				result = "X won";
		}
		
		// check for O
		check = checkO;
		for( vector<string>::iterator it = check.begin(); it != check.end(); it++ )
		{
			for( string::iterator sit = it->begin(); sit != it->end(); sit++ )
			{
				if( *sit == 'T' )
					*sit = 'O';
			}
			
			if( *it == "OOOO" )
				result = "O won";
		}
		
		if( result == "Draw" && endflag == false )
			result = "Game has not completed";
		
		out << "Case #" << t + 1 << ": " << result << endl;
	}
	
	
	
	return EXIT_SUCCESS;
}