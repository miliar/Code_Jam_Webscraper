#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int
mscore( vector<int> &s, int p )
{
  int t = 0;
  for(int i = s.size() -1 ; i > s.size()-1-p; i--){
    if( i < 0 ) break;
    t += s[i];
  }
  return t;
}

int
score(vector<int>& b, vector<int>& o, vector<char>& r)
{
  vector<int> s(0, r.size());
  int oi = 0, bi = 0;
  int so = 0, sb = 0;
  int t;
  s.push_back( 0 );

  for(int i = 0; i < r.size(); i++){

    if( r[i] == 'O' ){
      sb++;
      t = o[oi++] - mscore(s, so);
      so = 0;  
    }else{
      so++;
      t = b[bi++] - mscore(s, sb);
      sb = 0;
    }

    if( t < 0 ) t = 0;
    s.push_back( t + 1);
  }

  t = 0;
  for(int i = 0; i < s.size(); i++) t += s[i];
  //  copy(s.begin(), s.end(), ostream_iterator<int>(cout," "));
  //  cout<<endl;

  return t;
}

int
main()
{
  int t;
  cin>>t;

  for(int i = 0; i < t; i++){
    vector<int> B;
    vector<int> O;
    vector<char> R;
    int n; cin>>n;
    int pb = 1, po = 1;

    for(int j = 0; j < n; j++){
      char r;
      int p;
      cin>>r>>p;
      R.push_back( r );
      if( r == 'B' ) {
	B.push_back( abs(p - pb) );
	pb = p;
      }
      else{
	O.push_back( abs(p - po) );
	po = p;
      }
    }

    cout<<"Case #"<<i+1<<": "<<score(B, O, R)<<endl;
  }

}
