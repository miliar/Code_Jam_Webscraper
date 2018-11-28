#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<char,int> pci; 

char board[6][6];

bool win(char c){
    bool w;
    for(int i=0;i<4;i++){
        w = true;
        for(int j=0;j<4;j++) if( board[i][j]!=c && board[i][j] !='T') {w=false;}
        if(w) return true;

        w = true;
        for(int j=0;j<4;j++) if( board[j][i]!=c && board[j][i] !='T') {w=false;}
        if(w) return true;    
    }

    w = true;
    for(int i=0;i<4;i++) if( board[i][i]!=c && board[i][i] !='T') {w=false;}
    if(w) return true;

    w = true;
    for(int i=0;i<4;i++) if( board[3-i][i]!=c && board[3-i][i] !='T') {w=false;}
    if(w) return true;

    return false;
}

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        for(int i=0;i<4;i++) scanf("%s",board[i]);
        if(win('X')) printf("X won");
        else if(win('O')) printf("O won");
        else{
            bool empty=false;
            for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(board[i][j]=='.') empty=true;
            if(empty) printf("Game has not completed");
            else printf("Draw");
        }

        printf("\n");
    }

    return 0;
}
