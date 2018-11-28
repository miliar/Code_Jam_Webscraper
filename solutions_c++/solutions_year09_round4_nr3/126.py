#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;


bool before(const vector<int> &first, const vector<int> &second) {
  for (int pos = 0; pos < first.size(); ++pos) {
    if (first[pos] >= second[pos]) {
      return false;
    }
  }
  return true;
}

int main() {
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);

  int test_cases;
  cin >> test_cases;
  for (int test = 1; test <= test_cases; ++test) {

    int number_of_charts, chart_length;
    cin >> number_of_charts >> chart_length;
    vector<vector<int> > charts(number_of_charts, vector<int>(chart_length));
    for (int i = 0; i < number_of_charts; ++i) {
      for (int pos = 0; pos < chart_length; ++pos) {
        cin >> charts[i][pos];
      }
    }

    int net_size = number_of_charts * 2 + 2;
    int source = number_of_charts * 2;
    int sink = number_of_charts * 2 + 1;

    vector<vector<int> > cap(net_size, vector<int>(net_size));
    vector<vector<int> > flow(net_size, vector<int>(net_size));
    
    for (int i = 0; i < number_of_charts; ++i) {
      for (int j = 0; j < number_of_charts; ++j) {
        if (before(charts[i], charts[j])) {
          cap[i][number_of_charts + j] = 1;
          //cout << i << " -> " << j << endl;
        }
      }
    }
    for (int i = 0; i < number_of_charts; ++i) {
      cap[source][i] = 1;
      cap[number_of_charts + i][sink] = 1;
    }

    vector<int> pred(net_size, -1);
    int flow_size = 0;
    while (true) {
      vector<bool> marked(net_size, false);
     
      queue<int> que;
      que.push(source);
      marked[source] = true;
      while (!que.empty()) {
        int i = que.front();
        que.pop();
        for (int j = 0; j < net_size; ++j) {
          if (cap[i][j] - flow[i][j] > 0) {
            if (!marked[j]) {
              marked[j] = true;
              pred[j] = i;
              que.push(j);
            }
          }
        }
      }

      if (!marked[sink]) {
        break;
      }

      int i = sink;
      while (i != source) {
        ++flow[pred[i]][i];
        flow[i][pred[i]] = -flow[pred[i]][i];
        i = pred[i];
      }
      ++flow_size;
    }
    
    int answer = number_of_charts - flow_size;

    cout << "Case #" << test << ": " << answer << endl;
  }

  return 0;
}