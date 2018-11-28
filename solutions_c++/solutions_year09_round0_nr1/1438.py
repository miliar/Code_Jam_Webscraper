#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> ws(d);
	for (int i = 0; i < d; ++i) {
		cin >> ws[i];
  }
  vector<int> v(d);
  for (int i = 0; i < n; ++i) {
  	string s;
  	cin >> s;
  	fill(v.begin(), v.end(), 0);
  	int pos = 0;
  	for (int j = 0; j < s.size(); ++pos) {
  	 bool par = (s[j] == '(');
  	 if (par) ++j;
  	 do {
  	  for (int k = 0; k < d; ++k) {
  	  	if (v[k] == pos && ws[k][pos] == s[j]) {
  	  	 v[k] = pos + 1;
  	  	}
  	  }
  	 	++j;
  	 } while (j < s.size() && (par && s[j] != ')'));
  	 if (par) ++j;
  	}
  	int sum = 0;
  	for (int k = 0; k < d; ++k)
  		if (v[k] == l)
	  		++sum;
	  cout << "Case #" << (i+1) << ": " << sum << endl;
  }
	return 0;
}
