#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

#define MAX 256

char buf[MAX];
int case_cnt = 1;

int main(void)
{
  int t;
  gets(buf);
  sscanf(buf, "%d", &t);
  while(t--) {
    gets(buf);
    string num = buf;
    string tmp = num;
    if(next_permutation(tmp.begin(), tmp.end())) {
      printf("Case #%d: %s\n", case_cnt++, tmp.c_str());
    }
    else {
      int cnt = 0;
      int freq[10];
      for(int i = 0; i < 10; i++) freq[i] = 0;
      for(int i = 0; i < num.size(); i++) {
        freq[num[i] - '0']++;
        if(num[i] != '0') cnt++;
      }
      string res = "";
      for(int i = 1; i < 10; i++) {
        if(freq[i] > 0) { res += string(1, i + '0'); freq[i]--; break; }
      }
      cnt--;
      for(int i = 0; i < (int) num.size() - cnt; i++) res += string(1, '0');
      for(int i = 1; i < 10; i++) while(freq[i]) { res += string(1, i + '0'); freq[i]--; }
      printf("Case #%d: %s\n", case_cnt++, res.c_str());
    }
  }    
    
  return 0;
}

