#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<fstream>
#include<complex>
#include<cassert>
#include<climits>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
const double PI = 3.14159265;

struct Trie {
  bool is_word;
  Trie *next[26];
  Trie() : is_word(false){
    memset(next, 0, sizeof(next));
  }
  void insert(const char* p){
    Trie* t = this;
    for( ; *p; p++){
      int n = *p - 'a'; // mapping
      if(!t->next[n]) t->next[n] = new Trie();
      t = t->next[n];
    }
    t->is_word = true;
  }
  int count(const char* p){
    if(*p == 0) return 1;
    if(*p != '('){
      Trie* nx = next[*p-'a'];
      if(nx){
        return nx->count(p+1);
      }else{
        return 0;
      }
    }else{
      int ret = 0;
      vector<int> nxs;
      ++p;
      while(*p != ')'){
        nxs.push_back(*p-'a');
        ++p;
      }
      ++p;
      FOR(it,nxs){
        Trie *t = next[*it];
        if(t) ret += t->count(p);
      }
      return ret;
    }
  }
};
int main()
{
  int L,D,N;
  cin >> L >> D >> N;
  char buf[20];
  Trie dict;
  REP(i,D){
    cin >> buf;
    dict.insert(buf);
  }
  string s;
  REP(i,N){
    cin >> s;
    int K = dict.count(s.c_str());
    printf("Case #%d: %d\n", i+1, K);
  }
  return 0;
}

