#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int solve(vector <int>& v){
  sort(v.begin(),v.end());

  int check=0,ans=0;
  for(int i=0;i<v.size();i++){
    check ^= v[i];
    ans += v[i];
  }

  if(check == 0)
    return ans-v[0];
  else 
    return -1;
}

int main(){
  fstream ifs;
  FILE* ofp;
  int probnum;

  ofp = fopen("C.out", "w");
  ifs.open("C-large.in", fstream::in);
  ifs >> probnum;

  for(int i=0;i<probnum;i++){
    vector <int> v;
    int n,m;
    ifs >> n;
    for(int j=0;j<n;j++){
      ifs >> m;
      v.push_back(m);
    }
    int ans = solve(v);
    if(ans==-1)
      fprintf(ofp, "Case #%d: NO\n", i+1);
    else
      fprintf(ofp, "Case #%d: %d\n", i+1, ans);
  }
  return 0;
}

