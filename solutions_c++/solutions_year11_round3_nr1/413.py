#include <iostream>
#include <cstdlib>

using namespace std;
int main(){
  int T;
  cin >> T;
  for(int cases=1;cases<=T;++cases){
    int res=0;
    int R;
    int C;
    
    cin >> R >> C;
    char t[R][C];
    for(int j=0;j<R;++j){
      for(int k=0;k<C;++k){
        cin >>  t[j][k];
      }
    }
    

    
    
    int imp=0;
    for(int j=0;j<R;++j){
      for(int k=0;k<C;++k){
        if(t[j][k]=='#'){
          if(j+1==R || k+1==C ||t[j][k+1]!='#' || t[j+1][k]!='#' || t[j+1][k+1]!='#'){
            imp=1;
            break;
          }
          t[j][k]='/';
          t[j][k+1]='\\';
          t[j+1][k]='\\';
          t[j+1][k+1]='/';
          //         cout << t[j][k]; 
        }
        if(imp==1){
          break;
        }
        //      cout<<endl;
      }
    }
      
      //  res= max (timeo,timeb);
      if(imp){
        cout << "Case #"<<cases<<": "<<endl << "Impossible" << endl;
      }
      else{
        
        cout << "Case #"<<cases<<": "<<  endl;
        for(int j=0;j<R;++j){
          for(int k=0;k<C;++k){
            cout <<  t[j][k];
          }
          cout << endl;
        }
      }
    }
    
    return 0;
}