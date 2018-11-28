#include <iostream.h>
#include <fstream>
   
using namespace std;

int limite(int n, int cab){
    cab++;
    if(cab==n) return 0;
    else return cab;
    }

int main(){
       int t,n,k,cont=0,r,cab,col,total;
       ifstream entrada("C-small-attempt1.in");
       ofstream salida("solu.txt");
       entrada>>t;
       while(t>0){
                  total=0;
                  cab=0;
                  cont++;
                  entrada>>r>>k>>n;
                  col=0;
                  int cola[n];
                  for(int i=0;i<n;i++){
                          entrada>>cola[i];
                          }
                  if(n==1) total=r;
                  else
                  while(r>0){
                      int num=0,temp=col;
                      bool sigue=true;
                      while(num<k && sigue){
                          if((num+cola[cab])<=k){
                                  num+=cola[cab];
                                  cab=limite(n,cab);
                                  temp=limite(n,temp);
                                  if(cab==col) sigue=false;
                          }
                          else {
                                  sigue=false;
                          }
                      }
                      sigue=true;
                      col=temp;
                      total+=num;
                      r--;
                  }
                  salida<<"Case #"<<cont<<": "<<total<<endl;
                  t--;
                  }
       return 0;
       }
