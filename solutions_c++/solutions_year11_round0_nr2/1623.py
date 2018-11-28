#include <iostream>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main(){
  int T; cin >> T;
  for(int cs = 1; cs <= T; ++cs){
    map<pair<char, char>, char> trans;
    map<char, vector<char> > opposed;
    map<char, int> count;
    int C; cin >> C;
    while(C--){
      string S; cin >> S;
      trans[pair<char, char>(S[0], S[1])] = S[2];
      trans[pair<char, char>(S[1], S[0])] = S[2];
    }
    int D; cin >> D;
    while(D--){
      string s; cin >> s;
      opposed[s[0]].push_back(s[1]);
      opposed[s[1]].push_back(s[0]);
    }
    int N; cin >> N;
    vector<char> elements;
    for(int i = 0; i < N; ++i){
      char ch; cin >> ch;
      if(elements.size() == 0){
        elements.push_back(ch);
        count[ch]++;
        continue;
      }
      if(trans.count(pair<char, char>(ch, elements.back()))){
        char tr = trans[pair<char, char>(ch, elements.back())];
        count[elements.back()]--;
        count[tr]++;
        elements.pop_back();
        elements.push_back(tr);
      }
      else{
        elements.push_back(ch);
        count[ch]++;
        vector<char> tmp = opposed[ch];
        for(int i = 0; i < tmp.size(); ++i){
          if(count[tmp[i]]){
            count.clear();
            elements.clear();
            break;
          }
        }
      }
    }
    string s = "[";
    for(int i = 0; i < elements.size(); ++i){
      if(i > 0) s += ", ";
      s += elements[i];
    }
    s += "]";
    printf("Case #%d: %s\n", cs, s.c_str());
  }
}
