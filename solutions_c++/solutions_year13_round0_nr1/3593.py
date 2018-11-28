#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
typedef long long ll;
using namespace std;
char s[10][10];

bool work(char ch){
    int i,j;
    bool flag;
    for(i=0;i<4;i++){
        flag=1;
        for(j=0;j<4;j++)
            if(!(s[i][j]==ch || s[i][j]=='T')){
                flag=0;
                break;
            }
        if(flag) return 1;
    }
    for(j=0;j<4;j++){
        flag=1;
        for(i=0;i<4;i++)
            if(!(s[i][j]==ch || s[i][j]=='T')){
                flag=0;
                break;
            }
        if(flag) return 1;
    }
    flag=1;
    for(i=0;i<4;i++){
        if(!(s[i][i]==ch || s[i][i]=='T')){
            flag=0;
            break;
        }
    }
    if(flag) return 1;

    flag=1;
    for(i=0;i<4;i++){
        if(!(s[i][3-i]==ch || s[i][3-i]=='T')){
            flag=0;
            break;
        }
    }
    if(flag) return 1;
    return 0;
}

int main(){
    int t,T,i,j;
    bool flag;
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        for(i=0;i<4;i++) scanf("%s",s[i]);
        flag=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++)
                if(s[i][j]=='.'){
                    flag=1;
                    break;
                }
            if(flag) break;
        }
        bool ok1=work('X');
        bool ok2=work('O');
        printf("Case #%d: ",t);
        if(ok1==1){
            printf("X won\n");
        }
        else if(ok2==1){
            printf("O won\n");
        }
        else if(flag){
            printf("Game has not completed\n");
        }
        else printf("Draw\n");
    }

    return 0;
}
