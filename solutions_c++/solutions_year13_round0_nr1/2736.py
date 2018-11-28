#include<iostream>
#include<string>

#define DET(x) do{if( (x) != '.') return x;}while(0)

using namespace std;

int check(char M[4][4], int si, int sj, int di, int dj, int num){
  int i = si;
  int j = sj;
  int cnt = 1;
  char x = M[i][j];

  i += di;
  j += dj;
  if( x == '.' ) return 0;
  for(int t = 1; t < num; ++t){
    if( x != M[i][j] ){
      return cnt;
    }else ++cnt;
    i += di;
    j += dj;
  }
  return cnt;
}

char isok(char M[4][4], int i, int j, int num){
  if( num == 4 ) return M[i][j];
  return '.';
}

char solve(char M[4][4]){
  int num;
  char x;

  for(int i = 0; i < 4; ++i){
    num = check(M,i,0,0,1,4);
    x = isok(M,i,3,num); DET(x);

    num = check(M,0,i,1,0,4);
    x = isok(M,3,i,num); DET(x);
  }

  num = check(M,0,0,1,1,4);
  x = isok(M,3,3,num); DET(x);
    
  num = check(M,0,3,1,-1,4);
  x = isok(M,3,0,num); DET(x);
}


int main()
{
  int T;
  cin >> T;

  for(int tc=1;tc<=T;++tc){

    string status = "";
    char M[4][4];
    int wild_i = -1, wild_j = -1;
    bool not_draw = false;

    for(int i = 0; i < 4; ++i){
      for(int j = 0; j < 4; ++j){
        cin >> M[i][j];
        if( M[i][j] == '.' ) not_draw = true;
        if( M[i][j] == 'T' ){wild_i = i; wild_j = j;}
      }
    }

    for(int t = 0; t < 2; ++t){
      if( wild_i != -1 ){
        M[wild_i][wild_j] = t == 0 ? 'O' : 'X';
      }
      char ret = solve(M);

      if( ret =='X' ){ status = "X won"; break; }
      else if( ret == 'O' ){ status = "O won"; break; }
      else{
        if( !not_draw ) status = "Draw";
        else status = "Game has not completed"; 
      }
    }
    
    cout << "Case #" << tc << ": " << status << endl;
    
  }
  return 0;
}
