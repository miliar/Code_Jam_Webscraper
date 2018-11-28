#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;

const int N = 100;

int one(int x){
  return x < 0 ? -1 : x > 0 ? 1 : 0;
}

int main(void){
  int t;

  cin >> t;
  for(int k = 0; k < t; ++k){
    int n;
    list<int> is[2];

    cin >> n;
    vector<pair<char, int> > seq(n);
    for(int i = 0; i < n; ++i){
      cin >> seq[i].first >> seq[i].second;
      if(seq[i].first == 'O')
        is[0].push_back(i);
      else
        is[1].push_back(i);
    }

    int pos[] = {1, 1};
    int cur = 0;
    int cnt = 0;
    while(cur < seq.size()){
      ++cnt;
      if(seq[cur].first == 'O' && pos[0] == seq[cur].second){
        is[0].pop_front();
        if(is[1].size() > 0)
          pos[1] += one(seq[is[1].front()].second - pos[1]);
        ++cur;
      }
      else if(seq[cur].first == 'B' && pos[1] == seq[cur].second){
        if(is[0].size() > 0)
          pos[0] += one(seq[is[0].front()].second - pos[0]);
        is[1].pop_front();
        ++cur;
      }
      else{
        if(is[0].size() > 0)
          pos[0] += one(seq[is[0].front()].second - pos[0]);
        if(is[1].size() > 0)
          pos[1] += one(seq[is[1].front()].second - pos[1]);
      }
    }
    cout << "Case #" << k + 1 << ": " << cnt << endl;
  }

  return 0;
}
