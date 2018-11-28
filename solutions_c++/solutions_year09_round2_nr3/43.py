#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <set>

using namespace std;


typedef map<int,string> M;
typedef vector<M> VM;
typedef vector<VM> VVM;

int T, W, Q;

bool Before(const string &s, const string &t) {
  if (s.length() < t.length()) return true;
  if (t.length() < s.length()) return false;
  return s < t;
}

bool valid(int r, int c) {
  return r >= 0 && r < W && c >= 0 && c < W;
}
    
int main() {
  cin >> T;
  vector<string> S;
  vector<int> Qs;
  vector<string> answers;

  for (int caseno = 0; caseno < T; caseno++) {
    cin >> W >> Q;
    S.resize(W);
    for (int i = 0; i < W; i++)
      cin >> S[i];
    answers.clear();
    answers.resize(Q);
    Qs.clear();
    for (int i = 0; i < Q; i++) {
      int x;
      cin >> x;
      Qs.push_back(x);
    }
    
    set<int> done;
    VVM cache(W, VM(W));
    for (int i = 0; i < W; i++) {
      for (int j = 0; j < W; j++) {
	if (S[i][j] >= '0' && S[i][j] <= '9') {
	  cache[i][j][S[i][j] - '0'] = string("") + S[i][j];
	  done.insert(S[i][j] - '0');
	}
      }
    }

    while (true) {
      bool found = true;
      for (int i = 0; found && i < Q; i++) {
	if (done.find(Qs[i]) == done.end()) found = false;
      }
      if (found) break;


      /*
      for (int i = 0; i < W; i++) {
	for (int j = 0; j < W; j++) {
	  for (M::iterator iter = cache[i][j].begin(); 
	       iter != cache[i][j].end(); ++iter) {
	    cout << "(" << i << "," << j << "): " << iter->first << " = " << iter->second << endl;	    
	  }
	}
      }
      */


      int dr[] = {1, 0, -1, 0};
      int dc[] = {0, 1, 0, -1};

      VVM newcache = cache;

      for (int i = 0; i < W; i++) {
	for (int j = 0; j < W; j++) {
	  if (cache[i][j].size() == 0) continue;

	  for (int d1 = 0; d1 < 4; d1++) {
	    if (!valid(i+dr[d1], j+dc[d1])) continue;
	    char c1 = S[i+dr[d1]][j+dc[d1]];

	    for (int d2 = 0; d2 < 4; d2++) {
	      if (!valid(i+dr[d1]+dr[d2], j+dc[d1]+dc[d2])) continue;
	      char c2 = S[i+dr[d1]+dr[d2]][j+dc[d1]+dc[d2]];
	      
	      //if (i == 4 && j == 4) cerr << "HI" << c1 << " " << c2 << endl;
	      

	      for (M::iterator iter = cache[i][j].begin(); 
		   iter != cache[i][j].end(); ++iter) {
		
		string t = iter->second;
		t += c1;
		t += c2;
		int newsum = iter->first;
		if (c1 == '+') {
		  newsum += (c2 - '0');
		} else if (c1 == '-') {
		  newsum -= (c2 - '0');
		} else {
		  cerr << "WTF?" << endl;
		}

		int ni = i+dr[d1]+dr[d2];
		int nj = j+dc[d1]+dc[d2];
		
		if (newcache[ni][nj].find(newsum) == newcache[ni][nj].end()) {
		  newcache[ni][nj][newsum] = t;
		  done.insert(newsum);
		} else if (Before(t, newcache[ni][nj][newsum])) {
		  newcache[ni][nj][newsum] = t;
		}
	      }
	    }
	  }
	}
      }
      
      //exit(0);
      cache = newcache;
    }    
    
    cout << "Case #" << caseno+1 << ":" << endl;
    for (int q = 0; q < Q; q++) {
      string t = "";
      for (int i = 0; i < W; i++) {
	for (int j = 0; j < W; j++) {
	  if (cache[i][j].find(Qs[q]) == cache[i][j].end()) continue;
	  if (t == "" || Before(cache[i][j][Qs[q]], t)) {
	    t = cache[i][j][Qs[q]];
	  }
	}
      }

      cout << t << endl;
    }
  }
  
}
