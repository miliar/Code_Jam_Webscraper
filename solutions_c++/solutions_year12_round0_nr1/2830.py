#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

void cal_map(map<char, char>& m, vector<int>& v, const string& a, const string& b) {
  for(int i=0; i<a.length(); ++i) { m[a[i]] = b[i]; v[b[i]-'a'] = 1; }
}

int main(int argc, char** argv) {
  map<char, char> m;
  vector<int> v(26, 0);
  m['z'] = 'q'; v['q'-'a'] = 1;
  cal_map(m, v, "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
  cal_map(m, v, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
  cal_map(m, v, "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
  for(char ch = 'a'; ch <= 'z'; ch = ch+1) {
    if(m.find(ch) == m.end()){
      for(int i=0; i<26; ++i) if(v[i] == 0) m[ch] = 'a' + i;
      //      cout << ch << " *** : " << m[ch] << endl;
    }else {
      //      cout << ch << " : " << m[ch] << endl;
    }
  }
  
  int t=30;
  string g;
  ifstream fin(argv[1]);
  getline(fin, g);
  for(int i=1; i<=t; ++i){
    getline(fin, g);
    for(int j=0; j < g.length(); ++j)
      g[j] = m[g[j]];
    cout << "Case #"<< i << ": " << g << endl;
  }
  return 0;
}
