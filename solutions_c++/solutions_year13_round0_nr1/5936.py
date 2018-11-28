#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char map[10][10];
bool win(char p){
    bool tag;
    for(int i=0;i<4;i++){
        tag=true;
        for(int j=0;j<4;j++){
            if(map[i][j]!=p&&map[i][j]!='T'){
                tag=false;
                break;
            }
        }
        if(tag) return true;
    }
    for(int i=0;i<4;i++){
        tag=true;
        for(int j=0;j<4;j++){
            if(map[j][i]!=p&&map[j][i]!='T'){
                tag=false;
                break;
            }
        }
        if(tag) return true;
    }
    tag=true;bool tag2=true;
    for(int i=0;i<4;i++){
        if(map[i][i]!='T'&&map[i][i]!=p) tag=false;
        if(map[i][3-i]!='T'&&map[i][3-i]!=p) tag2=false;
    }
    if(tag||tag2) return true;
    return false;
}
int main()
{
  //  freopen("A-large.in","r",stdin);
 //   freopen("A-large.out","w",stdout);
    int test,t=1;
    cin>>test;
    while(t<=test){
        for(int i=0;i<4;i++) cin>>map[i];
        bool tag=win('X');
        if(tag){
            cout<<"Case #"<<t++<<": X won"<<endl;
            continue;
        }
        tag=win('O');
        if(tag){
            cout<<"Case #"<<t++<<": O won"<<endl;
            continue;
        }
        tag=false;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++) if(map[i][j]=='.') tag=true;
        }
        if(tag) cout<<"Case #"<<t++<<": Game has not completed"<<endl;
        else cout<<"Case #"<<t++<<": Draw"<<endl;
    }
    return 0;
}
