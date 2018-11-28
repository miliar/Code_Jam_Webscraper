#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>


using namespace std;

int main()
{
    ofstream fout ("gcj2.txt.in");
    ifstream fin ("gcj2.in.in");
    
    int t;
    int p;
    
    fin >> t;
    
    for(int i=0; i<t; i++)
    {
    fin >> p;
    
    
    
    
    int power[11];
    
    power[0]=1;
    power[1]=2;
    power[2]=4;
    power[3]=8;
    power[4]=16;
    power[5]=32;
    power[6]=64;
    power[7]=128;
    power[8]=256;
    power[9]=512;
    power[10]=1024;
    
    int aux = power[p];
    int constr[aux];
        
   for(int j=0; j<aux; j++)
    fin >> constr[j];
    
    int prices[p][aux];
    
    for(int j=0; j<p; j++)
    for(int l=0; l< power[p-j-1]; l++)
    fin >> prices[j][l];
    
    int res=0;
  
    for(int j=0; j<p; j++)
    {
    for(int l=0; l < power[j]; l++)
    {
    for(int r=0; r < power[p-j]; r++)
    if(constr[r+l*power[p-j]] < p-j)
    {
    res++;
    break;
    } 
    
    
    }
    }
    
    fout << "Case #" << i+1 << ": " << res << endl;
    
    
    
    }
    
    return 0;
    
}
