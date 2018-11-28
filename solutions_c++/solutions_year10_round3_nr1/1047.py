#include <iostream.h>
#include <fstream>

using namespace std;

int main(){
       int n,k,t,cont=0;
       ifstream entrada("A-large (3).in");
       ofstream salida("solu.txt");
       entrada>>t; 
       while(t>0){
                  int cruces=0;
                  cont++;
                  entrada>>n;
                  int linea[n][2];
                  for(int i=0;i<n;i++){
                          entrada>>linea[i][0];
                          entrada>>linea[i][1];
                          }
                  for(int i=0;i<n;i++){
                          int inicia=linea[i][0];
                          int salida=linea[i][1];
                          for(int j=i+1;j<n;j++){
                                  if((inicia>linea[j][0] && salida<linea[j][1]) || (inicia<linea[j][0] && salida>linea[j][1]))
                                  cruces++;
                                  }
                          }
                  salida<<"Case #"<<cont<<": "<<cruces<<endl;
                  t--;
                  }
}
