#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <set>

using namespace std;

#define MAX 1024

int get_it(vector <string> vs1, vector <string> vs2);
vector <string> parse_it(string s);

int case_cnt = 1;

int main(void)
{   
  int t;
  scanf("%d", &t);
  while(t--) {
    int n, m;
    char buf[MAX];  
    scanf("%d %d", &n, &m);
    set <vector <string> > seen;
    for(int i = 0; i < n; i++) {
      scanf(" %s", buf);
      seen.insert(parse_it(buf));
    }
    
    int res = 0;
    for(int i = 0; i < m; i++) {
      scanf(" %s", buf);
      vector <string> vs = parse_it(buf);
      set <vector <string> >::iterator it = seen.lower_bound(vs);
      int best = 100000;
      if(it == seen.end()) best = vs.size();
      else best = get_it(vs, *it);
      if(it != seen.begin()) best = min(best, get_it(vs, *(--it)));
      res += best;
      seen.insert(vs);
    }
    
    printf("Case #%d: %d\n", case_cnt++, res);
  }
      
    
  return 0;
}

int get_it(vector <string> vs1, vector <string> vs2)
{
  int res = 0;
  int i = 0;
  while(i < vs1.size() && i < vs2.size() && vs1[i] == vs2[i]) i++;
  while(i < vs1.size()) { res++; i++; }
    
  return res;
}

vector <string> parse_it(string s)
{
  vector <string> res;
  for(int i = 0; i < s.size(); i++) if(s[i] == '/') s[i] = ' ';
  
  string x;
  stringstream ss(s);
  while(ss >> x) res.push_back(x);
  
  return res;
}




