#include <stdio.h>
#include <memory.h>

struct Trips{
    int Lt, At;
} Trip[240];

int T, nA, nB, n, AnsA, AnsB;
int Match[201], Root[201], Now;
char S[10];
bool Con[201][201], Vis[201];

inline int Get_Time(){
    scanf("%s", S);
    return S[0] * 600 + S[1] * 60 + S[3] * 10 + S[4] - 32208;
}

void Input(){
    int i, j;
    scanf("%d", &T);
    scanf("%d%d", &nA, &nB);
    n = nA + nB;
    memset(Trip, 0, sizeof(Trip) );
    memset(Con, 0, sizeof(Con) );
    for ( i = 0; i < nA; ++ i){
        Trip[i].Lt = Get_Time();
        Trip[i].At = Get_Time();
    }
    for ( i = 0; i < nB; ++ i){
        Trip[i + nA].Lt = Get_Time();
        Trip[i + nA].At = Get_Time();
    }
    for ( i = 0; i < nA; ++ i ){
        for ( j = 0; j < nB; ++ j ){
            if ( Trip[j + nA].Lt - Trip[i].At >= T ){
                Con[i][j + nA] = true;
            }
            if ( Trip[i].Lt - Trip[j + nA].At >= T ){
                Con[j + nA][i] = true;
            }
        }
    }
}

int Dfs(int X){
    int i;
    for ( i = 0; i < n; ++ i ){
        if ( !Vis[i] && Con[X][i] ){
            Vis[i] = true;
            if ( Match[i] < 0 || Dfs(Match[i]) ){
                Match[i] = X;
                Root[i] = Now;
                return 1;
            }
        }
    }
    return 0;
}

void Solve(){
    int i;
    AnsA = AnsB = 0;
    memset(Match, 0xFF, sizeof(Match));
    for ( i = 0; i <= n; ++ i ){
        Root[i] = i;
    }
    for ( Now = 0; Now < n; ++ Now ){
        memset(Vis, 0, sizeof(Vis));
        Dfs(Now);
    }
    for ( i = 0; i < nA; ++ i){
        if ( Root[i] == i ){
            ++ AnsA;
        }
    }
    for ( i = 0; i < nB; ++ i){
        if ( Root[nA + i] == nA + i ){
            ++ AnsB;
        }
    }
/*    printf("$$ %d\n", T);
    printf("$$ %d\n", Trip[0].Lt);
    for ( i = 0; i < n; ++ i){
        printf("%d %d\n", i, Root[i]);
    }
*/
}

int main(){
    int t, Tic;
    scanf("%d", &t);
    for ( Tic = 1; Tic <= t; ++ Tic){
        Input();
        Solve();
        printf("Case #%d: %d %d\n", Tic, AnsA, AnsB);
    }
    return 0;
}
