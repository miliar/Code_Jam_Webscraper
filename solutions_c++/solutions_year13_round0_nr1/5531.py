#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <deque>
using namespace std;
#define ot(x) cout<<x<<endl
#define cen cout<<endl
#define rep(a,b,c) for(i=a;i<b;i+=c)
#define rep2(a,b,c) for(j=a;j<b;j+=c)
#define repi(a,b,c) for(j=a;j>b;j-=c)


int i,t,n,k,m,x,y,a[1007],b[100],j,con,r,minm=1005,maks,poin;
long long int tmp;


int main(){
    string s[6], ss;
    char c[10][10];
    scanf("%d",&n);
    rep(0,n,1){
        cin>>s[0]>>s[1]>>s[2]>>s[3];
        printf("Case #%d: ",i+1);
        rep2(0,4,1){
            for(k=0;k<4;k++){
                if(s[j][k]=='T'){
                    x=j;
                    y=k;
                    k=5;
                    j=5;
                }
            }
        }
        int kon=0;
        if(!kon){
            s[x][y]='X';
            rep2(0,4,1){
                if(!s[j].compare("XXXX")||
                   s[0][j]=='X' && s[1][j]=='X' && s[2][j]=='X' && s[3][j]=='X'||
                    s[0][0]=='X' && s[1][1]=='X' && s[2][2]=='X' && s[3][3]=='X'||
                    s[0][3]=='X' && s[1][2]=='X' && s[2][1]=='X' && s[3][0]=='X'){
                        printf("X won\n");kon=1;j=5;
                    }
            }
        }
        if(!kon){
            s[x][y]='O';
            rep2(0,4,1){
                if(!s[j].compare("OOOO")||
                   (s[0][j]=='O' && s[1][j]=='O' && s[2][j]=='O' && s[3][j]=='O')||
                    (s[0][0]=='O' && s[1][1]=='O' && s[2][2]=='O' && s[3][3]=='O')||
                   (s[0][3]=='O' && s[1][2]=='O' && s[2][1]=='O' && s[3][0]=='O')){
                        printf("O won\n");kon=1;j=5;
                    }
            }
        }
        if(!kon){
            rep2(0,4,1){
                for(k=0;k<4;k++){
                    if(s[j][k]=='.'){
                        printf("Game has not completed\n");
                        kon=1;
                        k=5;
                        j=5;
                    }
                }
            }
        }
        if(!kon)
            printf("Draw\n");
    }
    return 0;
}

/*
1 1 1 2 3 3 4
1 2 1 3 1 3 4
9
1 1 1 1 1 2 3 3 3
*/
