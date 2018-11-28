#include <iostream>
using namespace std;

#define fori(a,b) for(a=0;(a)<(b);a++)

char T[4][5];

bool wins(const char C) {
    int i,k;
    bool horizontal,vertical,diagonal;
    fori(i,4){
        horizontal=true;
        vertical=true;
        fori(k,4){
            if (T[i][k]!='T' && T[i][k]!=C) horizontal = false;
            if (T[k][i]!='T' && T[k][i]!=C) vertical = false; 
        }
        if( horizontal || vertical ) return true;
    }
    diagonal = true;
    fori(i,4) {
        if (T[i][i]!='T' && T[i][i]!=C) diagonal = false;
    }
    if(diagonal) return true;
    diagonal = true;
    fori(i,4){
        if (T[3-i][i]!='T' && T[3-i][i]!=C) diagonal = false;
    }
    return diagonal;
}

bool completed() {
    int i,j;
    fori(i,4){
        fori(j,4){
            if( T[i][j] == '.' ) return false;
        }
    }
    return true;
}


int main() {
    int n,N;
    bool winsO,winsX;
    
    cin>>N;
    fori(n,N){
        cin>>T[0]>>T[1]>>T[2]>>T[3];
        winsO = wins('O');
        winsX = wins('X');
        if( winsO && !winsX )
            cout<<"Case #"<<n+1<<": O won"<<endl;
        else if( !winsO && winsX )
            cout<<"Case #"<<n+1<<": X won"<<endl;
        else if( winsO && winsX ) 
            cout<<"Case #"<<n+1<<": Draw"<<endl;
        else if( completed() ) 
            cout<<"Case #"<<n+1<<": Draw"<<endl;
        else
            cout<<"Case #"<<n+1<<": Game has not completed"<<endl;
    }
    
    return 0;
}
