#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

int main() {
  ifstream cin("B-large (1).in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ":";
    cout << " ";
    long long L, t, N, C;
    long long res = 0;
    cin >> L >> t >> N >> C;
    vector<int> p(N);
    for(int i = 0; i < C; i++) {
      cin >> p[i];
    }
    for(int i = C; i < N; i++) {
      p[i] = p[i%C];
    }
    vector<double> times(N);
    long long curTime = 0;
    int curInd = -1;
    for(int i = 0; i < N; i++) {
      times[i] = p[i]*2;
      if(curInd == -1 && t < curTime+times[i])
        curInd = i;
      else if(curInd == -1)
        curTime += times[i];
    }
    long long num = L;
    if(curInd == -1 || num == 0) {
      long long tm = 0;
      for(int i = 0; i < N; i++)
        tm += (int)(times[i]+0.5);
      cout << tm;
    } else {
      num--;
      times[curInd] = p[curInd] + (t-curTime)/2;
      vector<pair<int, int> > pp(N);
      for(int i = curInd+1; i < N; i++) {
        pp[i].first = p[i];
        pp[i].second = i;
      }
      sort(pp.rbegin(), pp.rend());
      for(int i = 0; i < min(num, N-curInd); i++)
        times[pp[i].second] -= pp[i].first;
      long long tm1 = 0;
      for(int i = 0; i < N; i++)
        tm1 += (int)(times[i]+0.5);
      for(int i = 0; i < min(num, N-curInd); i++)
        times[pp[i].second] += pp[i].first;
      num++;
      times[curInd] = p[curInd]*2;
      for(int i = 0; i < min(num, N-curInd); i++)
        times[pp[i].second] -= pp[i].first;
      long long tm2 = 0;
      for(int i = 0; i < N; i++)
        tm2 += (int)(times[i]+0.5);
      cout << min(tm1, tm2);
    }
    cout << endl;
  }
}
