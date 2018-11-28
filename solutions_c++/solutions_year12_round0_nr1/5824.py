/* 
 * File:   main.cpp
 * Author: benoit
 *
 * Created on April 14, 2012, 2:26 PM
 */

#include <cstdlib>
#include <stdlib.h>
#include<iostream>
#include<fstream>
#include<string>

#include<math.h>
#include<assert.h>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

void solveLine(string line, int numSol);

typedef vector <int> Vect; 
typedef map<int,string> IntStr;
typedef pair<int,string> PairIntStr;
typedef map<string,int> StrInt;
typedef pair<string,int> PairStrInt;
typedef map<int,double> MapDouble;
typedef pair<int,double> PairIntDouble;

/*
 * 
 */
int main(int argc, char** argv) {
    
    ifstream myfile;
    myfile.open ("/home/benoit/Desktop/codeJam/googlereses/inputprod", ios::in );
    
    
    int N;
    myfile>>N;
    cout<<N;
    
    //Si 1ere ligne vide
    string lineStr;
    getline (myfile,lineStr);
    
    //traite chaque ligne
    for(int numSol=0; numSol<N;numSol++)
    {
        getline (myfile,lineStr);
        solveLine(lineStr, numSol+1);
    }
    return 0;
}


char google[] = { ' ', 'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char english[] = {' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

void solveLine(string line, int numSol)
{
    char* lineChar = new char[line.size()+1];
    lineChar[line.size()] = 0;
    string out = "";
    //cout << line << endl;
    
    for(int i=0; i<line.size();i++)
    {        
        for(int j=0; j<sizeof(english);j++)
        {
            if(line[i] == google[j]){
                //out = out + english[j];
                lineChar[i] = english[j];
                continue;
            }
        }  
    }
    cout<<endl<<lineChar<<endl;
    
    ofstream outfile;
    outfile.open ("/home/benoit/Desktop/codeJam/googlereses/output.txt", ios::out | ios::app);
    outfile<<"Case #"<<numSol<<": "<<lineChar<<endl;
    outfile.close();
}


