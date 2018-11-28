#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
int ntest;
string s[5];

int isValid(string t){
    sort(t.begin(),t.end());
    int c=t[0];
    if(c=='.') return 0;
    if(t[1]!=c || t[2]!=c) return 0;
    if(t[3]==c || t[3]=='Z'){
        if(c=='X') return 1;
        else return 2;
    }
    return 0;
}

int good(){
    for(int i=0; i<4; i++){
        string t="";
        for(int j=0; j<4; j++){
            t+= s[i][j];
        }
        int c = isValid(t);
        if(c) return c;
        t="";
        for(int j=0; j<4; j++){
            t+= s[j][i];
        }
        c = isValid(t);
        if(c) return c;
    }
    string t="";
    for(int j=0; j<4; j++){
        t+= s[j][j];
    }
    int c = isValid(t);
    if(c) return c;
    t="";
    for(int j=0; j<4; j++){
        t+= s[j][3-j];
    }
    c = isValid(t);
    if(c) return c;
    return 0;
}

bool isFinished(){
    for(int i=0;i<4; i++)
    for(int j=0; j<4; j++){
        if(s[i][j]=='.') return false;
    }
    return true;
}

void solve(int test){
    printf("Case #%d: ",test+1);
    int t = good();
    if(!t){
        if(isFinished()) printf("Draw\n");
        else printf("Game has not completed\n");
    }else{
        if(t==1){
            printf("X won\n");
        }
        else{
            printf("O won\n");
        }
    }
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d\n",&ntest);
    for(int t=0; t<ntest; t++){
        for(int i=0; i<4; i++){
            getline(cin,s[i]);
            for(int j=0; j<4; j++)
                if(s[i][j]=='T') s[i][j] = 'Z';
        }
        solve(t);
        if(ntest) scanf("\n");
    }
    return 0;
}
