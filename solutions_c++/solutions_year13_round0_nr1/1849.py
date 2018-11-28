#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
typedef long  long ll;

const int N = 100005;
const int inf = 1<<28;
const double eps = 1e-8;
using namespace std;
char s[10][10];

bool win(char d){
    int i,j;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(s[i][j]!=d&&s[i][j]!='T') break;
        }
        if(j==4) return 1;
        for(j=0;j<4;j++){
            if(s[j][i]!=d&&s[j][i]!='T') break;
        }
        if(j==4) return 1;
    }
    for(i=0,j=0;i<4;i++,j++){
        if(s[i][j]!=d&&s[i][j]!='T') break;
    }
    if(i==4) return 1;
    for(i=0,j=3;i<4;i++,j--){
        if(s[i][j]!=d&&s[i][j]!='T') break;
    }
    if(i==4) return 1;
    return 0;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        int cnt=0;
        for(int i=0;i<4;i++){
            scanf("%s",s[i]);
            for(int j=0;j<4;j++){
                if(s[i][j]=='.') cnt++;
            }
        }
        printf("Case #%d: ",cas++);
        if(win('X')) puts("X won");
        else if(win('O')) puts("O won");
        else{
            if(cnt) puts("Game has not completed");
            else puts("Draw");
        }
    }
    return 0;
}











