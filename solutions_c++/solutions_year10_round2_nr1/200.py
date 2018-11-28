#include <cstdio>
#include <map>
#include <string>
#include <list>

class dir;

class dir {
private:
  std::map<std::string, dir> ds;
public:
  int insert(std::list<std::string> &v) {
    int x = 0;
    std::string s = v.front();
    v.pop_front();
    if(ds.end() == ds.find(s))
      x = 1;
    if(v.empty()) {
      ds[s];
      return x;
    }
    return ds[s].insert(v) + x;
  }
};

std::list<std::string> parse(char *str)
{
  int n=1;
  std::list<std::string> v;
  for(;;) {
    int m = n;
    while(str[m] && str[m] != '/')
      ++m;
    if(!str[m]) {
      v.push_back(str+n);
      break;
    }
    str[m] = 0;
    v.push_back(str+n);
    n = m+1;
  }
  return v;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int N, M;
    scanf("%d%d", &N, &M);
    char str[10000];
    dir root;
    for(int i=0; i<N; ++i) {
      scanf("%s", str);
      std::list<std::string> v = parse(str);
      root.insert(v);
    }
    int sum = 0;
    for(int i=0; i<M; ++i) {
      scanf("%s", str);
      std::list<std::string> v = parse(str);
      sum += root.insert(v);
    }
    printf("Case #%d: %d\n", t, sum);
  }
  return 0;
}
