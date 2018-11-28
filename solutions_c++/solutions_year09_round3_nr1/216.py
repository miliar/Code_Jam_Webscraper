#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
  int T;
  cin>>T;
  for(int t=1;t<=T;t++) {
    string text;
    cin>>text;
    map<char, int> en;
    int next=1;
    bool zero=false;
    for(int i=0;i<text.size();i++) {
      if(en.find(text[i]) != en.end()) continue;
      if (i>0 && !zero) {
        en[text[i]] = 0;zero=true;
        continue;
      }
      en[text[i]]=next++;
    }
    long long int total=0;
    for(int i=0;i<text.size();i++) {
      total = next*total + en[text[i]];
    }
    printf("Case #%d: %lld\n", t, total);
  }
  return 0;
}
