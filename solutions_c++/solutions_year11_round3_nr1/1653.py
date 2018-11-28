#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <fstream>
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

int main(){
    ifstream in("A-large.in");
    ofstream out("A-large.out");

    int T;
    in>>T;
    int oo=1;
    while(T--){
               int R,C;
               in>>R>>C;
               char ip[100][100];
               int i=0;
               while(i<R)in>>ip[i++];
               bool flag =true;
               for(i=0;i<R;i++){
                      for(int j=0;j<C;j++){
                           if(ip[i][j]=='#'){
                                 
                                 if(i+1<R&&j+1<C&&ip[i][j+1]=='#'&&ip[i+1][j]=='#'&&ip[i+1][j+1]=='#'){
                                           ip[i][j]= ip[i+1][j+1] ='/';
                                           ip[i][j+1] = ip[i+1][j]='\\';
                                 }
                                 else{
                                      flag = false;
                                      break;
                                 }            
                           }
                      }
               }
               cout<<"Case #"<<oo<<":\n";
               out<< "Case #"<<oo<<":\n";
               if(flag){
                        for(i=0;i<R;i++){
                                  cout<<ip[i]<<'\n';
                                  out<<ip[i]<<'\n';
                        }
               }
               else {cout<<"Impossible\n";
                    out<<"Impossible\n";
               }   
        oo++;     
    }


    
    in.close();
    out.close();
    system("pause");
    return 0;
}
    
