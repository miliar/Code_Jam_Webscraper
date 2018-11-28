/*
 * Amit Mandal
 * Computer Science & Engineering
 * University of Dhaka
 */


#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<string>
#include<set>
#include<bitset>

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define INF (1<<30)
#define EPS 1e-9
#define PI acos(-1.0)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)<0?(-(a)):(a))
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define BIG(a) memset(a,63,sizeof(a))
#define SZ(a) ((int)a.size())
#define PB push_back
#define ALL(a) a.begin(),a.end()
#define ff first
#define ss second
#define MP make_pair

#define SF(a)  scanf("%d",&a)
#define PF printf
#define NL puts("")


using namespace std;
char G[11][11],dum[1000];

void input(){
    for(int i=0;i<4;i++) gets(G[i]);
    gets(dum);
}

bool win(char player){
    bool res=false;
    for(int j=0; j<4; j++){
        int cnt=0;
        for(int i=0; i<4; i++){
            if(G[j][i]==player || G[j][i]=='T') cnt++;
        }
        if(cnt==4){
            res=true; break;
        }
    }
    if(res) return true;

    for(int j=0; j<4; j++){
        int cnt=0;
        for(int i=0; i<4; i++){
            if(G[i][j]==player || G[i][j]=='T') cnt++;
        }
        if(cnt==4){
            res=true; break;
        }
    }
    if(res) return true;
    int cnt=0;
    for(int i=0; i<4; i++){
        if(G[i][i]==player || G[i][i]=='T') cnt++;
    }
    if(cnt==4) return true;
    cnt=0;
    for(int i=3,j=0; i>=0; i--,j++){
        if(G[j][i]==player || G[j][i]=='T') cnt++;
    }
    if(cnt==4) return true;

    return false;
}

bool unfinished(){
    bool res=false;
    int cnt=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(G[i][j]=='.') cnt++;
    if(cnt>0) res=true;
    return res;
}

int main()
{
   // READ("A-large.in");
   // WRITE("ALARGEout.in");
    int t;
    SF(t);    gets(dum);
    int kase=1;
    while(t--){
        input();
        printf("Case #%d: ",kase++);
        bool X= win('X');
        bool O= win('O');
        bool fin=unfinished();

        if(X) puts("X won");
        else if(O) puts("O won");
        else if(!fin)puts("Draw");
        else if(fin)puts("Game has not completed");
    }
    return 0;
}

