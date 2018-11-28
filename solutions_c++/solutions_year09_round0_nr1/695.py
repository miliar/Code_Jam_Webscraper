#include <sstream>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
// for do 0 ateh n, exclusive
#define FOR( i , n ) for (int i = 0; i < n ; i++ )

bool pode[16][30];
int p[5001][16];
int L,D,N;

void trab(string u){
     FOR(i,16)
      FOR(j,30)
        pode[i][j]=0;
     int cur=0;
     FOR(i,L)
              if(u[cur]!='(') {
                              pode[i][u[cur]-'a']=1;
                              cur++;                              
                              }
             else
             { 
             cur++;
             while(u[cur]!=')')
                               {
                               pode[i][u[cur]-'a']=1;
                               cur++;
                               }
             cur++;
              }
}

int main() {
  cin>>L>>D>>N;
  FOR(i,D){
    string u;  
    cin>>u;
    FOR(j,L)
      p[i][j]=u[j]-'a';
    }
  
  FOR(i,N){
    string u;
    cin>>u;
    trab(u);
    int resul=0;   
    FOR(j,D)
            {
            bool foi = true;
            FOR(l,L)
              if(!pode[l][p[j][l]]) {foi = false;break;}
            if(foi) resul++;
            }
   cout<<"Case #"<<i+1<<": "<<resul<<endl;
  }
  
  return 0;
}
