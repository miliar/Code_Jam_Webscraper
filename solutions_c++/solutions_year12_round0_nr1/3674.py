#include <cstdio>
#include <iostream>

using namespace std;

#define sz(x) ((int)(x).size())

const char op[26] = {
  'y', 'h', 'e', 's', 'o', 'c', 'v', 
  'x', 'd', 'u', 'i', 'g', 'l', 'b', 
  'k', 'r', 'z', 't', 'n', 'w', 'j',
  'p', 'f', 'm', 'a', 'q'};

int main()
{
  freopen("A.in", "r", stdin);
  //freopen("A.out", "w", stdout);
  
  int t; 
  scanf("%d\n", &t);
  
  for (int i = 0; i < t; ++i) {
    string s; getline(cin, s);
    for (int j = 0; j < sz(s); ++j) if (s[j] != ' ') {
      s[j] = op[s[j] - 'a'];
    }
    
    cout << "Case #" << i + 1 << ": " << s << '\n';
  }
  
  return 0;
}