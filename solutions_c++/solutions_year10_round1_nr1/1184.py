#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;
typedef pair<int,int> pii;
#define MAXN 123
char b[MAXN][MAXN], aux[MAXN][MAXN];
int cnt[MAXN], k;

void gravity(int n){
    memset(cnt, 0, sizeof(cnt));
    for(int i=n-1; i>=0; i--)
        for(int j=0; j<n; j++)
            if(aux[i][j] != '.'){
                swap(aux[n-1-(cnt[j]++)][j], aux[i][j]); 
            }
}

bool percurso(char c, vector< pii > &perc){
    
    char prev = 0;
    int cnt;
    for(int r=0; r<perc.size(); r++){
        int i = perc[r].first, j = perc[r].second;
        if(aux[i][j] != prev) cnt = 1;
        else cnt++;
        if(aux[i][j] == c && cnt >= k) return true;
        prev = aux[i][j];
    }
    return false;
}

bool verifica(char c, int n){
    //linha
    vector< pii > perc;
    for(int i=0; i<n; i++){
        perc.clear();
        for(int j=0; j<n; j++)
            perc.push_back(make_pair(i,j));
        if(percurso(c, perc)) return true;
    }
    //coluna
    for(int i=0; i<n; i++){
        perc.clear();
        for(int j=0; j<n; j++)
            perc.push_back(make_pair(j,i));
        if(percurso(c, perc)) return true;
    }
    //diagonal 1
    for(int i=0; i<n; i++){
        perc.clear();
        for(int j=0; i+j<n; j++)
            perc.push_back(make_pair(i+j, j));
        if(percurso(c, perc)) return true;
    }
    for(int j=0; j<n; j++){
        perc.clear();
        for(int i=0; i+j<n; i++)
            perc.push_back(make_pair(i, j+i));
        if(percurso(c, perc)) return true;
    }
    //diagonal 2
    for(int i=0; i<n; i++){
        for(int j=0; i+j<n; j++)
            perc.push_back(make_pair(i+j, n-1-j));
        if(percurso(c, perc)) return true;
        perc.clear();
    }
    for(int j=0; j<n; j++){
        perc.clear();
        for(int i=0; i+j<n; i++)
            perc.push_back(make_pair(i, j-i));
        if(percurso(c, perc)) return true;
    }
    return false;
}

int main (){

    int t, n, cases = 1;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d", &n, &k);
        for(int i=0; i<n; i++)
            scanf("%s", b[i]);
        //rotacao direita
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                aux[j][n-1-i] = b[i][j];

        gravity(n);
//         for(int i=0; i<n; i++){
//             for(int j=0; j<n; j++)
//                 printf("%c", aux[i][j]);
//             printf("\n");
//         }
        int rans = verifica('R', n);
        int bans = verifica('B', n);
        //rotacao esquerda

        printf("Case #%d: ", cases++);
        if(rans && bans) printf("Both\n");
        else if(rans) printf("Red\n");
        else if(bans) printf("Blue\n");
        else printf("Neither\n");
    }
                

    return 0;
}
