#include<iostream>
using namespace std;
char map[5][5];
int checkrow(){
    int ans=-1;
    char tmp;
    for(int i=0;i<4;i++){
        tmp=map[i][0];
        if(tmp=='T')tmp=map[i][1];
        if(tmp=='.')continue;
        int j=1;
        for(;j<4;j++){
            if(map[i][j]=='T')continue;
            if(map[i][j]!=tmp)break;
        }
        if(j==4){
            if(tmp=='O')return 1;
            else if(tmp=='X')return 2;
        }
    }
    return -1;
}
int checkcom(){
    char tmp;
    for(int i=0;i<4;i++){
        tmp=map[0][i];
        if(tmp=='T')tmp=map[1][i];
        if(tmp=='.')continue;
        int j=1;
        for(;j<4;j++){
            if(map[j][i]=='T')continue;
            if(map[j][i]!=tmp)break;
        }
        if(j==4){
            if(tmp=='O')return 1;
            else if(tmp=='X')return 2;
        }
    }
    return -1;
}
int checksq(){
    char tmp=map[0][0];
    if(tmp=='T')tmp=map[1][1];
    int j=1;
    for(;j<4;j++){
        if(map[j][j]=='T')continue;
        if(map[j][j]!=tmp)break;
    }
    if(j==4){
       if(tmp=='O')return 1;
       else if(tmp=='X')return 2;
    }
    tmp=map[0][3];
    if(tmp=='T')tmp=map[1][2];
    j=1;
    for(;j<4;j++){
        if(map[j][3-j]=='T')continue;
        if(map[j][3-j]!=tmp)break;
    }
    if(j==4){
       if(tmp=='O')return 1;
       else if(tmp=='X')return 2;
    }
    return -1;
}

int main(){
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        bool falg=false;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>map[i][j];
                if(map[i][j]=='.')falg=true;
            }
        }
        int ans=checkrow();
        if(ans==-1){
            ans=checkcom();
            if(ans==-1)ans=checksq();
        }
        if(ans==1)cout<<"Case #"<<z<<": O won"<<endl;
        else if(ans==2)cout<<"Case #"<<z<<": X won"<<endl;
        else if(falg)cout<<"Case #"<<z<<": Game has not completed"<<endl;
        else cout<<"Case #"<<z<<": Draw"<<endl;
    }
}
