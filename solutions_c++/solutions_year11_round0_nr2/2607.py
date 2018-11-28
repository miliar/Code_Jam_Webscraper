#include<iostream>
#include<string>
#include<vector>
using namespace std;

bool CheckCombine( char *s, int &len, int *cnt, const vector<string> &c ){
  for(int i = 0; i < (int)c.size(); ++i){
    if( (s[len - 1] == c[i][0] && s[len - 2] == c[i][1]) ||
	(s[len - 1] == c[i][1] && s[len - 2] == c[i][0]) ){

      cnt[ s[len-1] ]--;
      cnt[ s[len-2] ]--;
      cnt[ c[i][2] ]++;
      s[len-1] = 0;
      s[len-2] = c[i][2];
      --len;
      return true;
    }
  }
  return false;
}

bool CheckCancel( char *s, int &len, int *cnt, const vector<string> &o ){
  bool ret = false;
  for(int i = 0; i < (int)o.size(); ++i){
    if( cnt[ o[i][0] ] && cnt[ o[i][1] ] ){
      ret = true;
      break;
    }
  }
  if( ret ){
    s[0] = 0;
    len = 0;
    for(int i = 0; i < 256; ++i){
      cnt[i] = 0;
    }
  }
  return ret;
}

int main()
{
  int T;
  cin >> T;
  for(int tc=1;tc<=T;++tc){
    int C,D,dm;
    string N;
    vector<string> combin;
    vector<string> oppos;

    cin >> C;
    for(int i = 0; i < C; ++i){
      string tmp;
      cin >> tmp;
      combin.push_back( tmp );
    }
    cin >> D;
    for(int i = 0; i < D; ++i){
      string tmp;
      cin >> tmp;
      oppos.push_back( tmp );
    }
    cin >> dm >> N;

    char out[4096] = "";
    int cnt[256] = {0,};
    int len = 0;
    int pos = 0;
    while( pos < (int)N.length() ){
      out[len] = N[pos];
      cnt[ (int)out[len] ]++;
      ++len;
      ++pos;
      if( len >= 2 ){
	while( CheckCombine( out, len, cnt, combin ) );
	CheckCancel( out, len, cnt, oppos );
      }
    }
    cout << "Case #" << tc << ": [";
    for(int i = 0; i < len; ++i){
      if( i == len - 1 ){
	cout << out[i];
      }else{
	cout << out[i] << ", ";
      }
    }
    cout << "]\n";
  }
  return 0;
}
