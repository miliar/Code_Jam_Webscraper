#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

typedef vector<string> SI;
typedef set<string> SSET;
typedef map<string, SSET> MSMAP;
typedef map<string, int> SIMAP;
typedef map<int, SSET> ISMAP;

int N, M;
SI D;

// Current calc
string lis;
bool used[26];
SIMAP pens;

string calcMask(const string& s) {
  string m;
  REP(i, 0, s.size()) {
    if (used[s[i]-'a'])
      m += s[i];
    else
      m += '_';
  }
  return m;
}

void rec(int idx, SSET cands, int pen) {
  cout<<cand.size()<<endl;
  // cerr<<"REC :"<<idx<<", "<<pen<<endl;
  // for (SSET::iterator it=cands.begin(); it!=cands.end(); ++it) cerr<<*it<<" "; cerr<<endl;

  char c = lis[idx];

  bool appear=false;
  for (SSET::iterator it=cands.begin(); it!=cands.end(); ++it) {
    const string& cand = *it;
    if (find(cand.begin(), cand.end(), c)!=cand.end())
      appear=true;
  }
  if (!appear) {
    // used[c-'a'] = true;
    rec(idx+1, cands, pen);
    // used[c-'a'] = false;
    return;
  }

  MSMAP msmap;
  used[c-'a'] = true;
  for (SSET::iterator it=cands.begin(); it!=cands.end(); ++it) {
    const string& cand = *it;
    string mask = calcMask(cand);
    if (msmap.count(mask)==0)
      msmap[mask] = SSET();
    msmap[mask].insert(cand);
  }

  for (MSMAP::iterator it=msmap.begin(); it!=msmap.end(); ++it) {
    // cerr<<"Mask: "<<it->first<<endl;
    SSET& sset = it->second;
    const string& mask = it->first;
    bool addpen = (find(mask.begin(), mask.end(), c)==mask.end());
    int newpen = pen+(addpen?1:0);
    if (sset.size()==1) {
      string cand = *(sset.begin());
      pens[cand] = newpen;
      // cerr<<"Goal: "<<newpen<<", "<<cand<<endl;
    } else {
      //cout<<c<<", "<<mask<<", "<<pen+(addpen?1:0)<<endl;
      rec(idx+1, sset, newpen);
    }
  }
  used[c-'a'] = false;
}

void solve(int caseNum) {
  D.clear();
  pens.clear();
  cin>>N>>M;
  string buf;

  REP(i, 0, 26)
    used[i] = false;

  SSET cands;
  REP(i, 0, N) {
    cin>>buf;
    D.push_back(buf);
    cands.insert(buf);
  }

  printf("Case #%i: ", caseNum);
  REP(i, 0, M) {
    cin>>lis;
    pens.clear();

    ISMAP ismap;
    for (SSET::iterator it=cands.begin(); it!=cands.end(); ++it) {
      const string& cand = *it;
      int sz = cand.size();
      if (ismap.count(sz)==0)
        ismap[sz] = SSET();
      ismap[sz].insert(cand);
    }

    for (ISMAP::iterator it=ismap.begin(); it!=ismap.end(); ++it) {
      rec(0, it->second, 0);
    }

    // rec(0, cands, 0);
    int best = -1;
    string bests;

    // for (SIMAP::iterator it=pens.begin(); it!=pens.end(); ++it) {
      // const string& cand=it->first; int pen = it->second;

    REP(j, 0, D.size()) {
      const string& cand = D[j]; int pen = pens[cand];
      // cout<<cand<<": "<<pen<<endl;
      if (pen>best) {
        best = pen;
        bests = cand;
      }
    }
    if (i!=0) cout<<" ";
    cout<<bests;
  }

  printf("\n");
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

