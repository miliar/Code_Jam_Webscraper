#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void input(void);
void solve(void);

int n, m;
string s;
int case_cnt = 1;

int main(void)
{
  int t;
  cin >> t;
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  cin >> m;
  cin >> s;
  n = s.size();
}

void solve(void)
{
  vector <int> perm(m);
  for(int i = 0; i < m; i++) perm[i] = i;
  
  int ans = n;
  do {
    string x;
    for(int i = 0; i < n; i++) x += s[m * (i / m) + perm[i % m]];
    int cnt = 0;
    char last = 0;
    for(int i = 0; i < n; i++) if(x[i] != last) { cnt++; last = x[i]; }
    if(cnt < ans) ans = cnt;
  } while(next_permutation(perm.begin(), perm.end()));
  
  printf("Case #%d: %d\n", case_cnt++, ans);
}



