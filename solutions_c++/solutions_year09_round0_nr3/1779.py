#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <string.h>
using namespace std;


long long get_(string s, int st, string m, int pos) {
  long long cnt=0;

  if(pos==m.size()-1) {
    for(int i=st; i<s.size(); i++) if(s[i]==m[pos]) cnt++;
    return cnt;
  }



  for(int i=st; i<s.size(); i++) {
    if(s[i]==m[pos]) {
      cnt=( cnt + get_(s, i+1, m, pos+1) ) % 10000;
    }
  }

  return cnt;
}



int main() {
  string m="welcome to code jam";

  int t;
  scanf("%d", &t);
  string tt;
  getline(std::cin, tt);
  for(int iii=1; iii<=t; iii++) {
    string s_;
    getline(std::cin, s_);

    string s=s_;
    int inc=0;
    for(int i=0; i<s_.size(); i++) {
      if(s_[i]=='w' || s_[i]=='e' || s_[i]=='l' || s_[i]=='c' || s_[i]=='o' || s_[i]=='m' || s_[i]=='t' || s_[i]=='d' || s_[i]=='j' || s_[i]=='a' || s_[i]==' ') { s[inc]=s_[i]; inc++; }
    }
    s=s.substr(0, inc);


    long long cnt=0;
    for(int i=0; i<s.size(); i++) {
      if(s[i]=='w') {
        cnt=( cnt + get_(s, i+1, m, 1) ) % 10000;
      }
    }


    char buf[80];
    sprintf(buf, "%lld", cnt);
    char buf2[80];
    if(strlen(buf)==1) sprintf(buf2, "000%s", buf);
    if(strlen(buf)==2) sprintf(buf2, "00%s", buf);
    if(strlen(buf)==3) sprintf(buf2, "0%s", buf);
    if(strlen(buf)==4) sprintf(buf2, "%s", buf);
    cout<<"Case #"<<iii<<": "<<buf2<<endl;




  }

  return 0;
}
