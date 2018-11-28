#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

#define SMALL_FILE "A-small.in"
#define LARGE_FILE "A-large.in"

int* cache[1000];
int* storage_cache;

int solve(int* query, int initial, int Q, int S)
{
  //cout<<initial<<' '<<Q<<' '<<S<<endl;
  int pos, min = 2000;
  bool flag = true;
  
  for ( pos = 0; pos < Q; pos++ ) {
    if ( query[pos] == initial ) {
      flag = false;
      break;
    }
  }

  if (flag) return 0;

  for ( int i = 0; i < S; i++ ) {
    if ( i != initial ) {
      int num;
      int Q_new = Q - pos;
      if ( cache[Q_new][i] < 0 ) {
	num = solve(query + pos, i, Q_new, S);
	cache[Q_new][i] = num;
      }
      else
	num = cache[Q_new][i];
      if ( num < min ) min = num;
    }
  }

  return min + 1;
}

int main() {
  int N, S, Q;
  ifstream in(LARGE_FILE);
  //ifstream in(SMALL_FILE);
  ofstream out("out.txt");
  char *search[100];
  char query[101];
  int qidx[1000];
  search[0] = new char[100 * 101];
  storage_cache = new int[100 * 1000];
  for ( int i = 0; i < 1000; i++ )
    cache[i] = storage_cache + i * 100;

  for ( int i = 0; i < 100; i++ )
    search[i] = search[0] + i * 101;

  in>>N;

  for ( int c = 0; c < N; c++ ) {
    cout<<c<<endl;
    char tmp[10];
    // read input
    in>>S;
    in.getline(tmp, 10);
    for ( int i = 0; i < S; i++ ){
      in.getline(search[i], 101);
    }
    in>>Q;
    in.getline(tmp, 10);
    for ( int i = 0; i < Q; i++ ) {
      in.getline(query, 101);
      for ( int j = 0; j < S; j++ )
	if ( strcmp(search[j], query) == 0 ) {
	  qidx[i] = j;
	  break;
	}
    }

    // the algorithm begin, using dynamic programming
    for ( int i = 0; i < 1000 * 100; i++ )
      storage_cache[i] = -1;
    int min = 2000;
    for ( int i = 0; i < S; i++ ) {
      int num;
      if ( i != qidx[0] ) {
	num = solve(qidx, i, Q, S);
	if ( num < min ) min = num;
      }
    }
    out<<"Case #"<<c+1<<": "<<min<<endl;
    cout<<min<<endl;
  }//c

  delete [] search[0];
  delete [] storage_cache;

  return 0;
}
