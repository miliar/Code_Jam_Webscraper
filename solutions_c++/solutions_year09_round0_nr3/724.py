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

int cur[19];
char pos[19];


int main() {
  string u;
  int N;
  cin >> N;
  getline(cin,u);
  string tt = "welcome to code jam"; 
  FOR(i,19)
    pos[i] = tt[i];
    
  FOR(cas,N){
             FOR(i,19) cur[i]=0;
             getline(cin,u);
             
             FOR(i,u.size())
                            {
                            char p = u[i];
                            for(int j = 18; j>0;j--)
                              if (p==pos[j])
                                {
                                  cur[j] = (cur[j-1] + cur[j])%10000;          
                                }
                              if (p==pos[0])
                                 cur[0]++;                  
                            }           
             

             cout<<"Case #"<<cas+1<<": ";
             int r = cur[18];
             if(r<1000) cout<<"0";
             if(r<100) cout<<"0";
             if(r<10) cout<<"0";
             cout<<cur[18]<<endl;
             
             }


return 0;
}
