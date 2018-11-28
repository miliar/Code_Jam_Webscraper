#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)

int l, d, n;
vector<string> dict;

int can(string s, string d) {
    //cout << s << " " << d << endl;
    int j = 0;
    FR(i, l) {
          char ch = d[i];
          if (s[j]=='(') {
            bool fine = false;
            while (s[j]!=')') {                  
                  j++;
                  if (s[j]==ch) fine = true;
            }
            
            
            if (!fine) return 0;
          } else
            if (s[j]!=ch) return 0;
          j++;
    }
    //cout << "---" << j << " " << s.size() << endl;
    
    if (j!=s.size()) return 0;
    
    return 1;
}

int go(string s) {
    int ret = 0;
    FR(i, d) ret += can(s, dict[i]);
    return ret;
}

int main() {
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    
    cin >> l >> d >> n;
    
    string temp;
    getline(cin, temp);
    FR(i, d) {
          getline(cin, temp);
          dict.push_back(temp);                    
    }
    FR(i, n) {
          getline(cin, temp);
          printf("Case #%d: %d\n", i+1, go(temp));
    }    
    
    return 0;
}
