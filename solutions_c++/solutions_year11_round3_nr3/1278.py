# include <iostream>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <cmath>
# include <fstream>

using namespace std;

ifstream in("C-small-attempt0.in");
ofstream out("output.txt");

void solve(int f[], int N, int L, int H){
               
               for(int i = L; i<=H; ++i){
                       bool ok = true;
                       for(int j = 0; j<N; ++j){
                                 if(f[j]%i && i%f[j]){
                                           ok = false;
                                           break;
                                      }
                               }                      
                               
                               if(ok){
                                      out<<i;
                                      return;
                                    }                       
                       }              
               
               out<<"NO";
     }

int main(){
     
    int T, cas = 0;
    
    in>>T;

    while(T--){
               
               int N, L, H, f[101]={0};
               in>>N>>L>>H;
               
               for(int i = 0; i<N; ++i){
                       in>>f[i];
                       }
                                            
               out<<"Case #"<<++cas<<": ";
               solve(f, N, L, H);
               out<<endl;           
          }
 
 return 0;   
}
