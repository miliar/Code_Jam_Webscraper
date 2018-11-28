#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;


// perm is permutation on [0,..,k-1] 
string rletransform(int k, int *perm, string total){
  char *tmp = new char[k];
  for(int i=0; i<total.size(); i+=k){
    for(int j=0; j<k; ++j){
      tmp[j] = total[i+perm[j]];
    }
    for(int j=0; j<k; ++j){
      total[i+j] = tmp[j];
    }
  }
  return total;
}

int rlescore(const string &str){
  int ttl = 0;
  for(int i=1; i<str.size(); ++i){
    if(str[i] != str[i-1]) ++ttl;
  }
  return ttl;
}

int bestscore(const string &str, bool *used, int *perm, int k, int sofar){
  if(sofar == k){
    return rlescore(rletransform(k,perm,str));
  }
  int best = 0x7FFFF;
  for (int i = 0; i<k; ++i){
    if(!used[i]){
      used[i] = true;
      perm[sofar] = i;
      int nscore = bestscore(str, used, perm, k, sofar+1);
      if( best > nscore ) best = nscore;
      used[i] = false;
    }
  }
  return best;
}

void solve(int caseno){
  int k;
  string str;
  cin >> k >> str;

  bool *used = new bool[k];
  for(int i=0; i<k; ++i)
    used[i] = false;
  
  int *perm = new int[k];

  int ans = bestscore(str, used, perm, k, 0) + 1; // +1 to count first letter
  printf("Case #%d: %d\n", caseno,ans);
}

int main(){

  int n;
  cin >> n;
  for (int i=0; i<n; ++i){
    solve(i+1);
  }

  return 0;
}
