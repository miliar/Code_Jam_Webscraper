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
#include<set>

using namespace std;

void solveLine(int N, int S, int P, int t[], int numSol);

typedef vector<int> Vect;
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
    myfile.open ("/home/benoit/Desktop/codeJam/dancer/input", ios::in );
    
    
    int T;
    myfile>>T;
    cout<<T<<endl;
    
    //Si 1ere ligne vide
    string lineStr;
    getline (myfile,lineStr);
    
    //traite chaque ligne
    for(int numSol=0; numSol<T;numSol++)
    {
        int N;
        int S;
        int P;
        myfile>>N;
        myfile>>S;
        myfile>>P;
        
        int* total = new int[N];
        for(int i=0; i<N; i++){
            myfile>>total[i];
        }
        
        solveLine(N,S,P,total, numSol+1);
    }
    return 0;
}

int maxWinner  = 0;
bool winnerDone = false;

int countWinners(int N,int P, vector<Vect> cases){
    int count = 0;
    winnerDone = true;
    
    for(int i=0; i<N; i++){
        cout << "("<<cases.at(i).at(0)<<","<<cases.at(i).at(1)<<","<<cases.at(i).at(2) << ") : ";
        if(cases.at(i).at(2) >= P || cases.at(i).at(1) >= P){
            count++;
        }
    }
    
    cout<<endl;
    return count;
}

void setSurprisingAt(set<int> chosen, int N, int S, int P, vector<Vect> cases){
    if(S==0){
       maxWinner = max(maxWinner, countWinners(N,P,cases));
       return;
    }
            
   for(int i=0; i<N; i++){
       if(chosen.find(i) == chosen.end()){
           if(cases.at(i).at(2) ==10 || cases.at(i).at(1) == 0){
              continue; 
           }
           
           bool difference = false;
           if( cases.at(i).at(2) != cases.at(i).at(1)){
               difference = true;
               cases.at(i).at(1)++;
               cases.at(i).at(2)--;
           } else{
                cases.at(i).at(2)++;
                cases.at(i).at(1)--;
           }
                chosen.insert(i);
                S--;
                
                setSurprisingAt(chosen, N, S, P, cases);
                
                chosen.erase(i);
                S++;
                if(difference){
                    cases.at(i).at(2)++;
                    cases.at(i).at(1)--;
                } else{
                cases.at(i).at(2)--;
                cases.at(i).at(1)++;
                }
       }
   }
}

void solveLine(int N, int S, int P, int t[], int numSol)
{
    maxWinner = 0;
    winnerDone = false;
    vector<Vect> base = *new vector<Vect>(); 
    
    //Create Base Case without Surprising
    for(int i=0; i<N; i++){
        int value = floor(t[i]/3);
        int delta = t[i] - value*3;

        Vect data = *new Vect();
        data.push_back(value);
        data.push_back(value);
        data.push_back(value);
        
        if(delta == 1){
            data[2] = value+1;
        }else if(delta == 2){
            data[1] = value+1;
            data[2] = value+1;
        }
        
        base.push_back(data);
        cout <<"("<< t[i] <<": "<< base[i][0]<<" "<< base[i][1]<<" "<< base[i][2] << ") ";
    }
    cout<<endl;
    
    //Add Surprising to all possibles cases
    setSurprisingAt(*new set<int>(), N, S, P, base);
    if(!winnerDone){
        maxWinner = max(maxWinner, countWinners(N,P,base));
    }
    cout << "Solution with max: "<< P<<":" << maxWinner<< "For S="<<S<<endl;
    
    //Write answer
    ofstream outfile;
    outfile.open ("/home/benoit/Desktop/codeJam/dancer/output", ios::out | ios::app);
    outfile<<"Case #"<<numSol<<": "<<maxWinner<<endl;
    outfile.close();
}



