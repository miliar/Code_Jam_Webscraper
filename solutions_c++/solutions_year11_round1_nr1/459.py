#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    int i,j,k,nCases;
    fstream inputData;
    fstream outputData;
    //VARIABLES DEL PROBLEMA
    long long int N;
    unsigned int pD,pG;
    unsigned int m;
    bool res;
    //FIN VARIABLES PROBLEMA
    outputData.open("./output.txt",fstream::out);
    inputData.open("./data.txt",fstream::in);
    inputData >> nCases;//We first read the number of cases
    for(i=0;i<nCases;i++){
    //CODIGO PROBLEMA POR CASOS
    inputData >> N;
    inputData >> pD;
    inputData >> pG;
    if((pG==100 && pD==100)||(pG==0 && pD==0)){
        res=true;
    }else if((pG==100 && pD!=100) || (pG==0 && pD!=0)){
         res=false;
          }else{
               m=1;
               while(m<=N && (m*pD %100)!=0)m++;
               if(m>N) res=false;
               else res=true; 
                }

    
    
    //FIN CODIGO PROBLEMA POR CASOS
    if(res){
       outputData << "Case #" << i+1 << ": "  << "Possible" << endl;        
       }else{
            outputData << "Case #" << i+1 << ": "  << "Broken" << endl;        
            }
    }
    inputData.close();
    system("PAUSE");	
    return 0;
}
