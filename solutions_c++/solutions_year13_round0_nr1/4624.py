#include <bits/stdc++.h>
#define f(i,x,y) for (int i = int(x); i < int(y); i++)
#define fd(i,x,y) for(int i = int(x); i>= int(y); i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define pii pair<int,int>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define oo (1<<30)

using namespace std;

int main(){
    freopen("in.c","r",stdin);
    freopen("out.c","w",stdout);
    int TC,NC=1;
    scanf("%d\n",&TC);
    char tablero[5][5];
    while(TC--){
        f(i,0,4)    scanf("%s",tablero[i]);
        printf("Case #%d: ",NC++);
        //win horizontal
        int tmp = 0;
        f(i,0,4){
            map<char, int> m1;
            f(j,0,4)
                m1[tablero[i][j]]++;
            if(m1['O']==4){
                printf("O won\n");
                tmp = 1;
                break;  }
            if(m1['O']==3 && m1['T']==1){
                printf("O won\n");
                tmp = 1;
                break;  }
            if(m1['X']==4){
                printf("X won\n");
                tmp = 1;
                break;  }
            if(m1['X']==3 && m1['T']==1){
                printf("X won\n");
                tmp = 1;
                break; }
        }
        if(tmp == 1)    continue;
        f(j,0,4){
            map<char, int> m1;
            f(i,0,4)
                m1[tablero[i][j]]++;
            if(m1['O']==4){
                printf("O won\n");
                tmp = 1;
                break;  }
            if(m1['O']==3 && m1['T']==1){
                printf("O won\n");
                tmp = 1;
                break;  }
            if(m1['X']==4){
                printf("X won\n");
                tmp = 1;
                break;  }
            if(m1['X']==3 && m1['T']==1){
                printf("X won\n");
                tmp = 1;
                break; }
        }
        if(tmp == 1)    continue;
        map<char,int> m1;
        f(i,0,4)    m1[tablero[i][i]]++;
        if(m1['O']==4){
            printf("O won\n");
            continue;  }
        if(m1['O']==3 && m1['T']==1){
            printf("O won\n");
            continue;  }
        if(m1['X']==4){
            printf("X won\n");
            continue;  }
        if(m1['X']==3 && m1['T']==1){
            printf("X won\n");
            continue;  }
        m1.clear();
        f(i,0,4)    m1[tablero[i][3-i]]++;
        if(m1['O']==4){
            printf("O won\n");
            continue;  }
        if(m1['O']==3 && m1['T']==1){
            printf("O won\n");
            continue;  }
        if(m1['X']==4){
            printf("X won\n");
            continue;  }
        if(m1['X']==3 && m1['T']==1){
            printf("X won\n");
            continue;  }
        //empate o no terminaron
        f(i,0,4){
            int cont = 0;
            f(j,0,4){
                if(tablero[i][j]=='.')  cont++;
            }
            if(cont!=0){
                printf("Game has not completed\n");
                tmp = 1;
                break;
            }
        }
        if(tmp==1)  continue;
        printf("Draw\n");
    }
    return 0;
}

