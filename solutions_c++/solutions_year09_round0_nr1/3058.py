#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
using namespace std;

main(){
   

    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int l,d,n;
    in >> l >> d >>n;
    string dic[d],temp[3],signal[l],line,buff;

    //llenando el diccionario
    for (int i=0;i<d;i++){
       in >> dic[i];
    }
   
    //procesando la señal
    
    
    for (int i=0;i<n;i++){
       in >> line;
       int k=0;
       int j=0;
       while (line[k]!='\0'){ //separando la señal
           if (line[k] == '('){
           buff="";
           ++k;
              do{
                buff=buff+line[k];
                ++k;
              }while ( line[k]!=')');
           signal[j++]=buff; 
           }else
             signal[j++] = line[k];     
      k++; 
      }
      
      //comprobando las señales
     int cont=0; 
     for (int z=0; z<d;z++){
       bool sw=true;
       int pos=0;
       for (int x=0;x<l;x++){
          pos= signal[x].find(dic[z][x]);
          if (pos==-1){
            sw=false;
            break;
          }
            
       }
       if (sw)  
        cont++;               
     }
       out << "Case #" <<i+1 <<": "<<cont <<endl;
    }
       
}