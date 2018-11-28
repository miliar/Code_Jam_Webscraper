#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

void add( set<string> & dirs, string added ){
  if( added == "" ) return;
  if( added[ added.size() - 1 ] != '/' )
    added = added + '/';
  string tmp;
  for( size_t i(0); i < added.size(); ++i ){
    tmp = tmp + added[i];
    if( tmp[ tmp.size() -1 ] == '/' )
      dirs.insert( tmp );
  }
}

int main(){
  ifstream fin("in.in");
  ofstream fout("out.out");
  set<string> dirs;
  string input;
  int count;
  int T,N, M;
  fin >> T;
  for( int t(0); t < T; ++t ){
    fin >> N >> M;
    for( int d(0); d < N; ++d ){
      fin >> input;
      add( dirs, input );
    }
    if( dirs.find("/") != dirs.end() )
      dirs.erase( dirs.find("/"));
    count = dirs.size();

    for( int d(0); d < M; ++d ){
      fin >> input;
      add( dirs, input );
    }
    if( dirs.find("/") != dirs.end() )
      dirs.erase( dirs.find("/"));
    fout << "Case #" << t + 1 << ": " << dirs.size() - count << endl;
    dirs.clear();
  }
  system("pause");
  return 0;
}