#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("entrada.txt");
ofstream fout("salida.out");

int C,R;

char T[4][4];

int search(char X){
    int i,e,c;

    for(i=0; i<4; i++){
        c=0;
        for(e=0; e<4; e++)
            if(T[i][e]==X || T[i][e]=='T')  c++;
        if(c==4)    return true;
    }

    for(i=0; i<4; i++){
        c=0;
        for(e=0; e<4; e++)
            if(T[e][i]==X || T[e][i]=='T')  c++;
        if(c==4)    return true;
    }

    for(c=i=0; i<4; i++)
            if(T[i][i]==X || T[i][i]=='T')  c++;
    if(c==4)    return true;

    for(c=i=0; i<4; i++)
            if(T[i][3-i]==X || T[i][3-i]=='T')  c++;
    if(c==4)    return true;

    return false;
}

int solve(){
    int i,e;
    bool fins;
    fins=1;
    for(i=0; i<4; i++){
        for(e=0; e<4; e++){
            fin>>T[e][i];
            if(T[e][i]=='.') fins=0;
        }
    }

    int a=search('X');
    int b=search('O');

    if( a && !b ) fout<<"X won"<<endl;
    else if( b && !a ) fout<<"O won"<<endl;
    else if(a == b && a==0 && fins) fout<<"Draw"<<endl;
    else fout<<"Game has not completed"<<endl;

}

int main(){
    int i;
    fin>>C;

    for(i=1; i<=C;i++){
        fout<<"Case #"<<i<<": ";
        solve();
    }

    return 0;
}
