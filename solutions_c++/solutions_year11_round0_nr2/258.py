#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;
set <char> contra[27];
char comb[27][27];

string solve(string elem){
  char prev = 'A'+26;
  string ans;
  set <char> ops;
  for(int i=0;i<elem.length();i++){
    //    cout << ans << endl;
    char cur = elem[i];
    if(comb[cur-'A'][prev-'A']!=-1){
      ans.erase(ans.length()-1);
      ans += (comb[cur-'A'][prev-'A']);
      prev = comb[cur-'A'][prev-'A'];
      continue;
    }
   
    if(ops.count(cur) || contra[prev-'A'].count(cur)){
      ans.clear();
      ops.clear();
      prev='A'+26;
    }
    else{
      //      printf("%d opssize = %d prev = %c\n",contra[prev-'A'].size(),ops.size(), prev);
      set <char>::iterator it;
      for(it = contra[prev-'A'].begin();it!=contra[prev-'A'].end();it++){
	ops.insert(*it);
      }
      prev = cur;
      ans += cur;
    }
  }
  return ans;
}

int main(){
  fstream ifs;
  FILE* ofp;
  int probnum;

  ofp = fopen("B.out", "w");
  ifs.open("B-large.in", fstream::in);
  ifs >> probnum;
  for(int i=0;i<probnum;i++){
    for(int k=0;k<27;k++)for(int j=0;j<27;j++) comb[k][j]=-1;
    for(int k=0;k<27;k++) contra[k].clear();
    string str;
    int n;
    ifs >> n;
    for(int j=0; j<n; j++){
      ifs >> str;
      comb[str[0]-'A'][str[1]-'A'] = str[2];
      comb[str[1]-'A'][str[0]-'A'] = str[2];
    }
    ifs >> n;
    for(int j=0; j<n; j++){
      ifs >> str;
      contra[str[0]-'A'].insert(str[1]);
      contra[str[1]-'A'].insert(str[0]);
    }
    ifs >> n;
    ifs >> str;
    string ans = solve(str);
    string res = "[";
    for(int j=0;j<ans.length();j++){
      res += ans[j];
      if(j!=ans.length()-1)
	res += ", ";
    }
    res += "]";
    fprintf(ofp, "Case #%d: %s\n", i+1, res.c_str());
  }
}
    
