#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>

using namespace std;

char buffer[100009];
class Directory {
  public:
  int add(const string& d) {
    int ret = 0;
    if (d=="/" || d=="") return 0;
    size_t i = d.find_first_of('/',1);
    string child;
    string rest;
    if (i==string::npos) {
        child = d;
        rest = "";
    } else {
      child = d.substr(0,i);
      rest = d.substr(i);
    }
    map<string,Directory>::iterator it = children.find(child);
    if (it==children.end()) {
      Directory dir;
      ret = 1+dir.add(rest);
      children[child] = dir;
    } else {
      ret = it->second.add(rest);
    }
    return ret;
  }  
  private:
  map<string,Directory> children;
};
int main() {
  int t,n,m;
  scanf("%d",&t);
  for (int tc=1; tc<=t; ++tc) {
    scanf("%d%d",&n,&m);
    Directory root;
    int ret = 0;
    while (n--) {
        scanf("%s",buffer);
        root.add(string(buffer));
    }
    while (m--) {
        scanf("%s",buffer);
        ret += root.add(string(buffer));
    }
    printf("Case #%d: %d\n",tc,ret);
  }
  return 0;
}
