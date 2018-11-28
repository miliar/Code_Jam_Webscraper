#include <iostream>
#include <cstring>
using namespace std;

int board[105][105];   //1 is read, 2 is blue
char c;
bool R, B;
int n, k, t, ans, tmp, t1, t2, x, y;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for(int a=1;a<=t;++a){
        R = B = 0;
        memset(board, 0, sizeof(board));
        scanf("%d%d", &n, &k);
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                scanf(" %c", &c);
                if(c == 'R') board[n-1-j][n-1-i] = 1;
                else if(c == 'B') board[n-1-j][n-1-i] = 2;
            }
        }
        for(int j=0;j<n;++j){
            tmp = 0;
            for(int i=0;i<n;++i){
                if(board[i][j] && i>tmp){
                    board[tmp][j] = board[i][j];
                    board[i][j] = 0;
                    ++tmp;
                }
                else if(board[i][j] && i == tmp) ++tmp;
            }
        }
        //horizontal
        for(int i=0;i<n;++i){
            t1 = t2 = 0;
            for(int j=0;j<n;++j){
                if(board[i][j] == 1) ++t1;
                else{
                    if(t1>=k) R = 1; t1 = 0;
                }
                if(board[i][j] == 2) ++t2;
                else{
                    if(t2>=k) B = 1; t2 = 0;
                }
            }
            if(t1>=k) R = 1;
            if(t2>=k) B = 1;
        }
        //vertical
        for(int j=0;j<n;++j){
            t1 = t2 = 0;
            for(int i=0;i<n;++i){
                if(board[i][j] == 1) ++t1;
                else{
                    if(t1>=k) R = 1; t1 = 0;
                }
                if(board[i][j] == 2) ++t2;
                else{
                    if(t2>=k) B = 1; t2 = 0;
                }
            }
            if(t1>=k) R = 1;
            if(t2>=k) B = 1;
        }
        for(int i=0;i<n;++i){
            t1 = t2 = 0;
            //increasing gradient
            for(x = i,y=0;x<n && y<n;++x,++y){
                if(board[x][y] == 1) ++t1;
                else{
                    if(t1>=k) R = 1; t1 = 0;
                }
                if(board[x][y] == 2) ++t2;
                else{
                    if(t2>=k) B = 1; t2 = 0;
                }
            }
            if(t1>=k) R = 1;
            if(t2>=k) B = 1;
            t1 = t2 = 0;
            for(x = 0,y=i;x<n && y<n;++x,++y){
                if(board[x][y] == 1) ++t1;
                else{
                    if(t1>=k) R = 1; t1 = 0;
                }
                if(board[x][y] == 2) ++t2;
                else{
                    if(t2>=k) B = 1; t2 = 0;
                }
            }
            if(t1>=k) R = 1;
            if(t2>=k) B = 1;
            t1 = t2 = 0;
            //decreasing gradient
            for(x = i,y=0;x>=0 && y<n;--x,++y){
                if(board[x][y] == 1) ++t1;
                else{
                    if(t1>=k) R = 1; t1 = 0;
                }
                if(board[x][y] == 2) ++t2;
                else{
                    if(t2>=k) B = 1; t2 = 0;
                }
            }
            if(t1>=k) R = 1;
            if(t2>=k) B = 1;
            t1 = t2 = 0;
            for(x = n-1,y=i;x>=0 && y<n;--x,++y){
                if(board[x][y] == 1) ++t1;
                else{
                    if(t1>=k) R = 1; t1 = 0;
                }
                if(board[x][y] == 2) ++t2;
                else{
                    if(t2>=k) B = 1; t2 = 0;
                }
            }
            if(t1>=k) R = 1;
            if(t2>=k) B = 1;
            t1 = t2 = 0;
        }
        printf("Case #%d: ", a);
        if(!R && !B) printf("Neither\n");
        else if(R && !B) printf("Red\n");
        else if(!R && B) printf("Blue\n");
        else printf("Both\n");
    }
 //   system("pause");
}
