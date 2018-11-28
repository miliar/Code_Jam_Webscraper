#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int find(string s, vector<string> strs) {
  for (int i = 0; i < strs.size(); i++) {
    if (s == strs[i])
      return i;
  }
  assert(false);
}

int main() {
  int N, E, Q;
  vector<string> engines, queries;
  cin >> N;
  for (int test = 0; test < N; test++) {
    cin >> E;
    engines.resize(E);
    scanf("\n");
    for (int i = 0; i < E; i++) {
      getline(cin, engines[i]);
    }

    cin >> Q;
    queries.resize(Q);
    scanf("\n");
    for (int i = 0; i < Q; i++) {
      getline(cin, queries[i]);
    }


    vector<bool> seen(E, 0);
    int numseen = 0;
    int switches = 0;
    for (int i = 0; i < Q; i++) {
      int id = find(queries[i], engines);
      if (!seen[id]) {
	if (numseen < E-1) {
	  seen[id] = true;
	  numseen++;
	}
	else {
	  switches++;
	  seen = vector<bool>(E, 0);

	  seen[id] = true;
	  numseen = 1;
	}
      }
      else {
      }
    }
    
    cout << "Case #" << test+1 << ": " << switches << endl;
  }
  return 0;
}
