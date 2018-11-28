#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>

#define FOR(i, a, b) for (int i = (a);i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
using namespace std;

char field[4][4];
int MAX_field = 4;
int judge_num = 4;

/* 0 = no finish 1 = 1 win 2 = 2 win*/

int judge(){
  int one = 0;/*O*/
  int two = 0;/*X*/
  bool continue_flag = false;

  REP(i,MAX_field){
    one =0;
    two =0;
  REP(j,MAX_field){ /*yoko*/
       char cell = field[j][i];
	switch(cell){
	case('O'): 
	  if (++one == judge_num) return 1;
	  break;
	case('X'): 
	  if (++two == judge_num) return 2;
	  break;
	case('T'):
	  if (++one == judge_num) return 1;
	  if (++two == judge_num) return 2;
	  break;
	default:
	  continue_flag = true;
	  break;
	}
  }
  }

REP(i,MAX_field){
    one =0;two=0;
  REP(j,MAX_field){ /*tate*/
       char cell = field[i][j];
	switch(cell){
	case('O'): 
	  if (++one == judge_num) return 1;
	  break;
	case('X'): 
	  if (++two == judge_num) return 2;
	  break;
	case('T'):
	  if (++one == judge_num) return 1;
	  if (++two == judge_num) return 2;
	  break;
	default:
	  continue_flag = true;
	  break;
	}
  }
  }

one=0;two=0;
REP(i,MAX_field)/*migisita naname*/
      {
	char cell = field[i][i];
	switch(cell){
	case('O'): 
	  if (++one == judge_num) return 1;
	  break;
	case('X'): 
	  if (++two == judge_num) return 2;
	  break;
	case('T'):
	  if (++one == judge_num) return 1;
	  if (++two == judge_num) return 2;
	  break;
	default:
	  break;
	} 
 }
one=0;two=0;
REP(i,MAX_field)/*hidarisita naname*/
      {
	char cell = field[MAX_field -1 -i][i];
	switch(cell){
	case('O'): 
	  if (++one == judge_num) return 1;
	  break;
	case('X'): 
	  if (++two == judge_num) return 2;
	  break;
	case('T'):
	  if (++one == judge_num) return 1;
	  if (++two == judge_num) return 2;
	  break;
	default:
	  break;
	} 
 }


 if (continue_flag) return 0;
 else return 3;
}

void print_field(){
  REP(i,MAX_field){
    REP(j,MAX_field){
    cout << field[j][i];
      }
    cout << endl;
  }
}

int main(){
  int N;
  int ans[1000];
  FILE* fp_in = freopen("A-large.in", "r", stdin);
  cin >> N;
  REP(k,N){
    REP(i,MAX_field)
      REP(j,MAX_field)
      cin >> field[j][i];
    ans[k] = judge();
  }
  
  REP(i,N){ 
     cout << "Case #"<< i+1 << ": ";
     switch(ans[i]){
     case 0:
       cout << "Game has not completed" << endl;
       break;
     case 1:
       cout << "O won" << endl;
       break;
     case 2:
       cout << "X won" << endl;
       break;
     case 3:
       cout << "Draw" << endl;
       break;
  }
  }
  
return 0;
}
