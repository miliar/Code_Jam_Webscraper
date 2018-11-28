#include <fstream>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;
typedef vector<int> VI;
typedef vector< VI > VVI;
int solve(const VI& Qs, int S) {
  int N = Qs.size();
  VVI mem(2, VI(S,0));
  mem[0][Qs[0]] = -1;

  for (int i = 1; i < N; ++i) {
    VI& last = mem[(i+1)%2];
    VI& cur = mem[(i)%2];
    cur.assign(S, 1000);
    int q = Qs[i];

    for (int j = 0; j < S; ++j) {
      if (q == j) {
        cur[j] = -1;
        continue;
      }
      for (int k = 0; k < S; ++k) {// last
        if (last[k] == -1)
          continue;
        if (j==k) {
          if (last[k] < cur[j])
            cur[j] = last[k];
        } else {
          if (last[k]+1 < cur[j]) {
            cur[j] = last[k] + 1;
          }
        }
      }
    }
  }
  VI& final = mem[(N-1)%2];
  int ret = 1000;
  for (int i = 0; i < final.size(); ++i)
    if (ret > final[i] && final[i] >= 0)
      ret = final[i];

  return ret;
}
void main() {
    ifstream in("A-large.in");
    ofstream out;
    out.open("out_result", ios::trunc);

    int N = 0;
    char buf[1024];
    in.getline(buf, 1024);
    sscanf(buf,"%d", &N);
    map<string, int> S2Id;
    VI Qs;
    for (int i = 0; i < N; ++i) {
      S2Id.clear();
      Qs.clear();;

      int S = 0;
      in.getline(buf, 1024);
      sscanf(buf,"%d", &S);
      for (int j = 0; j < S; ++j) {
        in.getline(buf, 1024);
        string name(buf);
        S2Id[name] = j;
      }

      int Q = 0;
      in.getline(buf, 1024);
      sscanf(buf,"%d", &Q);
      for (int j = 0; j < Q; ++j) {
        in.getline(buf, 1024);
        string name(buf);
        Qs.push_back(S2Id[name]);
      }
      int ret = 0;
      if (Qs.size() == 0)
        ret = 0;
      else ret = solve(Qs, S);
      
      // write ret;
      out<<"Case #"<< i+1 <<": "<<ret<<endl;
    }
    out.close();
}