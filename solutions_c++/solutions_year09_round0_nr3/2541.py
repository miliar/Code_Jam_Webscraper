#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int main(){
  ifstream cin("C-small.in");
  ofstream cout("welcome.txt");
  string welcome = "welcome to code jam";
  int tc;
  cin>>tc;
  cin.ignore();
  for(int i=0;i<tc;i++){
    string linea;
    getline(cin,linea);
    int M[19][linea.length()];
    memset(M,0,sizeof(M));
    for(int f=0;f<19;f++){
      for(int c=0;c<linea.length();c++){   
        if( (f-1) >= 0 && (c-1) >= 0 ){
            if(linea[c]==welcome[f])
                M[f][c]=M[f][c-1] + M[f-1][c];
            else
                M[f][c]=M[f][c-1];
        }else{
          if( (c-1) >= 0){
            if(linea[c]==welcome[f])
               M[f][c]=M[f][c-1]+1;
            else
               M[f][c]=M[f][c-1];
          }else{
             if(f ==0){
               if(linea[c]==welcome[f])
                 M[f][c]=1;   
             }    
          }      
        }
        if(M[f][c]>9999)
          M[f][c]=(M[f][c]%9999);  
      }
    }
    cout<<"Case #"<<i+1<<": ";
    if(M[18][linea.length()-1]<10)
      cout<<"0";
    if(M[18][linea.length()-1]<100)
     cout<<"0";
    if(M[18][linea.length()-1]<1000)
     cout<<"0";
    cout<<M[18][linea.length()-1]<<endl;
  }
 return 0; 
}
