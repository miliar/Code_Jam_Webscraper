#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>

using namespace std;

#define MAX_S 1024

void input(void);
void solve(void);

vector <string> parse_it(vector <string> vs);

double get_it(int id, int &pos);

char buf[MAX_S];
vector <string> tokens;
vector <string> names;
vector <set <string> > animals;
int case_cnt = 1;

int main(void)
{
  int t;
  gets(buf);
  sscanf(buf, "%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  int lines, n;
  vector <string> vs;
  
  gets(buf);
  sscanf(buf, "%d", &lines);
  for(int i = 0; i < lines; i++) {
    gets(buf);
    vs.push_back(buf);
  }
  
  tokens = parse_it(vs);
  
  gets(buf);
  sscanf(buf, "%d", &n);
  names.clear();
  animals.clear();
  for(int i = 0; i < n; i++) {
    gets(buf);
    stringstream ss(buf);
    string name;
    string feature;
    int cnt;
    ss >> name >> cnt;
    names.push_back(name);
    animals.push_back(set <string> ());
    for(int j = 0; j < cnt; j++) {
      ss >> feature;
      animals.back().insert(feature);
    }
  }
}

void solve(void)
{
  printf("Case #%d:\n", case_cnt++);
  for(int i = 0; i < names.size(); i++) {
    int pos = 0;
    printf("%.7lf\n", get_it(i, pos));
  }
}

double get_it(int id, int &pos)
{
  pos++;
  double res;
  sscanf(tokens[pos].c_str(), "%lf", &res);
  pos++;
  if(isalpha(tokens[pos][0])) {
    if(animals[id].find(tokens[pos]) != animals[id].end()) {
      pos++;
      res = res * get_it(id, pos);
      get_it(id, pos);
      pos++;
      return res;
    }
    else {
      pos++;
      get_it(id, pos);
      res = res * get_it(id, pos);
      pos++;
      return res;
    }
  }
  pos++;
  return res;
} 

vector <string> parse_it(vector <string> vs)
{
  string s = "";
  for(int i = 0; i < vs.size(); i++) s += " " + vs[i];
  
  vector <string> res;
  for(int i = 0; i < s.size(); ) {
    if(s[i] == '(') { res.push_back(string(1, '(')); i++; continue; }
    if(s[i] == ')') { res.push_back(string(1, ')')); i++; continue; }
    if(isdigit(s[i]) || s[i] == '.') {
      string tmp = "";
      while(i < s.size() && (isdigit(s[i]) || s[i] == '.')) { tmp += s[i]; i++; }
      res.push_back(tmp);
      continue;
    }
    if(isalpha(s[i])) {
      string tmp = "";
      while(i < s.size() && isalpha(s[i])) { tmp += s[i]; i++; }
      res.push_back(tmp);
      continue;
    }
    i++;
  }
  
  return res;
}

  
