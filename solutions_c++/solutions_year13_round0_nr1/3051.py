#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <numeric>
using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define IREP(it,array) for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it)
#define PREP(it,array) for(vector<P>::iterator it=array.begin(); it!=array.end(); ++it)
#define SREP(it,array) for(vector<string>::iterator it=array.begin(); it!=array.end(); ++it)

#define MP       make_pair
#define PB       push_back
#define ALL(x)   (x).begin(),(x).end()

const int INF = 1<<29;
const double EPS = 1e-9;
double zero(double d){
  return d < EPS ? 0.0 : d;
}

typedef long long LL;
typedef pair<int,int> P;


bool isWon( char board[4][4], char player ){
  REP(i,4){
    if( board[i][0] == board[i][1] && 
	board[i][1] == board[i][2] &&
	board[i][2] == board[i][3] &&
	board[i][3] == player )
      return true;
  }

  REP(j,4){
    if( board[0][j] == board[1][j] && 
	board[1][j] == board[2][j] && 
	board[2][j] == board[3][j] && 
	board[3][j] == player )
      return true;
  }

  if( board[0][0] == board[1][1] && 
      board[1][1] == board[2][2] && 
      board[2][2] == board[3][3] && 
      board[3][3] == player )
    return true;

  if( board[0][3] == board[1][2] && 
      board[1][2] == board[2][1] && 
      board[2][1] == board[3][0] && 
      board[3][0] == player )
    return true;

  return false;
}


int main()
{
  cout.setf(ios::fixed, ios::floatfield);
  cout.precision(7);


  int N;
  cin >> N;
  REP(targetNum,N){

    char board[4][4];
    bool isT = false;
    P tPos;
    REP(i,4){
      REP(j,4){
	char c;
	cin>>c;
	board[i][j] = c;

	if( c=='T' ){
	  isT = true;
	  tPos = P(i,j);
	}
      }
    }

    bool isXwon = false;
    bool isOwon = false;

    // change T into X
    if(isT)
      board[tPos.first][tPos.second] = 'X';
    isXwon = isWon( board, 'X' );

    // change T into O
    if(isT)
      board[tPos.first][tPos.second] = 'O';
    isOwon = isWon( board, 'O' );

    string res="";

    if( isXwon && !isOwon)
      res = "X won";
    else if( !isXwon && isOwon )
      res = "O won";

    else if( isXwon && isOwon )
      res = "Draw";

    else if( !isXwon && !isOwon ){
      res = "Draw";
      bool isEmptyPoint = false;
      REP(i,4){
	REP(j,4){
	  if( board[i][j] == '.' ){
	    isEmptyPoint = true;
	    res = "Game has not completed";
	    break;
	  }
	}
	if(isEmptyPoint)
	  break;
      }
    }

    cout << "Case #" << targetNum+1 << ": " ;
    cout << res;
    cout << endl;
  }



  return 0;
}
