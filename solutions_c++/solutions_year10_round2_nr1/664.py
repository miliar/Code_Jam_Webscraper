#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <string>

using namespace std;

typedef struct dir *Dir;
struct dir {
  map<string,Dir> subdirs;
};

struct dir buffer[100100];
int used = 0;

int cria (Dir here, string path){
  int last = path.find_first_of("/");
  int bar = path.find_first_of("/", 1);
  int created = 0;
  while (bar != string::npos){
    string cur = path.substr(last+1, bar-last-1);
    if ((here->subdirs).count(cur) == 0){
      //printf("%s\n", cur.c_str());
      
      created++;
      (here->subdirs)[cur] = &buffer[used++];
    }
    here = (here->subdirs)[cur];
    last = bar;
    bar = path.find_first_of("/", last+1);
  }
  return created;
}

int main(){
  int t,n,m;
  char buf[121];
  string path;
  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++){
    for (int i = 0; i < used; i++)
      buffer[i].subdirs.clear();
    used = 0;
    Dir root = &buffer[used++];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++){
      scanf("%s", buf);
      path = buf;
      path.append("/");
      cria(root, path);
    }
    int created = 0;
    for (int i = 0; i < m; i++){
      scanf("%s", buf);
      path = buf;
      path.append("/");
      created += cria(root, path);
    }
    printf("Case #%d: %d\n", caso, created);
  }
  return 0;
}
