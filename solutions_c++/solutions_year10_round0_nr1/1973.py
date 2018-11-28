#include <cstdio>

int t, m ,s, n;
int main(){
        scanf("%d", &t);
        for (int i=0; i<t; i++){
                scanf("%d %d", &m, &n);
                s = 1;
                for (int j=0; j<m; j++)
                        s*=2;
                s-=1;
                if ((s&n)==s) printf("Case #%d: ON\n", i+1); else printf("Case $%d: OFF\n", i+1);
        }
        return 0;
}
