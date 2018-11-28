#include <stdio.h>
#include <string.h>
#include <memory.h>

const int Max = 1023;

struct LHS{
    char Name[110];
    int  Idx;
    LHS *Next;
} *Hash[Max + 1], Pool[101], *T;


int L, M, ti, HAns;
int hCode;
int n, Q, Ans, Qr[1001];
bool Vis[101];
char Str[110];

inline int g_Hash(char *S){
    L = strlen(S);
    M = L / 5;
    M >?= 1;
    HAns = 0;
    for ( ti = 0; ti < L; ti += M ){
        HAns += S[ti];
        HAns *= 26;
        HAns &= Max;
    }
    return HAns;
}

inline void Make_Idx(int Top){
    hCode = g_Hash(Pool[Top].Name);
    T = Hash[hCode];
    if ( T == NULL ){
        Hash[hCode] = &Pool[Top];
    }
    else{
        while ( T ->Next != NULL ){
            T = T ->Next;
        }
        T ->Next = &Pool[Top];
    }
}

void Input(){
    int i;
    memset(Hash, 0, sizeof(Hash));
    scanf("%d\n", &n);
    for ( i = 0; i < n; ++ i ){
        gets(Pool[i].Name);
        Pool[i].Next = NULL;
        Make_Idx(i);
    }
}

inline int Get_Idx(){
    hCode = g_Hash(Str);
    T = Hash[hCode];
    while ( T != NULL ){
        if ( strcmp(Str, T ->Name) == 0 ){
            return T ->Idx;
        }
        T = T ->Next;
    }
    return -1;
}

void Solve(){
    scanf("%d\n", &Q);
    int i, j, index, Lx = 1, Num;
    
    Ans = 0;
    memset(Vis, 0, sizeof(Vis) );
    Num = n;
    
    for ( i = 1; i <= Q; ++ i ){
        gets(Str);
        Qr[i] = Get_Idx();
    }
    for ( i = 1; i <= Q; ++ i ){
        index = Qr[i];
        if ( !Vis[index] ){
            Vis[index] = true;
            -- Num;
            if ( !Num ){
                ++ Ans;
                memset(Vis, 0, sizeof(Vis) );
                Num = n;
                -- i;
            }
        }
    }
}
        
int main(){
    int t, Tic;
    for ( Tic = 0; Tic < 101; ++ Tic){
        Pool[Tic].Idx = Tic;
    }
    scanf("%d\n", &t);
    for ( Tic = 1; Tic <= t; ++ Tic){
        Input();
        Solve();
        printf("Case #%d: %d\n", Tic, Ans);
    }
    return 0;
}
