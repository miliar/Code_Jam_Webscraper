#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;

int xs[1001];
int ys[1001];
vector< pair< int,int> > rs;
int N ;
int W;
int L;
int rec( int x , int y , int w , int l , int i ){
  if( i >= N ) return N;
  int ind = rs[i].second;
  int r =rs[i].first;
  //cout << x << "," << y << "," << W << "," << L << ", " << i << endl;
  if( x > w ) return i;
  if( y > l ) return i;
  xs[ind] = x;
  ys[ind] = y;
  int ret = i+1;
  int nextr = rs[ret].first;
  ret = rec( x+r+nextr , y, W , y+2*r-nextr, ret);
  nextr = rs[ret].first;
  ret = rec( x, y+r+nextr, x+2*r-nextr , L , ret );
  nextr = rs[ret].first;
  ret = rec( x+r+nextr, y+r+nextr, W, L , ret );
  return ret;
}

int main(){
   int n_case;
   cin >> n_case;
   for( int loop = 0 ; loop < n_case ; loop++ ){
     cin >> N >> W >> L;
     for( int i = 0 ; i < N ; i++ ){
      int r;
      cin >> r;
      rs.push_back(make_pair(r,i));
     }
     sort(rs.begin(), rs.end() );
     reverse( rs.begin(), rs.end());
     rec(0,0,W,L,0);
     cout << "Case #" << loop+1 << ": " ;
     for( int i = 0 ; i < N ; i++ ){
       cout << xs[i] << " " << ys[i] << " ";
     }
     cout << endl;
     rs.clear();
   }
   return 0;
}
