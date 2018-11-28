#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#define infile "b.in"
#define outfile "b.out"
#define lgMax 131

using namespace std;

vector <string> v;
vector <string> w;
vector <string> sol;
int n, m;

void read() {
  scanf("%d %d\n", &n, &m);
  for(int i = 1; i <= n; ++i) {
    char chr[lgMax];
    string str;
    scanf("%s\n", chr);
    for(int j = 0; chr[j] >= 'a' && chr[j] <= 'z'; ++j)
      str.push_back(chr[j]);
    v.push_back(str);
  }
  for(int i = 1; i <= m; ++i) {
    char chr[lgMax];
    string str;
    scanf("%s\n", chr);
    for(int j = 0; chr[j] >= 'a' && chr[j] <= 'z'; ++j)
      str.push_back(chr[j]);
    w.push_back(str);
  }
}

bool belongs(string a, string w, char x) {
  for(unsigned i = 0; i < w.size(); ++i)
    if((a[i] == x || w[i] == x) && a[i] != w[i])
      return false;
  return true;
}

int getCost(string pattern, string word) {
  vector <string> aux;
  int res = 0;

  for(unsigned i = 0; i < v.size(); ++i)
    if(v[i].size() == word.size())
      aux.push_back(v[i]);

  reverse(pattern.begin(), pattern.end());
  while(aux.size() > 1) {
    for(unsigned i = 0; i < aux.size(); ++i) {
      char chr = pattern[pattern.size()-1];
      if(find(aux[i].begin(), aux[i].end(), chr) != aux[i].end()) {
        for(unsigned j = 0; j < aux.size(); ++j)
          if(!belongs(aux[j], word, chr))
            aux[j] = aux.back(), aux.pop_back(), j--;
        if(find(word.begin(), word.end(), chr) == word.end())
          res++;
        break;
      }
    }
    pattern.resize(pattern.size()-1);
  }

  return res;
}

void solve() {
  for(unsigned i = 0; i < w.size(); ++i) {
    int best = -1; string str;
    for(unsigned j = 0; j < v.size(); ++j) {
      int cur = getCost(w[i], v[j]);
      //printf("%s %d\n", v[j].c_str(), cur);
      if(cur > best) best = cur, str = v[j];
    }
    sol.push_back(str);
  }
}

void write(int t) {
  printf("Case #%d:", t);
  for(unsigned i = 0; i < sol.size(); ++i)
    printf(" %s", sol[i].c_str());
  printf("\n");
}

void clear() {
  v.clear();
  w.clear();
  sol.clear();
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  int t;
  scanf("%d\n", &t);
  for(int test = 1; test <= t; ++test) {
    read();
    solve();
    write(test);
    clear();
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
