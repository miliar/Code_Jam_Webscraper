#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

#define SMALL_FILE "A-small.in"
#define LARGE_FILE "A-large.in"

int main()
{
  //ifstream in(LARGE_FILE);
  ifstream in(SMALL_FILE);
  ofstream out("out.txt");
  int T, n;
  int u[800], v[800];

  in>>T;
  for ( int t = 1; t <= T; t++ ) {
    //read data
    in>>n;
    for ( int i = 0; i < n; i++ )
      in>>u[i];
    for ( int i = 0; i < n; i++ )
      in>>v[i];

    // algorithm
    sort(v, v+n);
    sort(u, u+n);
    int s = 0;
    for ( int i = 0; i < n; i++ )
      s += v[i] * u[n-1-i];
    out<<"Case #"<<t<<": "<<s<<endl;
  }

  return 0;
}
