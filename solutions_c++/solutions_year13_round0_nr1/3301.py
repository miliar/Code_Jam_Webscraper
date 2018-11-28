#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

int main(){
    char a[4][4]; int t,f,r;
    cin>>t;
    for (int tt=1; tt<t+1; ++tt){
        //cout<<"TT"<<tt<<endl;
        f=0; r=0;
        for (int i=0; i<4; ++i){
            int redX=0,redO=0;
            for (int j=0; j<4; ++j){
                scanf(" %c", &a[i][j]);
                //cout<<"AAA"<<i<<" "<<j<<a[i][j]<<endl;
                redX+=(a[i][j]=='X')||(a[i][j]=='T');
                redO+=(a[i][j]=='O')||(a[i][j]=='T');
                if (a[i][j]=='.') f=1;
            }
            if (redX==4){r=1; }
            if (redO==4){r=2; }
        }
        if (!r)
        for (int i=0; i<4; ++i){
            int redX=0,redO=0;
            for (int j=0; j<4; ++j){
                redX+=(a[j][i]=='X')||(a[j][i]=='T');
                redO+=(a[j][i]=='O')||(a[j][i]=='T');
            }
            if (redX==4){r=1; }
            if (redO==4){r=2; }
        }
        if (!r){
            int redX=0,redO=0;
            for (int i=0; i<4; ++i){
                redX+=(a[i][i]=='X')||(a[i][i]=='T');
                redO+=(a[i][i]=='O')||(a[i][i]=='T');
            }
            if (redX==4){r=1; }
            if (redO==4){r=2; }
        }
        if (!r){
            int redX=0,redO=0;
            for (int i=0; i<4; ++i){
                redX+=(a[i][3-i]=='X')||(a[i][3-i]=='T');
                redO+=(a[i][3-i]=='O')||(a[i][3-i]=='T');
            }
            if (redX==4){r=1; }
            if (redO==4){r=2; }
        }
        if (!r) r=3+f;
        cout<<"Case #"<<tt<<": ";
        if (r==1) cout<<"X won"<<endl;
        if (r==2) cout<<"O won"<<endl;
        if (r==3) cout<<"Draw"<<endl;
        if (r==4) cout<<"Game has not completed"<<endl;
    }
    return 0;
}



