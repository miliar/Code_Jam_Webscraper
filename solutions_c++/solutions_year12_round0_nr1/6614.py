#include <iostream>
#include <string>

using namespace std;

char mapping[30];
bool mark[30];


void initMap(string S, string G) {
  for (int i = 0; i < S.length(); ++i) 
    if (S[i] != ' ') {
        mapping[S[i]-'a'] = G[i];
        mark[G[i]-'a'] = false;
    }
}

void init() {
    memset(mark, true, sizeof(mark));
    for (int i = 0; i < 30; ++i)
      mapping[i] = '#';
    string S = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string G = "our language is impossible to understand";
    initMap(S, G);
    S = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    G = "there are twenty six factorial possibilities";
    initMap(S, G);
    S = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    G = "so it is okay if you want to just give up";
    initMap(S, G);
    mapping['z'-'a'] = 'q';
    mapping['q'-'a'] = 'z';
}

void solve() {
    int T;
    cin >> T;
    cin.ignore();
    for (int i = 0; i < T; ++i) {
        string S;
        getline(cin, S);
        string G = "";
        for (int j = 0; j < S.length(); ++j) 
          if (S[j] == ' ') G = G + " ";
        else G = G + mapping[S[j]-'a'];
        cout << "Case #" << i+1 << ": " << G << endl;
    }
    
}


int main() {
  init();
  solve();
  return 0;
}

