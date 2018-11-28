#include <iostream>
#include <vector>
#include <iterator>
using namespace std;

const int IMPOSSIBLE = 0;

int
sadd( int a, int b )
{
  int t = 0;
  for(int i = 0; i <= 20; i++){
    int aa = a & ( 1<<i );
    int bb = b & ( 1<<i );
    if( aa == bb ) continue;
    t = (t | (1<<i ));
  }

  //  cout<<a<<" "<<b<<" "<<t<<endl;
  return t;
}

int
c_calc(vector<int>& v, int pos, int s, int p, int st, int pt)
{
  if( pos >= v.size() ){
    //    cout<<s<<" "<<p<<" "<<st<<" "<<pt<<endl;
    if( s == 0 || p == 0) return 0;
    if( s == p ) return (st > pt) ? st : pt ;
    return 0;
  }

  int l_ct = c_calc(v, pos+1, sadd(s, v[pos]), p, st+v[pos], pt);
  int r_ct = c_calc(v, pos+1, s, sadd(p, v[pos]), st, pt+v[pos]);

  return ( l_ct > r_ct ) ? l_ct : r_ct;
}

int
main()
{
  int t; cin>>t;
  for(int i = 0; i < t; i++){
    int n; cin>>n;
    vector<int> v;
    for(int j = 0; j < n; j++){
      int c; cin>>c;
      v.push_back(c);
    }

    cout<<"Case #"<<i+1<<": ";
    int cost = c_calc( v , 0, 0, 0, 0, 0);
    if( cost == IMPOSSIBLE ) cout<<"NO"<<endl;
    else cout<<cost<<endl;

  }
  
}
