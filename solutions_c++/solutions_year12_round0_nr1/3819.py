#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string glr[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jvqz"};

string eng[] = {"our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give upzq"};

int map[26];

int main() {
  for (int i = 0; i < 26; i++) map[i] = -1;

  for (int i = 0; i < 3; i++) {
    for (int s = 0; s < glr[i].size(); s++) {
      if (glr[i][s] == ' ') continue;

      int g = glr[i][s] - 'a';
      int e = eng[i][s] - 'a';
      if (map[g] != -1 && map[g] != e) cout << "EEK! " << (char)('a'+e) << (char)('a'+g) << endl;
      map[g] = e;
    }
  }

  //for (int i = 0; i < 26; i++) cout << (char)(map[i]+'a');

  int N; cin >> N;
  string line;
  getline(cin, line);
  for (int i = 1; i <= N; i++) {
    getline(cin, line);
    string nl = line;
    for (int s = 0; s < line.size(); s++) {
      if (!isalpha(nl[s])) continue;
      nl[s] = 'a' + map[line[s] - 'a'];
    }
    cout << "Case #" << i << ": " << nl << endl;
  }
}
