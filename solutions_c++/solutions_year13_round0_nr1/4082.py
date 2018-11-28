#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define _f(i,x,n) for(int i=x;i<n;i++)
#define _if(i,x,n) for(int i=(n);i>=x;i++)
#define _fv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _d(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dv(v) cout<<"L"<<__LINE__<<": "<<#v<<": "; di((v).begin(),(v).end());
#define _dvf(v) cout<<"L"<<__LINE__<<": "<<#v<<": "; di((v).begin(),(v).end()); *************************
template<typename it> void di(it i,it f) { cout<<"[ "; while(i!=f) cout<<*(i++)<<" "; cout<<"]"<<endl; }
template<typename it> void dif(it i,it f,string ) { cout<<"[ "; while(i!=f) cout<<*(i++)<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

template<class Origen,class Destino> Destino convertir(Origen entrada)
	{ stringstream flujo; flujo<<entrada; Destino salida; flujo>>salida; return salida; }

string board[4];

char determineStatus(){
  //check diagonals
  char last = board[0][0];
  bool flag = true;
  _f(i,1,4){
    if(board[i][i] == '.' || (board[i][i] != last && board[i][i] != 'T' && last != 'T')){
      flag = false;
      break;
    }
    else if(board[i][i] != 'T') last = board[i][i];
  }
  if(flag) return last;

  last = board[0][3];
  flag = true;
  _f(i,1,4){
    if(board[i][3-i] == '.' || (board[i][3-i] != last && board[i][3-i] != 'T' && last != 'T')){
      flag = false;
      break;
    }
    else if(board[i][3-i] != 'T') last = board[i][3-i];
  }
  if(flag) return last;

  _f(i,0,4){
    //check rows
    last = board[i][0];
    flag = true;
    _f(j,1,4){
      if(board[i][j] == '.' || (board[i][j] != last && board[i][j] != 'T' && last != 'T')){
        flag=false;
        break;
      }
      else if(board[i][j] != 'T') last = board[i][j];
    }
    if(flag) return last;
    //check columns
    last = board[0][i];
    flag = true;
    _f(j,1,4){
      if(board[j][i] == '.' || (board[j][i] != last && board[j][i] != 'T' && last != 'T')){
        flag=false;
        break;
      }
      else if(board[j][i] != 'T') last = board[j][i];
    }
    if(flag) return last;
  }
  
  //check if it is draw
  flag = true;
  _f(i,0,4)
    _f(j,0,4)
      if(board[i][j] == '.')
        flag = false;

  if(flag) return 'D';

  return 'I';
}

int main(){
    int T;
    cin>>T;
    _f(tt,1,T+1){
        _f(i,0,4)
          cin>>board[i];
        char status = determineStatus();
        string res;
        switch(status){
          case 'X':
            res = "X won";
            break;
          case 'O':
            res = "O won";
            break;
          case 'D':
            res = "Draw";
            break;
          default:
            res = "Game has not completed";
        }
        cout<<"Case #"<<tt<<": "<<res<<endl;
    }
    return 0;
}
