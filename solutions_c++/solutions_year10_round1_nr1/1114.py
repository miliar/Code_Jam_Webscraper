#include <iostream.h>
#include <fstream>
   
using namespace std;


int main(){
       int n,k,t,cont=0,top=0;
       ifstream entrada("A-large (2).in");
       ofstream salida("solu.txt");
       entrada>>t; 
       while(t>0){
                  cont++;
                  entrada>>n>>k;
                  bool r=false, bl=false;
                  char are[n][n];
                  for(int i=0;i<n;i++){
                          for(int j=0;j<n;j++){
                                  entrada>>are[i][j];
                                  }
                          }
                  for(int i=0;i<n;i++){
                          top=n-1;
                          for(int j=n-1;j>=0;j--){
                                  if(are[i][j]!='.'){
                                        are[i][top]=are[i][j];
                                        if(j!=top)are[i][j]='.';
                                        top--;
                                  }
                          }
                  }
                  for(int i=0;i<n;i++){
                          for(int j=0;j<n;j++){
                                  if(are[i][j]!='.'){
                                        char ficha;
                                        int a,b,contador;
                                        bool siga=true;
                                        a=i;
                                        b=j;
                                        ficha=are[i][j];
                                        if((ficha=='R' && !r) || (ficha=='B' && !bl)){
                                            contador=0;
                                            while(a<n && b>=0 && siga && contador!=k){
                                                      if(are[a][b]==ficha) contador++;
                                                      else siga=false;
                                                      a++;
                                                      b--;
                                                      }
                                            if(contador==k){
                                                      if(are[i][j]=='R')r=true;
                                                      else bl=true;
                                                      contador=0;
                                                      }
                                            a=i;
                                            b=j;
                                            siga=true;
                                            contador=0;
                                            while(a<n && siga && contador!=k){
                                                      if(are[a][b]==ficha) contador++;
                                                      else siga=false;
                                                      a++;
                                                      }
                                            if(contador==k){
                                                      if(are[i][j]=='R')r=true;
                                                      else bl=true;
                                                      contador=0;
                                                      }          
                                            a=i;
                                            b=j;
                                            siga=true;
                                            contador=0;
                                            while(a<n && b<n && siga && contador!=k){
                                                      if(are[a][b]==ficha) contador++;
                                                      else siga=false;
                                                      a++;
                                                      b++;
                                                      }
                                            if(contador==k){
                                                      if(are[i][j]=='R')r=true;
                                                      else bl=true;
                                                      contador=0;
                                                      }
                                            a=i;
                                            b=j;
                                            siga=true;
                                            contador=0;
                                            while(b<n && siga && contador!=k){
                                                      if(are[a][b]==ficha) contador++;
                                                      else siga=false;
                                                      b++;
                                                      }
                                            if(contador==k){
                                                      if(are[i][j]=='R')r=true;
                                                      else bl=true;
                                                      contador=0;
                                                      }
                                        }
                                        }
                                  }
                          }
                          if(r && bl) salida<<"Case #"<<cont<<": Both"<<endl;
                          else if(r) salida<<"Case #"<<cont<<": Red"<<endl;
                          else if(bl) salida<<"Case #"<<cont<<": Blue"<<endl;
                          else salida<<"Case #"<<cont<<": Neither"<<endl;
                  
                  /*for(int i=0;i<n;i++){
                          for(int j=0;j<n;j++){
                                  cout<<are[i][j];
                                  }
                                  cout<<endl;
                  }*/
                  t--;
       }
}
