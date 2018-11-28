#include <iostream>
#include <vector>
#include <string>

//#include "cout.h"

using namespace std;

int L, D, N;

int parse(vector<int>& ans, const string& s)
{
  ans.resize(L); for(int i=0;i<L;i++) ans[i]=0;

  int p=0;
  for(int i=0,len=s.size(); i<len;){
    int c=s[i++];
    if (c=='(') {
      while((c=s[i++])!=')'){
        ans[p] |= 1 << (c-'a');
      }
      p++;
    } else {
      ans[p++] = 1 << (c-'a');
    }
  }
  return p;
}

main()
{
  cin >> L >> D >> N;
  // L: [1-10] or [1-15]
  // D: [1-25] or [1-5000]
  // N: [1-10] or [1-500]

  // loading lexicon
  vector<vector<int> > lexicon(D,vector<int>(L,0));
  for(int d=0;d<D;d++){
    string s; cin >> s;

    int p = parse(lexicon[d], s);
    // printf("// word#%d = \"", 1+d); cout << s << "\" => " << p << " " << lexicon[d] << endl;
  }

  // loading cases
  for(int n=0;n<N;n++){
    string s; cin >> s;

    vector<int> case_(L,0);
    int p = parse(case_, s);
    // printf("// case#%d = \"", 1+n); cout << s << "\" => " << p << " " << case_ << endl;

    int K = 0;
    for(int d=0;d<D;d++){
      int x=0;
      for(int i=0;i<L;i++) if (lexicon[d][i] & case_[i]) x++;
      if (x==L) K++;
    }
    printf("Case #%d: %d\n", 1+n, K);
  }

}
