#include<iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    
    for(int i=0; i<T; i++){
        int xboard[4][4];
        int oboard[4][4];
        
        int dotcount = 0;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                char t;
                cin >> t;
                
                if(t=='.'){
                    xboard[j][k] = 0;
                    oboard[j][k] = 0;
                    dotcount ++;
                }
                else if(t=='T'){
                    xboard[j][k] = 1;
                    oboard[j][k] = 1;
                }
                else if(t=='X'){
                    xboard[j][k] = 1;
                    oboard[j][k] = 0;
                }
                else if(t=='O'){
                    xboard[j][k] = 0;
                    oboard[j][k] = 1;
                }
            }
        }
        
        // Check oboard
        int diagsum = 0;
        int xdiagsum = 0;
        int success = 0;
        int colsum[4];
        
        for(int j=0; j<4; j++){
            colsum[j]=0;
        }
        for(int j=0; j<4; j++){
            diagsum += oboard[j][j];
            xdiagsum += oboard[3-j][j];
            int rsum = 0;
            for(int k=0; k<4; k++){
                colsum[k] += oboard[j][k];
                rsum += oboard[j][k];
            }
            if (rsum == 4){ 
                success = 1;
                break;
            }
        }   
        for(int j=0; j<4; j++){
            if (colsum[j]==4){
                success = 1;
                break;
            } 
        }    
        if(diagsum==4) success = 1;
        if(xdiagsum==4) success = 1;
        if(success == 1){
            cout << "Case #" << i+1 << ": " << "O won" << endl;
            continue;
        } 

        success = 0;
        diagsum = 0;
        xdiagsum = 0;
        // Check xboard
        for(int j=0; j<4; j++){
            colsum[j]=0;
        }
        for(int j=0; j<4; j++){
            diagsum += xboard[j][j];
            xdiagsum += xboard[3-j][j];
            int rsum = 0;
            for(int k=0; k<4; k++){
                colsum[k] += xboard[j][k];
                rsum += xboard[j][k];
            }
            if (rsum == 4){ 
                success = 1;
                break;
            }
        }   
        for(int j=0; j<4; j++){
            if (colsum[j]==4){
                success = 1;
                break;
            } 
        }    
        if(diagsum==4) success = 1;
        if(xdiagsum==4) success = 1;
        if(success == 1){
            cout << "Case #" << i+1 << ": " << "X won" << endl;
            continue;
        } 
        
        if(dotcount == 0){
            cout << "Case #" << i+1 << ": " << "Draw" << endl;
        }
        else{
            cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
        }        
    }
}
