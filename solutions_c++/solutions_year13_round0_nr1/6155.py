#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>

#define forn(i,n) for(int i = 0; i < n; i++) 

#define checkresult if(oc + tc == 4) {\
        return 'O';\
    }\
    if(xc + tc == 4) {\
        return 'X';\
    }\

int t, oc, xc, tc, dotsc, h,k, oc2, xc2, tc2;
char game[4][4];

using namespace std;

void CheckC(char c){
    if(c == '.') {
        dotsc++;
    }            

    if(c == 'O'){
        oc++;
    } 
    if(c == 'X'){
        xc++;
    }
    if(c == 'T') {
        tc++;
    }    
}

char CheckState(){
    forn(i, 4){        
        oc = xc = tc = 0;
        forn(j, 4){       
            char c = game[i][j];
            CheckC(c);          
        }      
        checkresult
    }
    
    forn(i, 4){        
        oc = xc = tc = 0;
        forn(j, 4){        
            char c = game[j][i];
            CheckC(c);         
        }      
        checkresult
    }
    
    oc = xc = tc = 0;
    forn(i, 4){               
        char c = game[i][i];
        CheckC(c);
    }
    checkresult
    
    oc = xc = tc = 0;
    forn(i, 4){        
        char c = game[i][4-1-i]; 
        CheckC(c);
    }
    checkresult
    
    return 0;
}

char StateOfGame(){
    dotsc = 0;
    char c = CheckState();
    if(c != 0) return c;
    if(dotsc > 0) {
        return 'C';
    } else {
        return 'D';
    }
}

string s;
int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    cin>>t;
    
    forn(i, t){
        forn(x, 4) forn(y,4) {
            cin>>game[x][y];
        }
        
        char res = StateOfGame();
        
        printf("Case #%d: ", i+1);
        if(res == 'X')
            cout<<"X won";
        if(res == 'O')
            cout<<"O won";
        if(res == 'D')
            cout<<"Draw";
        if(res == 'C')
            cout<<"Game has not completed";
        cout<<'\n';
    }
    
    return 0;
}


