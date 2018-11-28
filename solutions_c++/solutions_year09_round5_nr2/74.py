#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

#define MAX 64
#define MOD 10009

void input(void);
void solve(void);

void back(int last, int cnt, int freq[MAX], int res[MAX], int zzz[MAX]);

int eval(int freq[MAX]);
vector <string> parse_it(string s);
int fact(int x);

int n, m;
vector <string> words;
vector <string> poly;
int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  char buf[1024];   
  scanf(" %s %d", buf, &m);
  poly = parse_it(buf);
  
  scanf("%d", &n);
  
  words.clear();
  for(int i = 0; i < n; i++) {
    scanf(" %s", buf);
    words.push_back(buf);
  }
}

void solve(void)
{
  int freq[MAX];
  int res[MAX];
  int zzz[MAX];
  memset(freq, 0, sizeof(freq));
  memset(res, 0, sizeof(res));
  memset(zzz, 0, sizeof(zzz));
  
  back(0, 0, freq, res, zzz);
  
  printf("Case #%d:", case_cnt++);
  for(int i = 1; i <= m; i++) printf(" %d", res[i]);
  printf("\n");
}

void back(int last, int cnt, int freq[MAX], int res[MAX], int zzz[MAX])
{
  if(cnt > 0) {
    int val = eval(freq);
    int z = fact(cnt);
    for(int i = 0; i < MAX; i++) z /= fact(zzz[i]);
    res[cnt] = (res[cnt] + val * z) % MOD;
  }
  
  if(cnt == m) return;
  
  for(int i = last; i < n; i++) {
    zzz[i]++;
    for(int j = 0; j < words[i].size(); j++) freq[words[i][j] - 'a']++;
    back(i, cnt + 1, freq, res, zzz);
    for(int j = 0; j < words[i].size(); j++) freq[words[i][j] - 'a']--;
    zzz[i]--;
  }
}

int eval(int freq[MAX])
{
  int res = 0;
  for(int i = 0; i < poly.size(); i++) {
    int term = 1;
    for(int j = 0; j < poly[i].size(); j++) {
      term = (term * freq[poly[i][j] - 'a']) % MOD;
    }
    res = (res + term) % MOD;
  }
    
  return res;
}

vector <string> parse_it(string s)
{
  for(int i = 0; i < s.size(); i++) if(s[i] == '+') s[i] = ' ';
       
  string tmp;
  stringstream ss(s);
  vector <string> res;
  while(ss >> tmp) res.push_back(tmp);
  
  return res;
}

int fact(int x)
{
  int res = 1;
  for(int i = 1; i <= x; i++) res = (res * i) % MOD;
  return res;
}
