#include <cstdio>
#include <cstring>
using namespace std;
 
bool xboard[4][4], oboard[4][4];
 
bool xWin(){
    for(int i=0;i<4;i++){
        if(xboard[i][0] && xboard[i][1] && xboard[i][2] && xboard[i][3])
            return true;
    }
    for(int i=0;i<4;i++){
        if(xboard[0][i] && xboard[1][i] && xboard[2][i] && xboard[3][i])
            return true;
    }
    
    if(xboard[0][0] && xboard[1][1] && xboard[2][2] && xboard[3][3])
        return true;
    
    if(xboard[0][3] && xboard[1][2] && xboard[2][1] && xboard[3][0])
        return true;
    
    return false;
}
 
bool oWin(){
    for(int i=0;i<4;i++){
        if(oboard[i][0] && oboard[i][1] && oboard[i][2] && oboard[i][3])
            return true;
    }
    for(int i=0;i<4;i++){
        if(oboard[0][i] && oboard[1][i] && oboard[2][i] && oboard[3][i])
            return true;
    }
    
    if(oboard[0][0] && oboard[1][1] && oboard[2][2] && oboard[3][3])
        return true;
    
    if(oboard[0][3] && oboard[1][2] && oboard[2][1] && oboard[3][0])
        return true;
    
    return false;
}
 
int main(){
    char s[10];
    int tc, cnt = 1;;
    scanf("%d",&tc);
    
    while(tc--){
        bool unfinished = false;
        memset(xboard,0,sizeof xboard);
        memset(oboard,0,sizeof oboard);
        
        for(int i=0;i<4;i++){
            scanf("%s",s);
            for(int j=0;j<4;j++){
                if(s[j]=='X')
                    xboard[i][j] = true;
                else if(s[j]=='O')
                    oboard[i][j] = true;
                else if(s[j]=='T'){
                    xboard[i][j] = true;
                    oboard[i][j] = true;
                }
                else unfinished = true;
            }
        }
 
        printf("Case #%d: ",cnt++);
        if(xWin()){
            printf("X won\n");
        }
        else if(oWin()){
            printf("O won\n");
        }
        else{
            if(unfinished) printf("Game has not completed\n");
            else printf("Draw\n");
        }
    }
    
    return 0;
}
