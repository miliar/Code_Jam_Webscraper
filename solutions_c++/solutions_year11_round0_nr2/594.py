#include <stdio.h>
#include <string.h>

int form[30][30];
bool op[30][30];
char str[200], s[100];

int main () {
    int kase, i, n, c, w, v, m, h = 1;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d", &n);
          memset(form,-1,sizeof(form));
          memset(op,0,sizeof(op));
          for (i = 0; i < n; ++i) {
              scanf("%s", s);
              w = s[0]-'A';
              v = s[1]-'A';
              c = s[2]-'A';
              form[w][v] = c;
              form[v][w] = c;
          }
          scanf("%d", &m);
          for (i = 0; i < m; ++i) {
              scanf("%s", s);
              w = s[0]-'A';
              v = s[1]-'A';
              op[w][v] = 1;
              op[v][w] = 1;
          }
          int len;
          scanf("%d", &len);
          scanf("%s", str);
          int r[300];
          int top = 0, j;
          for (i = 0; i < len; ++i) {
              v = str[i]-'A';
              while (top > 0) {
                    if (form[r[top-1]][v] != -1) {
                       v = form[r[top-1]][v];
                       top--;
                    }        
                    else break;
              }
              r[top++] = v;
              for (j = 0; j < top-1; ++j)
                  if ( op[v][r[j]] ) {
                     top = 0;
                     break;
                  }
          }
          printf("Case #%d: ", h++);
          printf("[");
          for (i = 0; i < top; ++i) {
              if (i == 0) printf("%c", 'A'+r[i]);
              else printf(", %c", 'A'+r[i]);
          }
          printf("]");
          printf("\n");
    }
    return 0;
}
