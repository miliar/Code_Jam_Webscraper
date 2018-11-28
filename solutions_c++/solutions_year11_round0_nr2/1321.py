
#include <iostream>
#include <map>
#include <vector>

using namespace std;

void print(vector<char> &w) {
  cout << "[";
  if (!w.empty()) cout << w[0];
  for (unsigned i = 1; i < w.size(); ++i)
    cout << ", " << w[i];
  cout << "]\n";
}

int main() {
  string s;
  int c, d, n, t;
  cin >> t;
  for (int z = 1; z <= t; ++z) {
    vector<int> v(26, 0);
    vector<map<int,char> > m(26);
    cin >> c;
    for (int i = 0; i < c; ++i) {
      cin >> s;
      int a = s[0] - 'A', b = s[1] - 'A';
      m[a][b] = s[2];
      m[b][a] = s[2];
    }
    cin >> d;
    for (int i = 0; i < d; ++i) {
      cin >> s;
      int x = s[0] - 'A', y = s[1] - 'A';
      v[x] |= 1 << y;
      v[y] |= 1 << x;
    }
    cin >> n >> s;
    vector<char> w;
    vector<int> u(26, 0);
    for (int i = 0; i < n; ++i) {
      int x = 0;
      for (int j = 0; j < 26; ++j)
	if (u[j] > 0) x |= 1 << j;
      int y = w.size()-1, a = s[i]-'A', b = y < 0 ? -1 : w[y]-'A';
      //cout << x << "," << y << "," << s[i] << "," << v[a] << ": ";
      //print(w);
      map<int,char>::iterator j = m[a].find(b);
      if (j != m[a].end()) {
	//cout << "Combine\n";
	w[y] = j->second;
	u[b]--;
	u[j->second - 'A']++;
      }
      else if ((x & v[a]) > 0) {
	//cout << "Clear\n";
	u = vector<int>(26, 0);
	w.clear();
      }
      else {
	//cout << "Append\n";
	w.push_back(s[i]);
	u[a]++;
      }
    }
    cout << "Case #" << z << ": ";
    print(w);
  }
}
