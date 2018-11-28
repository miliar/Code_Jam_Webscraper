#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    ofstream outfile;
    ifstream infile;
    infile.open("A-small.in", ifstream::in);
    outfile.open("A-small.out", ofstream::out);
    unsigned int cantCasos;
    infile >> cantCasos;
    unsigned int caso = 1;
    while(cantCasos>0)
    {

        unsigned int cantEngines;
        infile >> cantEngines;

        /*ut << "Caso"<<endl;
        cout << "Engines:"<<cantEngines<<endl;*/

        string * engines = new string[cantEngines];

        //Small fix to set infile properly
        getline(infile,engines[0]);

        map<string,unsigned int> mapEngines; 

        for(int i=0;i<cantEngines;i++){
            getline(infile,engines[i]);
            mapEngines[engines[i]]=i+1;
        }
        
        unsigned int cantQ;
        infile >> cantQ;
        if(cantQ>0){
        string * query = new string[cantQ];
        
                
        //Small fix to set infile properly
        getline(infile,query[0]);
        for(int i=0;i<cantQ;i++){
            getline(infile,query[i]);
        }                
        
        unsigned int **cost = new unsigned int * [cantQ];
        
        for(int i=0;i<cantQ;i++){
            cost[i] = new unsigned int[cantEngines];
        }     
        
        //Inicializo valores
        unsigned int p_min;
        unsigned int min;
        
        unsigned int skip = mapEngines[query[0]];
        for(int j=0;j<cantEngines;j++){
            if(j == skip-1)
            {
               cost[0][j] = UINT_MAX;
            }
            else{
                cost[0][j] = 0;
            }
            
        }  

        p_min = 0;                  
        for(int i=1; i<cantQ; i++)
        {   
            min = UINT_MAX;            
            unsigned int skipThis = mapEngines[query[i]];
            for(int j=0;j<cantEngines;j++){
                if (j==skipThis-1){                    
                    cost[i][j] = UINT_MAX;
                }else{               
                    if(cost[i-1][j] == UINT_MAX){
                        cost[i][j] = p_min + 1;
                    }else{
                       cost[i][j] = cost[i-1][j];
                    }
                }
                if(cost[i][j]<min){
                    min = cost[i][j];
                }
            }
            p_min = min;
        }
        outfile << "Case #"<<caso<<": "<<min<<endl;              
        delete[] cost;
        delete[] query;
        }else{
            outfile << "Case #"<<caso<<": "<<0<<endl;
        }
        delete[] engines;

        caso++;
        cantCasos--;
    }
    infile.close();
    outfile.close();
    return EXIT_SUCCESS;
}
