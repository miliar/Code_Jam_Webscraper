#include <iostream>
#include <string>
#include <vector>


using namespace std;



int T=0,R=0,C=0;
char g[50][50];

int main(int argc,char** argv){

 
  cin >> T;
  for(int t=1;t<=T;t++){
  
    cin >> R >> C;
    for(int r=0;r<R;r++){
   
        cin >> g[r];
   
    }

    bool imp = false;
    for(int r=0;r<R;r++){
   
      for(int c=0;c<C;c++){

        if(g[r][c] == '#'){

          if(c < C-1 && r < R - 1){
            if(g[r][c] == '#' && g[r][c+1] == '#' && g[r+1][c] == '#' && g[r+1][c+1] == '#'){
              g[r][c] = '/'; g[r][c+1] = '\\'; g[r+1][c] = '\\' ; g[r+1][c+1] = '/';
            }else{
              imp = true;
              break; 
            
            }

          }else{
            imp = true;
            break;
          }
        }        
      
      }
   
    }

    cout << "Case #" << t << ": " << endl;
    if(imp){
      cout << "Impossible" << endl;    
    }else{
      for(int r=0;r<R;r++){
   
          cout << g[r] << endl;
      }
   }


  }

  
  return 0;
}   
 
