// google code jam 2010 qualification round, #1
// author Zhong Wang, clock.w@gmail.com
#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

int main(){
    int T;
    long K,N;
    
    long g[31];
    g[0]=1;
    
    for(int i=1;i<=30;++i)
            g[i]=2*g[i-1];
    
    ifstream fin("A-large.in");
    fin>>T;
    
    ofstream fout;
    fout.open("A-large.out");
    
    for(int i=1;i<=T;++i)
    {fin>>N>>K;
    if(((K+1)%g[N])==0)
    fout<<"Case #"<<i<<": ON";
    else fout<<"Case #"<<i<<": OFF";
    if(i!=T) fout<<endl;        
            }
            
    fout.close();

    return 0;
    }
