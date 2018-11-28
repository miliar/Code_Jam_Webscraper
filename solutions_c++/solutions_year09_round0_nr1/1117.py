#include <iostream>
#include <vector>
#include <string>
#include <cctype>

#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

const int N=1024;

main(){
  int a,b,c;
  while(cin >> a >> b >> c){
    vector<string> vs(b);
    REP(i,b) cin >> vs[i];

    static bool ok[N][26];
    REP(cc,c){
      memset(ok,false,sizeof ok);
      
      REP(i,a){
        char t; cin >> t;
        if(isalpha(t)) ok[i][t-'a']=true;
        else           while(cin >> t && isalpha(t)) ok[i][t-'a']=true;
      }

      int cnt=0;
      REP(i,vs.size()){
        REP(j,a) if(!ok[j][vs[i][j]-'a']) goto end;
        cnt++; end:;
      }
      
      static int Case;
      printf("Case #%d: %d\n",++Case,cnt);
    }
  }
}
