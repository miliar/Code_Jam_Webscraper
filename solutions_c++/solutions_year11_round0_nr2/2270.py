#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cassert>

#define D(x) cout << #x " is " << x << endl
#define all(x) x.begin(), x.end()

using namespace std;

char BASES[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
map<char, string> opp;

bool is_base(char c){
  return (c == 'Q' or
          c == 'W' or
          c == 'E' or
          c == 'R' or
          c == 'A' or
          c == 'S' or
          c == 'D' or
          c == 'F');
}

bool opposed(string &ans, char c){
  //printf("Looking for opposed %s with %c\n", ans.c_str(), c);
  if(opp[c].size() == 0) return false;
  if(ans.size() == 0) return false;
  string &clrs = opp[c];
  for(int i=0;i<ans.size(); ++i){
    if(is_base(ans[i])){
      if(clrs.find(ans[i]) != string::npos){
        return true;
      }
    }
  }

  return false;
}

int main(){
  int T, K=1;
  scanf("%d", &T);
  while(T--){
    int C, D, N;
    string line, bases;
    map<string, char> comb;
    opp.clear();
    scanf("%d", &C);
    for(int i = 0;i<C;++i){
      cin >> line;
      bases = line.substr(0, 2);
      comb[bases] = line[line.size() - 1];
      reverse(all(bases));
      comb[bases] = line[line.size() - 1];
    }
    
    scanf("%d", &D);
    for(int i=0; i<D; ++i){
      cin >> line;
      opp[line[0]] += line[1];
      opp[line[1]] += line[0];
    }
    
    scanf("%d", &N);
    cin >> line;
    assert(line.size() == N);
    char c;
    string ans = "";
    string tmp = "__";
    ans+= line[0];
    for(int i = 1; i<N; ++i){
      tmp[0] = ans[ans.size() - 1];
      tmp[1] = line[i];
      bool cmp = false, op = false;;
      if( (c = comb[tmp]) != 0){
        ans[ans.size() - 1] = c;
        cmp = true;
      }
      if(!cmp && opposed(ans, line[i])){
        //printf("opossed %s  con %c\n", ans.c_str(), line[i]);
        ans = "";
        op = true;
      }
      if(!op && !cmp){
        ans+=line[i];
      }
    }
    printf("Case #%d: [", K++);
    if(ans.size() > 0){
      cout << ans[0];
      for(int i = 1; i<ans.size(); ++i){
        printf(", %c", ans[i]);
      }
    }
    printf("]\n");
    //cout << ans << endl;
  }
  return 0;
}
