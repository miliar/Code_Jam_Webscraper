#include<iostream>
#include<set>
#include<string>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int tc=1;tc<=T;++tc){
    int ans = 0;
    set<string> exist;
    set<string> want;
    int N,M;
    cin >> N >> M;
    exist.insert("/");
    for(int i = 0; i < N; ++i){
      string already;
      cin >> already;
      already += '/';
      exist.insert( already );
    }
    for(int i = 0; i < M; ++i){
      string w;
      cin >> w;
      w+='/';
      string tmp;
      for(int j = 0; j < w.length(); ++j){
	if( w[j] == '/' ){
	  tmp += w[j];
	  if( exist.find( tmp ) == exist.end() ){
	    ++ans;
	    exist.insert( tmp );
	  }
	}else
	  tmp += w[j];
      }
    }
    printf("Case #%d: %d\n", tc, ans);
  }
  return 0;
}
