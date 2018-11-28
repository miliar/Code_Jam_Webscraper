#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <cstdio>
#include <cstdlib>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

bool b[20][26];

bool match(const string& word) {
  for (int i = 0; i < word.length(); ++i) {
    if (!b[i][word[i]-'a']) return false;
  }
  return true;
}

int main()
{
        int tcase = 0;
        ifstream fin("z.in");
        ofstream fout("z.out");
        int l, d;
        fin >> l >> d;
        fin >> tcase;
        vector<string> words;
        string str;
        for (int i = 0; i < d; ++i) {
          fin >> str;
          words.push_back(str);
        }
        for (int tind = 1; tind <= tcase; tind++)
        {
          mset(b, 0);
          fin >> str;
          int k = 0;
          for (int i = 0; i < l; ++i) {
            if (str[k] == '(') {
              ++k;
              while (str[k] != ')') {
                b[i][str[k]-'a'] = true;
                ++k;
              }
              ++k;
            } else {
              b[i][str[k]-'a'] = true;
              ++k;
            }
          }
          int ans = 0;
          for (int i = 0; i < d; ++i)
            if (match(words[i])) {
              ans++;
            }
          fout << "Case #" << tind << ": " << ans << endl;
        }
        return 0;
}
