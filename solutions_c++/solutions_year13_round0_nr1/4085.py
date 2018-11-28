#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;

int t;
int ct;
bool T, X, O, UC;
int outcome[10000];
char map[5][5];

int main(){
    scanf("%d",&t);
    for(int k=1;k<=t;k++){
        X=O=UC=false;
        for(int i=0;i<4;i++){
                scanf("%s",&map[i]);
        }    
        for(int i=0;i<4;i++){
            ct = 0;
            T = false;
            for(int j=0;j<4;j++){
                if(map[i][j]=='.'){
                    UC=true;
                    break;
                }
                if(map[i][j]=='X'){
                    ++ct;
                }else if(map[i][j]=='O'){
                    --ct;
                }else if(map[i][j]=='T'){
                    T=true;
                }
            }
            if(ct == 4){
                X = true;
            }else if(ct==-4){
                O = true;
            }else if(T){
                if(ct==3){
                    X=true;
                }else if(ct==-3){
                    O=true;
                }
            }
        }
        /////////////////
        for(int i=0;i<4;i++){
            ct = 0;
            T = false;
            
            for(int j=0;j<4;j++){
                if(map[j][i]=='.'){
                    UC=true;
                    break;
                }
                
                if(map[j][i]=='X'){
                    ++ct;
                }else if(map[j][i]=='O'){
                    --ct;
                }else if(map[j][i]=='T'){
                    T=true;
                }
            }
            if(ct == 4){
                X = true;
            }else if(ct==-4){
                O = true;
            }else if(T){
                if(ct==3){
                    X=true;
                }else if(ct==-3){
                    O=true;
                }
            }
        }
        //////////////
        ct = 0;
        T = false;
        for(int i=0;i<4;i++){
            if(map[i][i]=='.'){
                    UC=true;
                    break;
                }
            if(map[i][i]=='X'){
                ++ct;
            }else if(map[i][i]=='O'){
                --ct;
            }else if(map[i][i]=='T'){
                T=true;
            }
        }
        if(ct == 4){
                X = true;
            }else if(ct==-4){
                O = true;
            }else if(T){
                if(ct==3){
                    X=true;
                }else if(ct==-3){
                    O=true;
                }
            }
            ///////
        ct = 0;
            T = false;
        for(int i=0;i<4;i++){
            if(map[i][3-i]=='.'){
                UC=true;
                break;
            }
            if(map[i][3-i]=='X'){
                ++ct;
            }else if(map[i][3-i]=='O'){
                --ct;
            }else if(map[i][3-i]=='T'){
                T=true;
            }
        }
        if(ct == 4){
            X = true;
        }else if(ct==-4){
            O = true;
        }else if(T){
            if(ct==3){
                X=true;
            }else if(ct==-3){
                O=true;
            }
        }
        ///////////////////
        if(X && O){
            outcome[k-1] = 2;
        }else if(X){
            outcome[k-1] = 0;
        }else if(O){
            outcome[k-1] = 1;
        }else if(UC){ 
            outcome[k-1] = 3;
        }else{
            outcome[k-1] = 2;
        }
        
    }
    
    FILE * file;
    file = fopen ("tictactoetomek.out","w");
    for(int i=0;i<t;i++){    
        fprintf(file,"Case #%d: ",i+1);
        if(outcome[i]==2){
            fprintf(file,"Draw");
        }else if(outcome[i]==0){
            fprintf(file,"X won");
        }else if(outcome[i]==1){
            fprintf(file,"O won");
        }else if(outcome[i]==3){ 
            fprintf(file,"Game has not completed");
        }
        fprintf(file, "\n");
    }
}
