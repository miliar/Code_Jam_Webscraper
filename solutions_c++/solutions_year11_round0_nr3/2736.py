#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

struct val{
  int v;
  int ind;
  val(int v, int d):v(v),ind(d){}
  bool operator<(const val &t)const{
    return v < t.v;
  }
};

int main()
{
  int T;
  cin >> T;
  for(int tc=1;tc<=T;++tc){
    int N;
    cin >> N;
    int minimum = 1<<28;
    int sum = 0;
    vector<int> org;
    vector<val> vv;
    for(int i = 0; i < N; ++i){
      int c;
      cin >> c;
      org.push_back(c);
      vv.push_back( val(c,i) );
      sum += c;
      minimum = min(minimum, c);
    }
    sort(vv.begin(),vv.end());
    reverse(vv.begin(),vv.end());

    vector< vector< val > > vbits;
    vbits.resize(30);
    for(int i = 0; i < (int)vv.size(); ++i){
      int ind=0;
      int bit = 1;
      while(bit<vv[i].v){
	if( vv[i].v & bit ) vbits[ind].push_back( vv[i] );
	bit*=2;
	++ind;
      }
    }
    
    for(int i = 0; i < vbits.size(); ++i){
      sort( vbits[i].begin(), vbits[i].end() );
      reverse( vbits[i].begin(), vbits[i].end() );
    }
    
    bool ng = false;
    for(int i = 0; i < (int)vbits.size(); ++i){
      if( vbits[i].size() >= 2 && vbits[i].size() % 2 == 0 ){
      }else if( vbits[i].size() > 0 ) ng=true;
    }
    
    cout << "Case #" << tc << ": ";
    if( ng ){
      cout <<"NO\n";
    }else{
      cout << sum-minimum << endl;
    }
    
  }
  return 0;
}
