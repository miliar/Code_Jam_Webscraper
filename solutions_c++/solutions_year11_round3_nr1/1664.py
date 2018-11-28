#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
#include <string>

using namespace std;



int main(){
    
    ifstream inf;
    inf.open("input1.txt");
    
    ofstream outf;
    outf.open("output1.txt");
    
    int nt;
    inf>>nt;
    
    for (int it = 0; it<nt; it++){
      int n1,n2;
      inf>>n1>>n2;
      
      char ** s = new char *[n1];
      
      for(int i = 0; i < n1; i++){
              s[i] = new char[n2];
              for (int j = 0; j < n2; j++){
                  char c;
                  inf>>c;
                  //outf<<c;
                  s[i][j]=c;
                   
              }
      }
      
      int imp = 0;
      
      for (int i = 0; i < n1 && !imp; i++){
          for (int j = 0; j < n2 && !imp; j++){
              if (s[i][j] == '#'){
                 if (j+1 < n2 && i+1 < n1 && s[i][j+1] == '#' && s[i+1][j] == '#' && s[i+1][j+1] == '#'){
                    s[i][j] = '/';
                    s[i+1][j] = '\\';
                    s[i][j+1] = '\\';
                    s[i+1][j+1] = '/';
                 }
                 else {
                 imp = 1;     
                 }            
              }
          }    
      }
    
    outf<<"Case #"<<it+1<<":\n";
    if (imp) outf<<"Impossible"<<endl;
    else {
         for (int i = 0; i < n1; i++){
             for (int j = 0; j < n2; j++){
                 outf<<s[i][j];    
             }
             outf<<endl;    
         }     
    }
    
        
    }
    //cin>>nt;
    return 0;
    
}
