#include<stdio.h>
#include<vector>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>

using namespace std;

typedef struct
{
	char BOARD[4][4];


	int XT(int i,int j)
	{
		return (BOARD[i][j] == 'X' || BOARD[i][j] == 'T') ? 1 : 0;
	}

	int OT(int i,int j)
	{
		return (BOARD[i][j] == 'O' || BOARD[i][j] == 'T') ? 1 : 0;
	}

	int XOT(int i,int j)
	{
		return (BOARD[i][j] != '.') ? 1 : 0;
	}
}PROBLEM;

vector<string> split( const string& line , const string& sep )
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

	int T = 0;
	try{
		std::string line;
		int line_num = 0;
		while( getline( ifs , line ) ){
			if( line_num == 0 )	{
				T = strtoul( line.c_str() , NULL , 10);
			}else{
				PROBLEM p;

				for (int i = 0; i < 4; i++)
				{
					for (int j = 0; j < 4; j++)
					{
						p.BOARD[i][j] = line[j];
					}
					getline( ifs , line );
				}
				problems.push_back(p);
			}
			++line_num;
		}
	}catch(...){
		return false;
	}
	if( problems.size() != T ) return false;
	return true;
}

int bit(int a,int b, int c, int d)
{
	return (a << 3) + (b << 2) + (c << 1) + d;
}

int solve(PROBLEM &p)
{
	int b[3][10];
	for(int i=0;i<10;++i){
		if(i<4){
			b[0][i] = bit(p.XT(0,i) , p.XT(1,i) , p.XT(2,i) , p.XT(3,i) );
			b[1][i] = bit(p.OT(0,i) , p.OT(1,i) , p.OT(2,i) , p.OT(3,i) );
			b[2][i] = bit(p.XOT(0,i) , p.XOT(1,i) , p.XOT(2,i) , p.XOT(3,i) );
		}else if(i<8){
			int t=i-4;
			b[0][i] = bit(p.XT(t,0) , p.XT(t,1) , p.XT(t,2) , p.XT(t,3) );
			b[1][i] = bit(p.OT(t,0) , p.OT(t,1) , p.OT(t,2) , p.OT(t,3) );
			b[2][i] = bit(p.XOT(t,0) , p.XOT(t,1) , p.XOT(t,2) , p.XOT(t,3) );
		}else{
			if(i==9){
				b[0][i] = bit(p.XT(0,0) , p.XT(1,1) , p.XT(2,2) , p.XT(3,3) );
				b[1][i] = bit(p.OT(0,0) , p.OT(1,1) , p.OT(2,2) , p.OT(3,3) );
				b[2][i] = bit(p.XOT(0,0) , p.XOT(1,1) , p.XOT(2,2) , p.XOT(3,3) );
			}else{
				b[0][i] = bit(p.XT(3,0) , p.XT(2,1) , p.XT(1,2) , p.XT(0,3) );
				b[1][i] = bit(p.OT(3,0) , p.OT(2,1) , p.OT(1,2) , p.OT(0,3) );
				b[2][i] = bit(p.XOT(3,0) , p.XOT(2,1) , p.XOT(1,2) , p.XOT(0,3) );
			}
		}
	}
	bool ghnc = true;
	for(int i=0;i<10;++i){
		if(b[0][i]==15) return 2;
		if(b[1][i]==15) return 3;
		if(b[2][i]==15) {
			ghnc = false;
		}
	}
	if(ghnc) return 0;
	return 1;
}

int main(int argc, char *argv[])
{
	vector<PROBLEM> problems;
	if( argc != 2 ) return -1;
	if( !read_problem( argv[1] , problems ) ) return -2;
	
	int count = 0;
	for( auto itr = problems.begin(); itr != problems.end() ; ++itr )
	{
		PROBLEM &problem = *itr;
		
		auto x = solve(problem);

		if(x==0){
			printf("Case #%d: Game has not completed\n",++count);
		}else if(x == 1){
			printf("Case #%d: Draw\n",++count);
		}else if(x == 2){
			printf("Case #%d: X won\n",++count);
		}else if(x == 3){
			printf("Case #%d: O won\n",++count);
		}
	}

	return 0;
}
