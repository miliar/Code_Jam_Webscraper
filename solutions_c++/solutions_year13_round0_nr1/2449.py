#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<limits>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second
#define PP system("PAUSE");

using namespace std;

char mat[10][10];

int checkrow(int now){
    int cnt = 1;
    char tmp = mat[0][now];
    if(tmp == '.') return 0;
    if(tmp == 'T'){
        tmp = mat[1][now];
        cnt++;
        for(int i = 2; i < 4; i++)
            if(mat[i][now]==tmp || mat[i][now]=='T') cnt++;
        if(cnt==4 && tmp=='X') return 1;
        else if(cnt == 4) return 2;
    }
    for(int i = 1; i < 4; i++)
        if(mat[i][now]==tmp || mat[i][now]=='T') cnt++;
    if(cnt==4 && tmp=='X') return 1;
    else if(cnt == 4) return 2;
    return 0;
}
int checkcol(int now){
    int cnt = 1;
    char tmp = mat[now][0];
    if(tmp == '.') return 0;
    if(tmp == 'T'){
        tmp = mat[now][1];
        cnt++;
        for(int i = 2; i < 4; i++)
            if(mat[now][i]==tmp || mat[now][i]=='T') cnt++;
        if(cnt==4 && tmp=='X') return 1;
        else if(cnt == 4) return 2;
    }
    for(int i = 1; i < 4; i++)
        if(mat[now][i]==tmp || mat[now][i]=='T') cnt++;
    if(cnt==4 && tmp=='X') return 1;
    else if(cnt == 4) return 2;
    return 0;
}
int checkdia(int now){
    if(now&1){
        int cnt = 1;
        char tmp = mat[0][0];
        if(tmp == '.') return 0;
        if(tmp == 'T'){
            tmp = mat[1][1];
            cnt++;
            for(int i = 2; i < 4; i++)
                if(mat[i][i]=='T' || mat[i][i]==tmp) cnt++;
            if(cnt==4 && tmp=='X') return 1;
            else if(cnt == 4) return 2;
        }
        for(int i = 1; i < 4; i++)
            if(mat[i][i]=='T' || mat[i][i]==tmp) cnt++;
            if(cnt==4 && tmp=='X') return 1;
            else if(cnt == 4) return 2;
    }
    else{
        int cnt = 1;
        char tmp = mat[0][3];
        if(tmp == '.') return 0;
        if(tmp == 'T'){
            tmp = mat[1][2];
            cnt++;
            for(int i = 2; i < 4; i++)
                if(mat[i][3-i]=='T' || mat[i][3-i]==tmp) cnt++;
            if(cnt==4 && tmp=='X') return 1;
            else if(cnt == 4) return 2;
        }
        for(int i = 1; i < 4; i++)
            if(mat[i][3-i]=='T' || mat[i][3-i]==tmp) cnt++;
            if(cnt==4 && tmp=='X') return 1;
            else if(cnt == 4) return 2;
    }
    return 0;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int cc = 1; cc <= T; cc++){
        printf("Case #%d: ", cc);
        for(int i = 0; i < 4; i++)
            scanf("%s", mat[i]);
        int now = 0;
        bool flag = false;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                if(mat[i][j] == '.') flag = true;
        for(int i = 0; i < 4; i++){
            now = checkrow(i);
            if(now == 1){
                puts("X won");
                break;
            }
            if(now == 2){
                puts("O won");
                break;
            }
            now = checkcol(i);
            if(now == 1){
                puts("X won");
                break;
            }
            if(now == 2){
                puts("O won");
                break;
            }
            now = checkdia(i);
            if(now == 1){
                puts("X won");
                break;
            }
            if(now == 2){
                puts("O won");
                break;
            }
        }
        if(now==0 && flag) puts("Game has not completed");
        else if(now == 0) puts("Draw");
    }
    return 0;
}
