#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <sstream>
#include <functional>
#include <utility>
#include <vector>
#include <list>

using namespace std;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  //setvbuf(stdout, NULL, _IOFBF, 10000);
  
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int a, b;
    scanf("%d %d", &a, &b);
    int npairs = 0;
    ostringstream oss;
    for (int i = a; i <= b; ++i){
      oss << i;
      string is = oss.str();
      oss.str("");
      oss.clear();
      for (int j = i+1; j <= b; ++j) {
        oss << j;
        string js = oss.str();
        oss.str("");
        oss.clear();
        if (is.length() == js.length()) {
          for (int k = 1; k <= is.length() - 1; ++k) {
            //cout << is << " : " << js.substr(k) + js.substr(0, k) << endl;
            string rearr = js.substr(k) + js.substr(0, k);
            if (is == rearr && rearr != js) {
              ++npairs;
              break;
            }
          }
        }
      }
    }
    printf("Case #%d: %d\n", ctr+1, npairs);
  }

  return 0;
}
