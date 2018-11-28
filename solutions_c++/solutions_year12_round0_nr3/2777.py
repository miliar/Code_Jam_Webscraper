#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> &p1, pair <int, int> &p2) {
  if(p1.first == p2.first)
    return p1.second < p2.second;
  return p1.first < p2.first;
}

int digits(int num) {
  int dig = 0;
  while(num > 0) {
    num /= 10;
    dig++;
  }
  return dig;
}

int advance(queue<int> &que, int num, int ten) {
  int fst = que.front();
  que.pop();  
  que.push(fst);

  num -= fst*ten;
  num *= 10;
  num += fst;

  return num;
}

int main() {
  
  int T;
  cin >> T;

  for(int t = 1; t <= T; t++) {
    int A, B;
    cin >> A >> B;
    
    set<pair<int, int> > prs;
    for(int j = A; j <= B; j++) {      
      vector<int> stk;
      queue<int> que;

      int ten = 1, num = j;
      while(num > 0) {
        ten *= 10;
        stk.push_back(num % 10);
        num /= 10;
      }      

      ten /= 10;

      reverse(stk.begin(), stk.end());
      for(int i = 0; i < stk.size(); i++)
        que.push(stk[i]);      
      
      num = j;

      do {
        num = advance(que, num, ten);
        if(que.front() != 0 && j < num && num <= B) {
          prs.insert(make_pair(j, num));
        }
      } while(num != j);  
    }

    cout << "Case #" << t << ": "<< prs.size() << endl;
  }
  
  return 0;
}
