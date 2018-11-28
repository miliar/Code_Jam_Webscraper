#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

//#define S scanf
int main(){
    int T,N,K;
    long long h;
    ifstream in("input.in");
    ofstream out("output.out");
    //scanf("%d",&T);
    
    in>>T;
    int c=1;
    while(T--){ 
              in>>N>>K;
              h=1<<N;
              if(K%h==h-1)
              out<<"Case #"<<c++<<": ON"<<endl;
              // out("Case #%d : ON\n",c++);
               else
               out<<"Case #"<<c++<<": OFF"<<endl;
               //printf("Case #%d : OFF\n",c++);
               }
               
                  return 0;
               }

