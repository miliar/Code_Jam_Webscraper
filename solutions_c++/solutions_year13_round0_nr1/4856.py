#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;

#define maxn 10

int a[maxn][maxn];
bool have;
bool Xwon, Owon;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    int cases;
    int k;
    int i, j;
    char ch;
    int aa, bb;
    
    scanf("%d",&cases);
    for (k = 1; k <= cases; ++k) {
        printf("Case #%d: ",k);
        memset(a,0,sizeof(a));
        have = false;
        for (i = 0; i < 4; ++i) {
            scanf("%c",&ch);
            for (j = 0; j < 4; ++j) {
                scanf("%c",&ch);
                if (ch == '.') {
                    a[i][j] = -1;
                    have = true;
                }
                else if (ch == 'T') a[i][j] = 2;
                else if (ch == 'X') a[i][j] = 1;
                else if (ch == 'O') a[i][j] = 0;    
            }
        }
        scanf("%c",&ch);
        Xwon = false;
        Owon = false;
        for (i = 0; i < 4; ++i) {
            aa = 0; bb = 0;
            for (j = 0; j < 4; ++j){
                if (a[i][j] == 0) ++aa;
                if (a[i][j] == 2) ++bb;
            }
            if (aa == 4 || (aa == 3 && bb == 1)) {
                Owon = true;
                break;
            }
        }
        for (j = 0; j < 4; ++j) {
            aa = 0; bb = 0;
            for (i = 0; i < 4; ++i){
                if (a[i][j] == 0) ++aa;
                if (a[i][j] == 2) ++bb;
            }
            if (aa == 4 || (aa == 3 && bb == 1)) {
                Owon = true;
                break;
            }
        }
        aa = 0; bb = 0;
        for (i = 0; i < 4; ++i){
            if (a[i][i] == 0) ++aa;
            if (a[i][i] == 2) ++bb;
        }
        if (aa == 4 || (aa == 3 && bb == 1)) {
            Owon = true;
        }
        aa = 0; bb = 0;
        for (i = 0; i < 4; ++i){
            if (a[i][4-i-1] == 0) ++aa;
            if (a[i][4-i-1] == 2) ++bb;
        }
        if (aa == 4 || (aa == 3 && bb == 1)) {
            Owon = true;
        }
        
        
        //==========================//
        
        for (i = 0; i < 4; ++i) {
            aa = 0; bb = 0;
            for (j = 0; j < 4; ++j){
                if (a[i][j] == 1) ++aa;
                if (a[i][j] == 2) ++bb;
            }
            if (aa == 4 || (aa == 3 && bb == 1)) {
                Xwon = true;
                break;
            }
        }
        for (j = 0; j < 4; ++j) {
            aa = 0; bb = 0;
            for (i = 0; i < 4; ++i){
                if (a[i][j] == 1) ++aa;
                if (a[i][j] == 2) ++bb;
            }
            if (aa == 4 || (aa == 3 && bb == 1)) {
                Xwon = true;
                break;
            }
        }
        aa = 0; bb = 0;
        for (i = 0; i < 4; ++i){
            if (a[i][i] == 1) ++aa;
            if (a[i][i] == 2) ++bb;
        }
        if (aa == 4 || (aa == 3 && bb == 1)) {
            Xwon = true;
        }
        aa = 0; bb = 0;
        for (i = 0; i < 4; ++i){
            if (a[i][4-i-1] == 1) ++aa;
            if (a[i][4-i-1] == 2) ++bb;
        }
        if (aa == 4 || (aa == 3 && bb == 1)) {
            Xwon = true;
        }
        
        if (Xwon) printf("X won\n");
        else if (Owon) printf("O won\n");
        else if (!have) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;    
}
