#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

char tab[100][100];
char S[100];

struct Tnode {
  double waga;
  char wlas[100];
  int next[2];
};

Tnode tree [10000];
int treeN;

void rec_tree(int v) {
  char c;
  scanf("%c", &c);
  while (c!='(') scanf("%c", &c);
  scanf("%lf", &tree[v].waga);
  scanf("%c", &c);
  while ((c!=')') && ((c<'a') || (c>'z'))) scanf("%c", &c);

  if (c==')') {
    tree[v].next[0]=tree[v].next[1]=-1;
  } else {

    int i=0;
    while ((c>='a') && (c<='z')) {
      tree[v].wlas[i++]=c;
      scanf("%c", &c);
    }
    tree[v].wlas[i]=0;

    int w=++treeN;
    tree[v].next[0]=w;
    rec_tree(w);
    w=++treeN;
    tree[v].next[1]=w;
    rec_tree(w);
    scanf("%c", &c);
    while ((c!=')')) scanf("%c", &c);
  }
}



struct ltstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) < 0;
  }
};



float licz() {
  int n;
  scanf("%s", S);
//printf("%s\n", S);
  scanf("%d", &n);
//printf("%d\n", n);
  for (int i=0; i<n; i++) {scanf("%s", tab[i]);}
// printf("%s\n", tab[i]);}
  set<const char*, ltstr>  W(tab, tab + n);
  double wyn=1.0;
  int v=0;
//printf("\n");
  for(;;) {
//printf("%d\n", v);
    wyn*=tree[v].waga;
    if (tree[v].next[0]==-1) break;
    v=tree[v].next[(W.count(tree[v].wlas))==0];
  }
//printf("\n");
  return wyn;
}


int main() {
  int Z;
  scanf("%d", &Z);
  for (int z=1; z<=Z; z++) {
    int N;

    scanf("%d", &N);
    treeN=0;
//printf("przed rec\n");
    rec_tree(0);
//printf("po rec\n");

    scanf("%d", &N);
    printf("Case #%d:\n", z);
    while (N--) printf("%.7lf\n", licz());
  }
  return 0;
}
