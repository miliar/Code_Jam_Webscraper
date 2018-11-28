#include <cstdio>
#include <cstdlib>
#include <cstring>

#define swap(a, b, type) type _swap_tmp = a; a = b; b = _swap_tmp;

typedef struct {
        short combo;
        char res;
        char eow;
} unit;

int comp(const void *a, const void * b) {
    return ((unit*) a)->combo - ((unit*) b)->combo;
}

int main() {
    int t, c, i, d, j, a = 1;
    char cb[100][4], op[50][3], cur[110], iv[110], *pt;
    unit *r;
    int ct[128], *_cb;
    scanf("%d", &t);
    while (t--) {
          memset(ct, 0, sizeof(ct));
          scanf("%d", &c);
          for (i = 0, _cb = (int*) cb; i < c; i++, _cb += 2) {
              scanf("%s", cb[i << 1]);
              *(_cb + 1) = *_cb;
              swap(cb[(i << 1) + 1][0], cb[(i << 1) + 1][1], char);
          }
          c <<= 1;
          qsort(cb, c, 4, comp);
          scanf("%d", &d);
          for (i = 0; i < d; i++) scanf("%s", op[i]);
          scanf("%*d %s", iv);
          pt = cur;
          for (i = 0; iv[i]; i++) {
              *(pt++) = iv[i];
              ct[iv[i]]++;
              // printf("[%d ", pt - cur);
              if (pt - cur >= 2) {
                 r = (unit*) bsearch(pt - 2, cb, c, 4, comp);
                 if (r != NULL) ct[*(--pt)]--, ct[*(--pt)]--, *(pt++) = r->res;
                 for (j = 0; j < d; j++) {
                     // printf("<%c %c %d %d>", op[j][0], op[j][1], ct[op[j][0]], ct[op[j][1]]);
                     if (ct[op[j][0]] && ct[op[j][1]]) {
                        pt = cur; memset(ct, 0, sizeof(ct));
                        break;
                     }
                 }
              }
              // printf("%d]", pt - cur);
          }
          *pt = 0;
          
          printf("Case #%d: ", a++);
          pt = cur;
          if (*pt) {
             printf("[%c", *pt);
             while (*(++pt)) printf(", %c", *pt);
          } else printf("[");
          
          printf("]\n");
    }
    return 0;
}
