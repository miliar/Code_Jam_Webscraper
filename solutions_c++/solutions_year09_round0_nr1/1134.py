#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> words;
int l, n, d;

int match(string p, string w) {
  int it=0;
  for (size_t i=0;i<w.length();i++) {
    if (p[it]!='(') {
      if (p[it]!=w[i])
	return 0;
      else {
	it++;
	continue;
      }
    }
    bool found=false;
    while (p[++it]!=')') {
      if (p[it]==w[i])
	found=true;
    }
    it++;
    if (!found) 
      return 0;
  }
  return 1;
}

int main() {
  string str;
  cin >> l >> d >> n;
  for (int i=0;i<d;i++) {
    cin >> str;
    words.push_back(str);
  }
  for (int i=0;i<n;i++) {
    cin >> str;
    int cnt=0;
    for (int j=0;j<d;j++)
      cnt+=match(str, words[j]);
    cout << "Case #" << i+1 << ": " << cnt << endl;
  }
  return 0;
}
