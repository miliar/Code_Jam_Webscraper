#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 5000
#define M 500
#define L 15
struct node {
  struct node *ch[26];
}p[N*L];
int n, d, l;
int sz;
char s[100*L];
struct node *q[2][N], **cur, **nxt;
int ncur, nnxt;

int main()
{
  memset(&p[0], 0, sizeof(struct node));
  sz = 1;
  scanf("%d%d%d", &l, &d, &n);
  for(int i = 0; i < d; i++) {
    scanf("%s", s);
    struct node *pp = &p[0];
    for(int j = 0; j < l; j++) {
      if(pp->ch[s[j]-'a'] == NULL) {
        memset(&p[sz], 0, sizeof(struct node));
        pp->ch[s[j]-'a'] = &p[sz];
        ++sz;
      }
      pp = pp->ch[s[j]-'a'];
    }
  }
  for(int i = 0; i < n; i++) {
    scanf("%s", s);
    char *ps = s;
    cur = q[0]; nxt = q[1];
    cur[0] = &p[0]; ncur = 1;
    for(int j = 0; j < l; j++) {
      nnxt = 0;
      if(*ps=='(') {
        for(++ps; *ps != ')'; ++ps) {
          for(int k = 0; k < ncur; k++) {
            if(cur[k]->ch[*ps-'a'])
              nxt[nnxt++] = cur[k]->ch[*ps-'a'];
          }
        }
      } else {
        for(int k = 0; k < ncur; k++) {
          if(cur[k]->ch[*ps-'a'])
            nxt[nnxt++] = cur[k]->ch[*ps-'a'];
        }
      }
      ++ps;
      struct node **ptmp = cur; cur = nxt; nxt = ptmp;
      ncur = nnxt; nnxt = 0;
    }
    printf("Case #%d: %d\n", i+1, ncur);
  }
  return 0;
}
