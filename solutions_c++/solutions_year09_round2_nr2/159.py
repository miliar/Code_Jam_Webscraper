#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <set>
#include <vector>
#include <string>

using namespace std;

int main() {
  int t;
  scanf("%d",&t);
  for (int i = 0; i < t; i++) {
    printf("Case #%d: ",i+1);
    string s,s2;
    cin >> s;
    s2 = s;
    bool r = next_permutation(s2.begin(),s2.end());
    if (r == true) cout << s2 << endl;
    else {
      s2 = s;
    denovo:
      s2 = '0' + s2;
      s = s2;
      if (next_permutation(s2.begin(),s2.end()) == false) {
	s2 = s;
	goto denovo;
      }
      cout << s2 << endl;
    }    
  }
  return 0;
}
