#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long LL;

typedef vector<int> VI;
typedef vector<VI> VVI;

const int MAGIC = 10009;

string poly;
VVI letter_counts;
vector<string> dict;
int K;
int n;

LL eval(const string &poly, const VI &counts) {
  
  /*
  cerr << "Evaluating";
  for (int i = 0; i < counts.size(); i++) cerr << " " << counts[i];
  cout << endl;
  */

  LL term = 1;
  LL sum = 0;
  for (int i = 0; i <= poly.size(); i++) {
    if (i == poly.size() || poly[i] == '+') {
      sum += term;
      term = 1;
    } else {
      term *= counts[poly[i] - 'a'];
    }
  }

  return sum;
}

LL choose(int left, VI &counts) {
  if (left == 0) return eval(poly, counts) % MAGIC;
  
  LL val = 0;
  for (int pos = 0; pos < n; pos++) {
    for (int i = 0; i < counts.size(); i++) counts[i] += letter_counts[pos][i];
    val = (val + choose(left - 1, counts)) % MAGIC;
    for (int i = 0; i < counts.size(); i++) counts[i] -= letter_counts[pos][i];
  }

  return val;
}

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; t++) {
    cin >> poly;
    cin >> K;
    cin >> n;
    dict.resize(n);
    for (int i = 0; i < n; i++) 
      cin >> dict[i];

    letter_counts.clear();
    letter_counts.resize(n, VI(26));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < dict[i].length(); j++) {
	letter_counts[i][dict[i][j] - 'a']++;
      }
    }

    cout << "Case #" << (t+1) << ":";
    for (int k = 1; k <= K; k++) {
      VI vals(26);
      cout << " " << choose(k, vals);
    }
    cout << endl;
  }
}
