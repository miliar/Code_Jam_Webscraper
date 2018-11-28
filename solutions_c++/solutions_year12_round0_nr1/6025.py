#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
    ifstream fin("fin.in");
    ofstream fout("fout.out");
           char g[]=".yhesocvxduiglbkrztnwjpfmaq";           
           int t;
           string str;
while(fin>>t) {
          for(int a=0;a<=t;a++) {
                      getline(fin,str);  
  if(a==0) {NULL;} else {
                      fout<<"Case #"<<a<<": ";
                                       for(int x=0;x<str.length();x++) {
                                           if(str[x]==' ') {fout<<" ";} else {
                                               int l=((int)str[x])-96;
                                               fout<<g[l];
                                                                              }
                                                                       }       
                                       fout<<"\n";     

                         }         }
              }
          return 0;}
                                       
