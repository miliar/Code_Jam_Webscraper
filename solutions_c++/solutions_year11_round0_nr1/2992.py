#include<iostream>
#include<fstream>
#include<vector>
#include<stdlib.h>
#include<sstream>
#include<string>
#include<iterator>

//#define ONLINE
using namespace std;
int findNextPointer(int *curP,vector<string> tokens,string robot){
    int nextP=0;
    for(int i=*curP;i<tokens.size();i++){
        if(tokens[i]==robot){
            nextP=atoi(tokens[i+1].c_str());
            *curP=i+2;
            break;
        }
    }
    return nextP;
}
int main(){
    #ifndef ONLINE
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out","wt",stdout);
    #endif
    string line;
    int nCase=0;
    getline(cin,line);
    nCase=atoi(line.c_str());
    for(int i=0;i<nCase;i++){
        getline(cin,line);
        istringstream iss(line);
        vector<string> tokens;
        copy(istream_iterator<string>(iss),
             istream_iterator<string>(),
             back_inserter<vector<string> >(tokens));
        int curPS=1, curPO=0, curPB=0;
        int curO=1,curB=1;
        int nextO=1,nextB=1;
        int sec=0;
        nextO = findNextPointer(&curPO,tokens,"O");
        nextB = findNextPointer(&curPB,tokens,"B");
        while(curPS<tokens.size()){
            sec++;
            bool moveSequence=false;
            if(curO<nextO) curO++;
            else if(curO>nextO) curO--;
            else{
                if(tokens[curPS]=="O") {
                    nextO=findNextPointer(&curPO,tokens,"O");
                    moveSequence=true;
                }
            }
            if(curB<nextB) curB++;
            else if(curB>nextB) curB--;
            else{
                if(tokens[curPS]=="B"){
                    nextB=findNextPointer(&curPB,tokens,"B");
                    moveSequence=true;
                }
            }
            if(moveSequence) curPS+=2;
        }
        cout<<"Case #"<<i+1<<": "<<sec<<endl;
    }
    return 0;
}

