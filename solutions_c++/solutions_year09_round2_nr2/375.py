#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

string nextNum (string num) {
  int i;
  string res = num;
  for (i = res.size()-2; i >= 0; i--) {
    if (res[i] < res[i+1])
      break;
  }
  if (i >= 0) {
    char min = '9' + 1;
    int pos = 0;
    for (int j = i + 1; j < res.size(); j++) {
      if (res[j] > res[i] && res[j] < min) {
        min = res[j];
        pos = j;
      }
    }
    char temp = res[i];
    res[i] = res[pos];
    res[pos] = temp;
    sort(res.begin() + i + 1, res.end());
  }
  else {
    res += "0";
    sort(res.begin(), res.end());
    int i;
    for (i = 0; i < res.size(); i++) {
      if (res[i] != '0')
        break;
    }
    res[0] = res[i];
    res[i] = '0';
  }
      
  return res;
}

int main () {
  int N;
  scanf ("%d", &N);
  
  for (int k = 1; k <= N; k++) {
    char str[25];
    scanf("%s", str);
    string num = string(str);
    string res = nextNum(num);
    printf ("Case #%d: %s\n", k, res.c_str());
  }
  return 0;
}
