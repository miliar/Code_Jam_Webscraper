#include <iostream>
#include <cstdio>
using namespace std;
bool xw,ow,dr;
int cse;
char brd[6][6];

void chk(int x,int y,int dx,int dy){
    int i=x;int j=y;
    int xc=0,oc=0,tc=0;
    for(;i<4&&j<4&&i>=0&&j>=0;i=i+dx,j=j+dy){
        if(brd[i][j]=='X') xc++;
        else if(brd[i][j]=='O') oc++;
        else if(brd[i][j]=='T') tc++;
    }
    if(xc==4) xw=1;
    if(oc==4) ow=1;
    if(xc==3 && tc==1) xw=1;
    if(oc==3 && tc==1) ow=1;

    return;
}


int main(){
    freopen("a.txt","rt",stdin);
    freopen("a.out","wt",stdout);
    cin>>cse;
    for(int run=1;run<=cse;run++){
        xw=0;ow=0;dr=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++){
                cin>>brd[i][j];
                if(brd[i][j]=='.') dr=1;
            }

    for(int i=0;i<4;i++){
        chk(i,0,0,1);
    }
    for(int j=0;j<4;j++){
        chk(0,j,1,0);
    }
    chk(0,0,1,1);
    chk(3,0,-1,1);

    if(xw==1) cout<<"Case #"<<run<<": X won\n";
    else if(ow==1) cout<<"Case #"<<run<<": O won\n";
    else if(dr==1) cout<<"Case #"<<run<<": Game has not completed\n";
    else cout<<"Case #"<<run<<": Draw\n";

    }



    return 0;

}
