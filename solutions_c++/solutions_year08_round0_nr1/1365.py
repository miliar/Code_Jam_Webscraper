#include<iostream>
#include<string>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>

#include<cstdio>
#include<cstdlib>

using namespace std;

#define FOR(i,s,n) for (int i=(int)(s); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

map<string, int> dic;
vector<int> input;

const int INF(1<<20);

int solve2()
{
  const int M = dic.size(), N = input.size();
  vector<vector<int> > table(2, vector<int>(M, 0));
  int prev(0), now(1);
  table[prev][input[0]] = INF;
  
  FOR(i, 1, N) {
    int minval = *min_element(ALL(table[prev]));
    REP(j, M) {
      if (j == input[i])
        table[now][j] = INF;
      else if (input[i-1] == j)
        table[now][j] = *min_element(ALL(table[prev])) + 1;
      else 
        table[now][j] = table[prev][j];
    }
    swap(prev, now);
  }
  return *min_element(ALL(table[prev]));
}

int main()
{
  string buf;
  getline(cin, buf);
  int n = atoi(buf.c_str());
  REP(i, n) {
    getline(cin, buf);
    dic.clear();
    int S = atoi(buf.c_str());
    REP(j, S) {
      getline(cin, buf);
      dic[buf] = j;
    }
    getline(cin, buf);
    input.clear();
    int Q = atoi(buf.c_str());
    REP(j, Q) {
      getline(cin, buf);
      int idx(-1);
      if (dic.find(buf) != dic.end()) idx = dic[buf];
      if (input.empty() || input.back() != idx) input.PB(idx);
    }
    
    int ans(1000);

    if (input.empty()) {
      ans = 0;
    } else {
      ans = solve2();
    }
    
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}

