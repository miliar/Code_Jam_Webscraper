#include <iostream>
#include <set>
#include <string>
#include <map>

using namespace std;

int count_diff(string s) {
  set<char> sc;
  for (size_t i=0;i<s.length();i++)
    sc.insert(s[i]);
  return sc.size();
}

int main() {
  int t;
  string str;
  cin >> t;
  for (int k=1;k<=t;k++) {
    cin >> str;
    int num = count_diff(str);
    set<char> used;
    map<char, int> m;
    m[str[0]]=1;
    
    bool used0=false;
    int next=2;
    
    for (size_t i=1;i<str.length();i++)
      if (m.find(str[i])==m.end()) {
	if (!used0) {
	  m[str[i]]=0;
	  used0=true;
	}
	else
	  m[str[i]]=next++;
      }

    unsigned long long cnt=0;
    unsigned long long power=1;
    int mul = num==1?2:num;
    for (int i=str.length()-1; i>=0;i--) {
      cnt+=m[str[i]]*power;
      power*=mul;
    }
    cout << "Case #" << k << ": " << cnt << endl;
  }
  return 0;
}
