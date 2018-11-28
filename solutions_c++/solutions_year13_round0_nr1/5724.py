#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char s[5][5],ss[5];
bool _check(){

    if(ss[0]!=ss[1])return false;
    if(ss[1]!=ss[2])return false;
    if(ss[2]!=ss[3])return false;
    if(ss[0] == '.') return false;
    return true;
}
bool check(int num){
    for(int i = 0; i < 4; i++){
        ss[i] = s[num][i] ;
    }
    for(int i = 0; i < 4; i++){
        if(s[num][i] == 'T'){
            ss[i] = 'O';
            if(_check())return true;
            ss[i] = 'X';
            if(_check())return true;
        }
    }
    return _check();
}
int main(){
    int t,tt=1;
    freopen("A-small-attempt0 (2).in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d", &t);
    while(t--){
        printf("Case #%d: ",tt++);
        for(int i = 0; i < 4; i++)
            scanf("%s",s[i]);
        bool f = false;
        for(int i = 0; i < 4; i++)if(check(i)){
            printf("%c won\n",s[i][0]!='T'?s[i][0]:s[i][1]);
            f=true;break;
        }
        if(!f){
            for(int i = 0; i < 4; i++)
                for(int j=i+1; j < 4; j++)
                    swap(s[i][j],s[j][i]);
            for(int i = 0; i < 4; i++)if(check(i)){
            printf("%c won\n",s[i][0]!='T'?s[i][0]:s[i][1]);
            f=true;break;
            }
        }
        if(!f){
            char tmp1[5],tmp2[5];
            for(int i = 0; i < 4; i++)
                tmp1[i] = s[i][i];

            for(int i = 0; i < 4; i++)
                tmp2[i] = s[i][3-i];
            for(int i = 0; i < 4; i++)
                s[0][i] = tmp1[i];
            if(check(0)){f = true;printf("%c won\n",s[0][0]!='T'?s[0][0]:s[0][1]);}
            if(!f){
                for(int i = 0; i < 4; i++)
                    s[0][i] = tmp2[i];
                if(check(0)){f = true;printf("%c won\n",s[0][0]!='T'?s[0][0]:s[0][1]);}
            }
        }
        if(!f){
            for(int i = 0; i < 4 ; i++)
                for(int j = 0; j < 4; j ++)
                    if(s[i][j] == '.')
                        f = true;
            if(f){
                puts("Game has not completed");
            }else {
                puts("Draw");
            }
        }
    }
}

