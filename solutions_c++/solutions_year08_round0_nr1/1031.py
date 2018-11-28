#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <climits>
using namespace std;

int Y[1001][100];

int main() {
  int N;
  cin >> N;
  for (int casenum=1; casenum <= N; casenum++) {

    int S;
    cin >> S >> ws;
    //cout << S << endl;
    map<string, int> namemap;
    for (int i=0; i<S; i++) {
      string name;
      getline(cin, name);
      namemap[name] = i;
      //cout << name << " " << namemap[name] << endl;
    }

    int Q;
    cin >> Q >> ws;
    //cout << Q << endl;
    vector<int> queries(Q);
    for (int i=0; i<Q; i++) {
      string name;
      getline(cin, name);
      queries[i] = namemap[name];
      //cout << name << " " << namemap[name] << endl;
    }

    for (int i=0; i<S; i++) {
      Y[Q][i] = 0;
    }

    for (int i=Q-1; i>=0; i--) {
      for (int j=0; j<S; j++) {	
	if (queries[i] != j) {
	  Y[i][j] = Y[i+1][j];
	} else {
	  Y[i][j] = INT_MAX;
	  for (int k=0; k<S; k++) {
	    if (k != j) {
	      Y[i][j] = min(Y[i][j], Y[i+1][k]+1);
	    }
	  }
	}
      }
    }

    int y = INT_MAX;
    for (int i=0; i<S; i++) {
      y = min(y, Y[0][i]);
    }

    cout << "Case #" << casenum << ": " << y << endl;
  }

  return 0;
}
