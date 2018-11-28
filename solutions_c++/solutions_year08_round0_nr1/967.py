#include <cstdio>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define MAX_L 256

char buf[MAX_L];
vector <string> S;
set <string> used;

int main(void)
{
  int t;
  gets(buf);
  sscanf(buf, "%d", &t);
  for(int case_cnt = 1; case_cnt <= t; case_cnt++) {
    int n;
    gets(buf);
    sscanf(buf, "%d", &n);
    S.clear();
    for(int i = 0; i < n; i++) {
      gets(buf);
      S.push_back(buf);
    }
    
    int m;
    gets(buf);
    sscanf(buf, "%d", &m);
    
    int ans = 0;
    used.clear();
    for(int i = 0; i < m; i++) {
      gets(buf);
      used.insert(buf);
      if(used.size() == n) {
        used.clear();
        used.insert(buf);
        ans++;
      }
    }
    
    printf("Case #%d: %d\n", case_cnt, ans);
  }
        
  return 0;
}

