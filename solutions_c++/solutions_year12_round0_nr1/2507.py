#include <iostream>
#include <string>

using namespace std;

char from_googlerese[26];

const string g_in[] = {
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
  
const string g_out[] = {
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up"
};


void init_googlerese() {
  for (int i = 0; i < 26; ++i) {
    from_googlerese[i] = '0';
  }
  
  from_googlerese['a'-'a'] = 'y';
  from_googlerese['o'-'a'] = 'e';
  from_googlerese['z'-'a'] = 'q';
  from_googlerese['q'-'a'] = 'z';
  for (int i = 0; i < 3; ++i) {
    const int n = g_in[i].size();
    for (int j = 0; j != n; ++j) {
      if (g_in[i][j] != ' ') {
        from_googlerese[g_in[i][j] - 'a'] = g_out[i][j];
      }
    }
  }
  
}

int main() {
  init_googlerese();
  
  int T;
  cin >> T;
  string tmp;
  getline(cin, tmp);

  for (int t = 1; t <= T; ++t) {
    string G;
    getline(cin, G);
    cout << "Case #" << t << ": ";
    for (int i = 0; i < G.size(); ++i) {
      if(G[i] == ' ') {
        cout << ' ';
      } else {
        cout << from_googlerese[G[i]-'a'];
      }
    }
    cout << '\n';
  }
  

  return 0;
}
