#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

int seatstaken( vector<int> & coaster ){
  int ret(0);
  for( unsigned int i(0); i < coaster.size(); ++i ){
    ret += coaster[i];
  }
  return ret;
}

bool enough( vector<int> & coaster, vector<int> & groups, int max ){//enough for next group
  if( groups.size() == 0 ) return false;
  if( max >= seatstaken( coaster ) + groups[0] ) return true;
  else return false;
}

void addgroup( vector<int> & coaster, vector<int> & groups ){
  coaster.push_back( groups[0] );
  groups.erase( groups.begin());
}

void requeue( vector<int> & coaster, vector<int> & groups ){
  for( unsigned int i(0); i < coaster.size(); ++i ){
    groups.push_back( coaster[i] );
  }
  coaster.clear();
}

int main(){
  ifstream fin("in.in");
  ofstream out("out.out");
  int T, R, N, K, tmpG, Euros(0);
  vector<int> C, G;
  fin >> T;
  for( int curT(0); curT < T; ++curT ){
    Euros = 0;
    fin >> R;
    fin >> K;
    fin >> N;
    G.clear();
    for( int i = 0; i < N; ++i ){ 
      fin >> tmpG;
      G.push_back(tmpG);
    }
    for( int curR(0); curR < R; ++curR ){
      while( enough( C, G, K ) ){ // adding groups to coaster
        addgroup( C, G );
      }
      Euros += seatstaken( C );
      requeue( C, G );
    }
    out << "Case #" << curT + 1 << ": " << Euros << endl;
  }
  fin.close();
  out.close();
  system("pause");
  return 0;
}