#include <cstdlib>
#include <iostream>

using namespace std;

bool checkWin(bool* ptr){
     for(int i=0;i<4;i++){
             int spos = 4*i;
             if(ptr[spos+0] && ptr[spos+1] && ptr[spos+2] && ptr[spos+3])
               return true;
     }
     for(int i=0;i<4;i++){
             if(ptr[i] && ptr[i+4] && ptr[i+8] && ptr[i+12])
               return true;
     }
    if(ptr[0] && ptr[5] && ptr[10] && ptr[15])
               return true;
    if(ptr[3] && ptr[6] && ptr[9] && ptr[12])
               return true;
     
     return false;

}

int main(int argc, char *argv[])
{
    int num_case;
    bool X[4][4];
    bool O[4][4];
    bool hvEnded;
    scanf("%d", &num_case);
    for(int i=0;i<num_case;i++){
        hvEnded = true;
        memset(&X, 0, sizeof(bool) * 16);                
        memset(&O, 0, sizeof(bool) * 16);                
        
        char line[10];
        
        for(int l=0;l<4;l++){
                scanf("%s", &line);
                for(int j=0;j<4;j++){
                        switch(line[j]){
                              case 'X':
                                   X[l][j] = true;
                                   break;
                              case 'O':
                                   O[l][j] = true;
                                   break;
                              case 'T':
                                   X[l][j] = true;
                                   O[l][j] = true;
                                   break;
                              default:
                                   hvEnded = false;
                                   break;
                        }
                }                                
        }
        
        if(checkWin(X[0])) printf("Case #%d: X won\n", i+1);
        else if(checkWin(O[0])) printf("Case #%d: O won\n", i+1);
        else if(!hvEnded) printf("Case #%d: Game has not completed\n", i+1);       
        else printf("Case #%d: Draw\n", i+1);       
        
    }
}


