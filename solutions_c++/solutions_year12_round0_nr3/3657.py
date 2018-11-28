#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;


string convertInt(int n) {
  stringstream ss;
  ss << n;
  return ss.str();
}

int convertString(string n) {
  stringstream ss(n);
  int i = 0;
  ss >> i;
  return i;
}


int permutar(int n, int i) {
  string n_s = convertInt(n);
  int n_len = n_s.size();
  string n_first = n_s.substr(0, i);
  string n_tail = n_s.substr(i, n_len-i);
  string p = n_tail + n_first;
  return convertString(p);
}


bool en_cache(int p, vector<int> cache) {
  return (find(cache.begin(), cache.end(), p) != cache.end());
}

int contar_par(int n, int b) {
  int r = 0;
  string n_s = convertInt(n);
  int n_len = n_s.size();
  int p = 0, i = 0;
  vector<int> cache;

  for (i = 1; i < n_len; i++) {
    p = permutar(n, i);
    if (p > n && p <= b && !en_cache(p, cache)) {
      cache.push_back(p);
      r++;
    }
  }

  return r;
}


int main() {
  int tc = 0, i=0;
  cin >> tc;
  for (i = 0; i < tc; i++) {
    int A=0, B=0, j=0, sum=0;

    cin >> A;
    cin >> B;
    
    for (j = A; j < B; j++) {
      sum += contar_par(j, B);
    }
    cout << "Case #" << i+1 << ": " << sum << endl;
  }
  
  return 0;
}
