#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define Forf(i,f,n) for(int i=(f);i<(n);++i)
#define For(i,n) for(int i=0;i<(n);++i)
#define foreach(it,m) for(typeof((m).begin()) it = (m).begin();it!=(m).end();++it) 

int compute_rle(const string &s) {
  int iprev = 0;
  int num = 1;
  Forf(i,1,s.size()) {
    if (s[i]!=s[iprev]) {
      iprev = i;
      num++;
    }
  }
  return num;
}

void solveit() {
  int k;
  cin >> k;
  vector<int> v(k);
  For(i,k) v[i]=i;

  string s;
  cin >> s;
  
  string w = s;
  int bestrle = s.size()+1;
  while(1) {
    //    cerr << bestrle << endl;
    For(i,s.size()/k) {
      For(j,k) {
	w[i*k+j] = s[i*k+v[j]];
      }
    }
    int rle = compute_rle(w);
    if (rle<bestrle) bestrle = rle;
    if (!next_permutation(v.begin(), v.end())) break;
  }
  cout << bestrle << endl;
}


int main() {
  int N;
  cin >> N;
  For(c,N) {
    cout << "Case #" << (c+1) << ": ";
    solveit();
  }
}
