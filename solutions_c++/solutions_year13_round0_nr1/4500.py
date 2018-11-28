/* k_____k */

#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<ctime>
#include<cctype>
#include<cassert>
#include<climits>
#include<cerrno>
#include<cfloat>
#include<ciso646>
#include<clocale>
#include<csetjmp>
#include<csignal>
#include<cstdarg>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cwchar>
#include<cwctype>

//containers
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<complex>
#include<string>
#include<stack>
#include<bitset>
#include<istream>
#include<valarray>

//IOs
#include<iostream>
#include<sstream>
#include<iomanip>
#include<fstream>
#include<exception>
#include<ios>
#include<iosfwd>
#include<ostream>
#include<iterator>
#include<stdexcept>
#include<streambuf>


//algorithm & miscellaneous
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<limits>
#include<locale>
#include<memory>
#include<new>

// My Terms
#define pb push_back
#define mp make_pair
#define ins insert
#define fir first
#define sec second
#define PRINT(x)        cout << #x << " " << x << endl
#define pi acos(-1)
#define ll long long
#define EM empty()
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define fill(a,v)     memset(a, v, sizeof(a))

using namespace std;

unsigned long long mod=1000000007;

bool done,emp_cell;
string winner;
vector<string> board;
void check_rows(){
	for(int i=0;i<sz(board);i++){
		if(board[i][0]=='X' or board[i][0]=='T')
			if(board[i][1]=='X' or board[i][1]=='T')
				if(board[i][2]=='X' or board[i][2]=='T')
					if(board[i][3]=='X' or board[i][3]=='T')
						done=true,winner="X won";
		if(board[i][0]=='O' or board[i][0]=='T')
			if(board[i][1]=='O' or board[i][1]=='T')
				if(board[i][2]=='O' or board[i][2]=='T')
					if(board[i][3]=='O' or board[i][3]=='T')
						done=true,winner="O won";
	}
	return ;
}
void check_cols(){
	for(int i=0;i<sz(board);i++){
		if(board[0][i]=='X' or board[0][i]=='T')
			if(board[1][i]=='X' or board[1][i]=='T')
				if(board[2][i]=='X' or board[2][i]=='T')
					if(board[3][i]=='X' or board[3][i]=='T')
						done=true,winner="X won";
		if(board[0][i]=='O' or board[0][i]=='T')
			if(board[1][i]=='O' or board[1][i]=='T')
				if(board[2][i]=='O' or board[2][i]=='T')
					if(board[3][i]=='O' or board[3][i]=='T')
						done=true,winner="O won";
	}
	return ;
}
void check_diag1(){
	if(board[0][0]=='X' or board[0][0]=='T')
		if(board[1][1]=='X' or board[1][1]=='T')
			if(board[2][2]=='X' or board[2][2]=='T')
				if(board[3][3]=='X' or board[3][3]=='T')
					done=true,winner="X won";
	if(board[0][0]=='O' or board[0][0]=='T')
		if(board[1][1]=='O' or board[1][1]=='T')
			if(board[2][2]=='O' or board[2][2]=='T')
				if(board[3][3]=='O' or board[3][3]=='T')
					done=true,winner="O won";
	return ;
}
void check_diag2(){
	if(board[0][3]=='X' or board[0][3]=='T')
		if(board[1][2]=='X' or board[1][2]=='T')
			if(board[2][1]=='X' or board[2][1]=='T')
				if(board[3][0]=='X' or board[3][0]=='T')
					done=true,winner="X won";
	if(board[0][3]=='O' or board[0][3]=='T')
		if(board[1][2]=='O' or board[1][2]=='T')
			if(board[2][1]=='O' or board[2][1]=='T')
				if(board[3][0]=='O' or board[3][0]=='T')
					done=true,winner="O won";
	return ;
}
int main(){
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++){
		done=false,emp_cell=false;
		int _times=4;string inp;
		while(_times--){
			cin>>inp;
			board.pb(inp);
			if(inp.find('.')!=-1)
				emp_cell=true;
		}
		check_rows();
		if(!done)check_cols();
		if(!done)check_diag1();
		if(!done)check_diag2();
		if(!done){
			if(!emp_cell)
				winner="Draw";
			else 
				winner="Game has not completed";
		}	
		printf("Case #%d: ",i);
		cout<<winner<<"\n";
		board.clear();	
	}
	return 0;
}


/*
This isn't my field,
still i code to show,
anyone can do it ^_^
*/


