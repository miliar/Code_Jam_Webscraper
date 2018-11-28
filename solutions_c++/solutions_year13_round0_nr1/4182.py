#include <iostream>
#include <string>
#include <sstream>
#include <utility>
#include <climits>
#include <vector>
#include <iterator>
#include <cctype>
#include <stack>

using namespace std;

int main(){
	int N;
	cin >> N;
	string dummy;
	getline(cin, dummy);
	for(int i = 0 ; i < N; ++i){
        string x[4];
        for(int j = 0; j < 4; ++j){
                getline(cin, x[j]);
        } 
        getline(cin, dummy);
        
        bool isXWin, isOWin;
        bool isFull = true;
        for(int j = 0 ; j < 4; ++j){ 
                isXWin = true;  
                isOWin = true;                    
                for(int k = 0; k < 4; ++k){
                        if(x[j][k] == '.') isFull = false;
                        
                        if(x[j][k] != 'X' && x[j][k] != 'T'){
                                  isXWin = false;                                          
                        }
                        if(x[j][k] != 'O' && x[j][k] != 'T'){
                                  isOWin = false;                                            
                        } 
                }
                if(isXWin) {
                  cout << "Case #" << (i+1) << ": X won" << endl;
                  break;
                }
                if(isOWin) {
                  cout << "Case #" << (i+1) << ": O won" << endl;
                  break;
                }
        }
        if(isXWin || isOWin) continue;
        
        for(int j = 0 ; j < 4; ++j){ 
                isXWin = true;  
                isOWin = true;                    
                for(int k = 0; k < 4; ++k){
                        if(x[k][j] != 'X' && x[k][j] != 'T'){
                                  isXWin = false;                                          
                        }
                        if(x[k][j] != 'O' && x[k][j] != 'T'){
                                  isOWin = false;                                            
                        } 
                }
                if(isXWin) {
                  cout << "Case #" << (i+1) << ": X won" << endl;
                  break;
                }
                if(isOWin) {
                  cout << "Case #" << (i+1) << ": O won" << endl;
                  break;
                }
        }
        if(isXWin || isOWin) continue;
        
        isXWin = true;  
        isOWin = true;                    
        for(int k = 0; k < 4; ++k){
                 if(x[k][k] != 'X' && x[k][k] != 'T'){
                            isXWin = false;                                          
                 }
                 if(x[k][k] != 'O' && x[k][k] != 'T'){
                            isOWin = false;                                            
                 } 
        }
        if(isXWin) {
          cout << "Case #" << (i+1) << ": X won" << endl;          
        }
        if(isOWin) {
          cout << "Case #" << (i+1) << ": O won" << endl;          
        }
        if(isXWin || isOWin) continue;
        
        isXWin = true;  
        isOWin = true;                    
        for(int k = 0; k < 4; ++k){
                 if(x[k][3-k] != 'X' && x[k][3-k] != 'T'){
                            isXWin = false;                                          
                 }
                 if(x[k][3-k] != 'O' && x[k][3-k] != 'T'){
                            isOWin = false;                                            
                 } 
        }
        if(isXWin) {
          cout << "Case #" << (i+1) << ": X won" << endl;          
        }
        if(isOWin) {
          cout << "Case #" << (i+1) << ": O won" << endl;          
        }
        if(isXWin || isOWin) continue;
                
        
        if(isFull) cout << "Case #" << (i+1) << ": Draw" << endl;
        else cout << "Case #" << (i+1) << ": Game has not completed" << endl;
           
	}
	return 0;
}
