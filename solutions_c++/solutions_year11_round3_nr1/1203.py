#include <iostream>
#include <stdio.h>

using namespace std;

bool grid[60][60];
int var[60][60];
int R , C;

bool hajar(int x, int y){
    var[x][y]=1;
    if(x+1<=R&&var[x+1][y]==1) var[x+1][y]=3;
    else
    return 0;

    if(y+1<=C&&var[x][y+1]==1) var[x][y+1]=2;
    else
    return 0;

    if(var[x+1][y+1]==1) var[x+1][y+1]=4;
    else
    return 0;
    return 1;
}

bool cek(){

    for(int i=1;i<=R;i++)
    for(int j=1;j<=C;j++){
        if(var[i][j]==1) {if (hajar(i,j)==0) return 0;}
    }

    return 1;
}

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin>>T;
    for(int ts=1;ts<=T;ts++){
        cin >> R >> C;

        char c;
        for(int i=1;i<=R;i++)
        for(int j=1;j<=C;j++){
            cin >> c;
            if(c=='.') {grid[i][j]=0;var[i][j]=0;}
            else{
            grid[i][j]=1;var[i][j]=1;}
        }

        if(cek()==0) printf("Case #%d:\nImpossible\n",ts);
        else{
            printf("Case #%d:\n",ts);
            for(int i=1;i<=R;i++)
            for(int j=1;j<=C;j++){
                if(grid[i][j]==0) cout<<".";
                else{
                    if(var[i][j]==1) printf("/");
                    if(var[i][j]==2) printf("\\");
                    if(var[i][j]==3) printf("\\");
                    if(var[i][j]==4) printf("/");
                }
                if(j==C) cout<<endl;
            }
        }
    }

    return 0;
}
