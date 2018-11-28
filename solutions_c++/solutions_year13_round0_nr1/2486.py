#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int T; char s[10][10];
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        for(int i=0; i<4; i++) scanf("%s",s[i]);
        //for(int i=0; i<4; i++) printf("---- %s\n",s[i]);

        bool not_over = false, x = false, o = false;
        for(int i=0; i<16; i++){
            if( s[i/4][i%4]=='.' ) not_over = true;
        }

        bool same = false;
        for(int i=0; i<4; i++){
            same = true;
            for(int j=0; j<4; j++){
                if( s[i][j]!='X' && s[i][j]!='T' ) same = false;
            }
            if( same ) x = true;
            //if( i==0 ) cout<<same<<" "<<x<<endl;
        }
        for(int i=0; i<4; i++){
            same = true;
            for(int j=0; j<4; j++){
                if( s[j][i]!='X' && s[i][j]!='T' ) same = false;
            }
            if( same ) x = true;
        }
        same = true;
        for(int i=0; i<4; i++) if( s[i][i]!='X' && s[i][i]!='T' ) same = false;
        if( same ) x = true;
        same = true;
        for(int i=0; i<4; i++) if( s[i][3-i]!='X' && s[i][3-i]!='T' ) same = false;
        if( same ) x = true;


        same = false;
        for(int i=0; i<4; i++){
            same = true;
            for(int j=0; j<4; j++){
                if( s[i][j]!='O' && s[i][j]!='T' ) same = false;
            }
            if( same ) o = true;
        }
        for(int i=0; i<4; i++){
            same = true;
            for(int j=0; j<4; j++){
                if( s[j][i]!='O' && s[i][j]!='T' ) same = false;
            }
            if( same ) o = true;
        }
        same = true;
        for(int i=0; i<4; i++) if( s[i][i]!='O' && s[i][i]!='T' ) same = false;
        if( same ) o = true;
        same = true;
        for(int i=0; i<4; i++) if( s[i][3-i]!='O' && s[i][3-i]!='T' ) same = false;
        if( same ) o = true;
        
        printf("Case #%d: ",t);
        if( x ) printf("X won\n");
        else if( o ) printf("O won\n");
        else if( not_over ) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}

