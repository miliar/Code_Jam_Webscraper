#include <cstdio>
#include <cstring>
using namespace std;

const char result[][10] = {"Neither", "Red", "Blue", "Both"};
const int Neither   =   0;
const int Red       =   1;
const int Blue      =   2;
const int Both      =   3;
const int MAXN  =   100+5;

char maps[MAXN][MAXN];
int N,K;

void input(){
    memset(maps, '.', sizeof(maps));
    scanf("%d%d", &N, &K);
    for(int i=1; i<=N; ++i){
        scanf("%s", &maps[i][1]);
    }
}

void moveRight(){
    for(int i=1; i<=N; ++i){
        for(int j=N; j>0; --j){
            if(maps[i][j] != '.')continue;
            int k = j;
            for(; k>0; --k)
                if(maps[i][k] != '.')
                    break;
            for(int l=j; k>0; --k,--l){
                maps[i][l] = maps[i][k];
                maps[i][k] = '.';
            }
        }
    }
    /*
    for(int i=1; i<=N; ++i){
        for(int j=1; j<=N; ++j)
            printf("%c", maps[i][j]);
        printf("\n");
    }
    */  
}

bool row(int i,int j,int dx,int dy){
    char p = maps[i][j];
    for(int k=0; k<K; ++k, i+=dx, j+=dy){
        if(maps[i][j] != p)
            return false;
    }
    return true;
}

int check(){
    bool bw = false, rw = false;

    for(int i=1; i<=N; ++i){
        for(int j=1; j<=N; ++j){
            if(maps[i][j] == '.')continue;
            if(maps[i][j] == 'R' && rw)continue;
            if(maps[i][j] == 'B' && bw)continue;

            if(row(i, j, 0, 1) || row(i, j, 1, 0) || row(i, j, 1, -1)
                || row(i, j, 1, 1))
                (*(maps[i][j] == 'R'? &rw: &bw)) = true;
        }
    }

    int result = 0;
    if(bw)result |= 2;
    if(rw)result |= 1;
    return result;
}

int solve(){
    moveRight();
    return check();
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        input();
        printf("Case #%d: %s\n", i, result[solve()]);
    }
}

