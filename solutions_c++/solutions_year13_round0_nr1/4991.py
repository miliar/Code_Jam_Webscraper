#include<cstdio>
#include<cstring>
using namespace std;

const int N = 10;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define Me(x , y) memset(x , y , sizeof(x))

int n;
char ch[N][N];

int main(){
    freopen("a.in" , "r" , stdin);
    freopen("a.out" , "w" , stdout);
    scanf("%d" , &n);
    fo (p , 1 , n){
        printf("Case #%d: " , p);
        bool flag = 0;
        fo (i , 1 , 4) scanf("%s" , ch[i] + 1);
        fo (i , 1 , 4){
            bool tf = 0;
            fo (j , 1 , 4)
                if (ch[i][j] != 'X' && ch[i][j] != 'T'){
                    tf = 1; break;
                }
            if (!tf){
                puts("X won"); flag = 1; break;
            }
            tf = 0;
            fo (j , 1 , 4)
                if (ch[i][j] != 'O' && ch[i][j] != 'T'){
                    tf = 1; break;
                }
            if (!tf){
                puts("O won"); flag = 1; break;
            }
        }
        if (flag) continue;
        fo (i , 1 , 4){
            bool tf = 0;
            fo (j , 1 , 4)
                if (ch[j][i] != 'X' && ch[j][i] != 'T'){
                    tf = 1; break;
                }
            if (!tf){
                puts("X won"); flag = 1; break;
            }
            tf = 0;
            fo (j , 1 , 4)
                if (ch[j][i] != 'O' && ch[j][i] != 'T'){
                    tf = 1; break;
                }
            if (!tf){
                puts("O won"); flag = 1; break;
            }
        }
        if (flag) continue;
        bool tf = 0;
        fo (i , 1 , 4)
            if (ch[i][i] != 'X' && ch[i][i] != 'T'){
                tf = 1; break;
            }
        if (!tf){
            puts("X won"); continue;
        }
        tf = 0;
        fo (i , 1 , 4)
            if (ch[i][5 - i] != 'X' && ch[i][5 - i] != 'T'){
                tf = 1; break;
            }
        if (!tf){
            puts("X won"); continue;
        }
        tf = 0;
        fo (i , 1 , 4)
            if (ch[i][i] != 'O' && ch[i][i] != 'T'){
                tf = 1; break;
            }
        if (!tf){
            puts("O won"); continue;
        }
        tf = 0;
        fo (i , 1 , 4)
            if (ch[i][5 - i] != 'O' && ch[i][5 - i] != 'T'){
                tf = 1; break;
            }
        if (!tf){
            puts("O won"); continue;
        }
        tf = 0;
        fo (i , 1 , 4)
            fo (j , 1 , 4)
                if (ch[i][j] == '.') tf = 1;
        if (tf) puts("Game has not completed"); else puts("Draw");
    }
    return 0;
}
