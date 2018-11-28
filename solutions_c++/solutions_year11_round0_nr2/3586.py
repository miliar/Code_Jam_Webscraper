#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;
int findvalue(int* a,int size,int value,int startV);
int main(int argc, char *argv[])
{
    int fd;
    int i,j,nCases;
    //VARIABLES DEL PROBLEMA
    int tam;
    int c,d,n;
    int k;
    char c1,c2,c3;
    char actual,aux;
    char composicion[26][26];
    bool opuestos[26][26];
    char resultado[100];
    //FIN VARIABLES DEL PROBLEMA
    fstream inputData;
    fstream outputData;
    outputData.open("./output.txt",fstream::out);
    inputData.open("./data.txt",fstream::in);
    inputData >> nCases;//We first read the number of cases
    for(i=0;i<nCases;i++){
        tam=0;
        for(j=0;j<100;j++) resultado[j]=' ';
        for(j=0;j<26;j++){
          for(k=0;k<26;k++){
           composicion[j][k]=0;
           opuestos[j][k]=false;                  
          }                
        }
        inputData >> c;
        for(j=0;j<c;j++){
            inputData >> c1 >> c2 >> c3;
            composicion[c1-'A'][c2-'A']=c3;
            composicion[c2-'A'][c1-'A']=c3; 
        }
        inputData >> d;
        for(j=0;j<d;j++){
            inputData >> c1 >> c2;
            opuestos[c1-'A'][c2-'A']=true;
            opuestos[c2-'A'][c1-'A']=true;
        }
        inputData >>n;
        for(j=0;j<n;j++){
            inputData >> actual;
            if(tam==0){
               resultado[0]=actual;
               tam++;     
            }else{
                  aux=resultado[tam-1];
                  if(composicion[actual-'A'][aux-'A']!=0){
                     resultado[tam-1]=composicion[actual-'A'][aux-'A'];                                        
                  }else{
                      for(k=0;k<tam;k++){
                         if(opuestos[actual-'A'][resultado[k]-'A']){
                         tam=0;
                         break;                                           
                         }                   
                      }
                      if(k==tam && tam!=0){
                                 resultado[tam]=actual;
                                 tam++;
                                 }    
                  }
                  }
        
        }
        outputData << "Case #" << i+1 << ": " << "[";
        for(k=0;k<tam;k++){
        outputData << resultado[k];
        if(k!=tam-1)
        outputData <<", ";                   
        }
        outputData << "]" << endl;

    }
    inputData.close();
    system("PAUSE");	
    return 0;
}
