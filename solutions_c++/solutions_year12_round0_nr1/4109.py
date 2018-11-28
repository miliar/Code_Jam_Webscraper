#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;

string alfabeto1="abcdefghijklmnopqrstuvwxyz";
string alfabeto2="yhesocvxduiglbkrztnwjpfmaq";

void encontrar_secuencia(int num_caso,string entrada){

      int tam=0;
      int pos=0;
      tam=entrada.size();

      for(int i=0;i<tam;i++){

             pos=-1;

             for(int j=0;j<26;j++){

                 if(alfabeto1.at(j)==entrada.at(i)){
                     pos=j;
                     break;

                 }

             }
            if(pos==-1){
             entrada.replace(i,1," ");
            }
            else entrada.replace(i,1,alfabeto2.substr(pos,1));

      }

      cout<<"Case #"<<num_caso<<": "<<entrada<<endl;
}


int main()
{
     int num_casos=0;
     string entrada,num;

     getline(cin,num);
     num_casos=atoi(num.c_str());

     for(int i=0;i<num_casos;i++){

            getline(cin,entrada);
            encontrar_secuencia(i+1,entrada);

     }
     return 0;
}
