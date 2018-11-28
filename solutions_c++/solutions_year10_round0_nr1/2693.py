#include <iostream.h>
#include <fstream>
   
using namespace std;

int main(){
       int t,n,k,cont=0;
       ifstream entrada("A-large.in");
       ofstream salida("solu.txt");
       entrada>>t; 
       while(t>0){
                  int ant=0,act=0;
                  cont++;
                  bool b=true;
                  entrada>>n>>k;
                  if(k!=0){
                      if(n!=1){
                          for(int i=0;i<n;i++){
                                  act=(ant*2)+1;
                                  ant=act;
                                  }
                          if((k-act)%(act+1)!=0) 
                               b=false;
                          if(b)
                               salida<<"Case #"<<cont<<": ON"<<endl;
                          else
                               salida<<"Case #"<<cont<<": OFF"<<endl;
                      }
                      else{
                           if(k%2!=0)
                                     salida<<"Case #"<<cont<<": ON"<<endl;
                           else
                                     salida<<"Case #"<<cont<<": OFF"<<endl;
                           }
                  }
                  else{
                       salida<<"Case #"<<cont<<": OFF"<<endl;
                       }
                  t--;
                  }
       return 0;
       }
