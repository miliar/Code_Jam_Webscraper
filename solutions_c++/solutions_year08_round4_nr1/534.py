#include <stdio.h>
#include <string.h>

#define MAX_N   (200000)
#define TYPE_LEAF 0
#define TYPE_AND  1
#define TYPE_OR   2

int NN;
bool nodeval[MAX_N];
int nodetype[MAX_N];
bool changeable[MAX_N];

int maketrue(int node) {
    //printf("maketrue(%d)=", node);
    if (nodetype[node] == TYPE_LEAF) return nodeval[node] ? 0 : -1; //cant change leaf
    
    if (changeable[node] && nodetype[node] == TYPE_AND) {
        int res = maketrue(node * 2+1);
        int res2 = maketrue(node * 2 + 2);
        if (res < 0) {
            if (res2 < 0) {
                //printf("-1\n"); 
                return -1; 
            }
            //printf("%d\n", res2+1);
            return res2 + 1;
        } else {
            if (res2 < 0) {
                //printf("%d\n", res+1);
                return res + 1;
            }
            int changeleft = res + 1;
            int changeright = res2 + 1;
            int changeboth = res + res2;
            if (changeright < changeleft) changeleft = changeright;
            //printf("%d %d\n", changeleft, changeboth);
            return (changeleft < changeboth ? changeleft : changeboth);
        }
    } else {
        if (nodetype[node] == TYPE_AND) {
            int res = maketrue(node * 2+1);
            if (res < 0) {
                //printf("%d\n", res);
                return res;
            }
            int res2 = maketrue(node * 2 + 2);
            if (res2 < 0) { 
                //printf("%d\n", res2);
                return res2;
            }
            //printf("%d\n", res+res2);
            return res + res2;
        } else {
            int res = maketrue(node * 2+1);
            int res2 = maketrue(node * 2 + 2);
            if (res < 0 && res2 < 0) {
                //printf("%d\n", res); 
                return res;
            }
            //printf("%d %d\n", res, res2);
            if (res < 0) return res2;
            if (res2 < 0) return res;
            return (res < res2 ? res : res2);
        }
    }
}

int main() {
    int NTc;
    scanf("%d", &NTc);
    int i, j, k;
    for (int tc = 0; tc < NTc; tc++) {
        int V;
        printf("Case #%d: ", tc+1);
        scanf("%d %d", &NN, &V);
        memset(changeable, 0, sizeof(changeable));
        for (i = 0; i < (NN-1)/2; i++) {
            scanf("%d %d", &j, &k);
            nodetype[i] =  (j ^ V) ? TYPE_OR : TYPE_AND;
            changeable[i] = k;
        }
        for (; i < NN; i++) {
            scanf("%d", &j);
            nodetype[i] = TYPE_LEAF;
            changeable[i] = false;
            nodeval[i] = j ^ !V;
        }
        int res = maketrue(0);
        if (res < 0) printf("IMPOSSIBLE\n");
        else printf("%d\n", res);
    }
    return 0;
}
