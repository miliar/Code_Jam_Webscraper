#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

//ifstream fin("a_small.in");
//ofstream fout("a_small.out");

vector<string> dict;
vector<string> tokens;

void process(string str)
{
  tokens.clear();
  int len = str.size(), i;
  for (i=0; i<len; ++i) {
    string temp = "";
    if (str[i] == '(') {
      ++i;
      while (i < len && str[i] != ')') {
        temp += str[i];
        ++i;
      }
      tokens.push_back(temp);
    } else {
      temp += str[i];
      tokens.push_back(temp);
    }
  }
}

int main()
{
  //freopen("a_large.in", "r", stdin);
  //freopen("a_large.out", "w", stdout);
  string temp;
  int length, diction, cases, i, t;
  scanf("%d%d%d\n", &length, &diction, &cases);
  dict.clear();
  for (i=0; i<diction; ++i) {
    cin >> temp;
    dict.push_back(temp);
  }

  for (t=1; t<=cases; ++t) {
    printf("Case #%d: ", t);
    cin >> temp;
    process(temp);
    int l, ans = 0;
    for (i=0; i<diction; ++i) {
      string cur = dict[i];
      for (l=0; l<length; ++l) {
        char curChar = cur[l];
        int ii, tokenLength = tokens[l].size();
        for (ii=0; ii<tokenLength; ++ii) {
          if (tokens[l][ii] == curChar) break;
        }
        if (ii >= tokenLength) break;
      }
      if (l >= length) ++ans;
    }
    printf("%d\n", ans);
  }
  
  return 0;
}
