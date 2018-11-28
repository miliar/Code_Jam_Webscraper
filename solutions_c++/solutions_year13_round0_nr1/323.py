#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

struct board{
  std::vector< std::vector< char > > b;
  int size;
  int k;
};

int count_dots( board b ){
  int dots = 0;
  int i,j;
  for ( i = 0; i < 4; ++i)
    for ( j = 0; j < 4; ++j)
      if ( b.b[i][j] == '.' )
        dots++;
  return dots;
}

int find_winner( board b, char p ){
  int won = 0;
  int wtry;
  int i,j;
  // horizontal:
  for ( i = 0; i < 4; ++i ){
    wtry = 0;
    for ( j = 0; j < 4; ++j ){
      if ( (b.b[i][j] == p) || (b.b[i][j] == 'T') )
        wtry++;
    }
    if ( wtry == 4 )
      won = 1;
  }
  // verticle:
  for ( j = 0; j < 4; ++j ){
    wtry = 0;
    for ( i = 0; i < 4; ++i ){
      if ( (b.b[i][j] == p) || (b.b[i][j] == 'T') )
        wtry++;
    }
    if ( wtry == 4 )
      won = 1;
  }
  // \:
  wtry = 0;
  for ( i = 0; i < 4; ++i ){
    if ( (b.b[i][i] == p) || (b.b[i][i] == 'T') )
      wtry++;
  }
  if ( wtry == 4 )
    won = 1;
  
  // /:
  wtry = 0;
  for ( i = 0; i < 4; ++i ){
    if ( (b.b[i][3-i] == p) || (b.b[i][3-i] == 'T') )
      wtry++;
  }
  if ( wtry == 4 )
    won = 1;

  return won;
}

int main(){

  using namespace std;
  fstream fin("g1.dat",ios::in);
  int i,j,k;
  int t, ti;
  fin >> t;

  vector< board > bs(t); 

  //cout << n_cases << endl;
  for ( ti= 0; ti< t; ++ti ){
    bs[ti].b.resize(4);
    for ( i = 0; i < 4; ++i)
      bs[ti].b[i].resize(4);
    
    for ( i = 0; i < 4; ++i)
      for ( j = 0; j < 4; ++j)
        fin >> bs[ti].b[i][j];
  }
  fin.close();

  
  for ( ti= 0; ti< t; ++ti ){
    for ( i = 0; i < 4; ++i){
      for ( j = 0; j < 4; ++j)
        cout << bs[ti].b[i][j] << " ";
      cout << endl;
    }
    cout << count_dots(bs[ti]) << endl;
  }


  
  fstream fout("o1.dat",ios::out);
  for ( ti = 0; ti < t; ++ti ){
    if ( find_winner( bs[ti], 'X' ) == 1 ){
      fout << "Case #" << (ti+1) << ": X won" << endl;
    } else if ( find_winner( bs[ti], 'O' ) == 1 ){
      fout << "Case #" << (ti+1) << ": O won" << endl;
    } else if ( count_dots( bs[ti] ) > 0 ){
      fout << "Case #" << (ti+1) << ": Game has not completed" << endl;
    } else {
      fout << "Case #" << (ti+1) << ": Draw" << endl;
    }
  }

  return 0;
}



