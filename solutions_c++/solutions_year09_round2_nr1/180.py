#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

const int bufsize = (1<<16);
char buf[bufsize+10];
int left=0,pos=0;
inline char gc() {
  if(left<=0) { pos=0;
    left=fread(buf,1,bufsize,stdin);
    if(left<=0) return EOF;
  } --left; return buf[pos++];
}
inline char peek() {
  if(left<=0) { pos=0;
    left=fread(buf,1,bufsize,stdin);
    if(left<=0) return EOF;
  } return buf[pos];
}
inline int getint() {
  int x=0, znak=1;
  while((peek()<'0' || peek()>'9') && peek()!='-') gc();
  if(peek()=='-') { gc(); znak=-1; }
  while(peek()>='0' && peek()<='9') x=x*10+gc()-'0'; return x*znak;
}
inline bool iswhite(char x) {
  return x==' ' || x=='\n' || x=='\r' || x=='\t';
}
inline void skip() {
  while(iswhite(peek())) gc();
}
inline int getstr(char *s) {
  int n=0;
  skip();
  while(true) {
    char x=peek();
    if(x==EOF) break;
    if(iswhite(x)) break;
    if(x==')') break;
    s[n++]=gc();
  }
  s[n]=0;
  return n;
}

typedef long double LD;
const LD eps = 1e-7;

struct node {
  LD factor;
  bool leaf;
  string feature;
  node *left, *right;
};

char bufer[1000];
inline node *get() {
  node *x=new node;
  while(peek()!='(') gc();
  gc();
  skip();
  getstr(bufer);
  x->factor=atof(bufer);
  skip();
  if(peek()==')') {
    gc();
    x->leaf=true;
    x->left = x->right = 0;
  } else {
    x->leaf=false;
    getstr(bufer);
    x->feature = bufer;
    x->left = get();
    x->right = get();
    while(peek()!=')') gc();
    gc();
  }
  return x;
}

map<string,bool> cechy;
inline double pobierz(node *p) {
  if(p->leaf) return p->factor;
  else {
    if(cechy[p->feature]==true) {
      return p->factor*pobierz(p->left);
    } else {
      return p->factor*pobierz(p->right);
    }
  }
}

int main() {
  int zes = getint();
  for(int z=1; z<=zes; ++z) {
    int lines;
    lines = getint();
    node *root = get();
    int ile = getint();
    if(ile>0) printf("Case #%d:\n",z);
    for(int i=1; i<=ile; ++i) {
      getstr(bufer);
      cechy.clear();
      string name = string(bufer);
      int cnt = getint();
      for(int j=1; j<=cnt; ++j) {
        getstr(bufer);
        string feat = bufer;
        cechy[feat]=true;
      }
      printf("%.7lf\n",pobierz(root));
    }
  }
  return 0;
}
