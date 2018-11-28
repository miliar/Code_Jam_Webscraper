#include <string>
#include <map>
#include <iostream>

using namespace std;

int main() {
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  string source1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  string code1 = "our language is impossible to understand";
  string source2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  string code2 = "there are twenty six factorial possibilities";
  string source3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string code3 = "so it is okay if you want to just give up";

  map<char, char> lingvo;
  for(int i = 0; i < source1.size(); ++i) {
    lingvo[source1[i]] = code1[i];
  }
  for(int i = 0; i < source2.size(); ++i) {
   lingvo[source2[i]] = code2[i];
   }
  for(int i = 0; i < source3.size(); ++i) {
    lingvo[source3[i]] = code3[i];
  }

  lingvo['y'] = 'a';
  lingvo['q'] = 'z';
  lingvo['z'] = 'q';
  lingvo['e'] = 'o';


  for(char a = 'a'; a <= 'z'; ++a) {
   // cout << a << " " << lingvo[a] << endl;
  }
  

  int n = 0; 
  cin >> n;
  char str[200];
  cin.getline(str, 200);
  for(int i = 0; i < n; ++i) {
    cin.getline(str, 200);
    string q = str;
    string res;
    for(int j = 0; j < q.size(); ++j) {
      res.push_back(lingvo[q[j]]);
    }
    cout << "Case #" << i+1 << ": " << res << endl;
  }

  return 0;
}
