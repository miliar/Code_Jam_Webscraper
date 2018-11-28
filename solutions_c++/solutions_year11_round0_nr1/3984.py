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
    int botonActual;
    char robotActual;
    int posB=1,posO=1,tickB=1,tickO=1;
    int tickActual=1;
    int numOrdenes=0;
    int res;
    int posAux;
    int tickAux;
    int diff;
    fstream inputData;
    fstream outputData;
    outputData.open("./output.txt",fstream::out);
    inputData.open("./data.txt",fstream::in);
    inputData >> nCases;//We first read the number of cases
    for(i=0;i<nCases;i++){
        inputData >> numOrdenes;
        res=0;
        posB=1;posO=1;tickB=1;tickO=1;
        tickActual=1; 
        for(j=0;j<numOrdenes;j++){
            inputData >> robotActual;
            inputData >> botonActual;
            if(robotActual=='O'){
                posAux=abs(posO-botonActual);
                tickAux=tickActual-tickO;
                diff=tickAux-posAux;
                if(diff>=0){
                      tickActual=tickActual+1;
                      tickO=tickActual;
                      posO=botonActual;              
                }else{
                      tickActual=tickActual+1;
                      tickActual=tickActual+abs(diff);
                      tickO=tickActual;
                      posO=botonActual;
                      res=res+abs(diff);      
                }            
            }else{
                posAux=abs(posB-botonActual);
                tickAux=tickActual-tickB;
                diff=tickAux-posAux;
                if(diff>=0){
                      tickActual=tickActual+1;
                      tickB=tickActual;
                      posB=botonActual;              
                }else{
                      tickActual=tickActual+1;
                      tickActual=tickActual+abs(diff);
                      tickB=tickActual;
                      posB=botonActual;
                      res=res+abs(diff);  
                  }                          
        }
        
        }
        res=res+numOrdenes;              
        outputData << "Case #" << i+1 << ": " << res << endl;

    }
    inputData.close();
    system("PAUSE");	
    return 0;
}
