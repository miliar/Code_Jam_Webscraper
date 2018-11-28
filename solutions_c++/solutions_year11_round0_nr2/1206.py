#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
using namespace std;

int main(){
    int T,C,D,N,now = 0;
    string Cform[40],Doop[40];
    char Ans[111];
    
    ofstream outfile("1.out");
    
    cin >> T;
    for (int i = 0;i < T;i++){
        
        cin >> C;
        for (int j = 0;j < C;j++){
            cin >> Cform[j];
        }
        
        cin >> D;
        for (int j = 0;j < D;j++){
            cin >> Doop[j];
        }
        cin >> N;
        now = 0;
        for (int j = 0;j < N;j++){
            cin >> Ans[now];
            now++;
            int k = 0;
            int bb = 0;
            
            if ( now <2 ) continue;
            
            if ( C == 0 ) {
                        for (int l = 0; l < D ; l++){
                for ( int h = 0;h<now;h++){
                    bool Dflag = false;
                    if (Ans[h] == Doop[l][0])
                       for (int hh = 0;hh<now;hh++)
                           if (Ans[hh] == Doop[l][1]){
                              Dflag = true;
                              now = 0;
                              break;
                           }
                    if (Dflag) break;
                }
            }
            continue;
            }
            
            if ((Ans[now-1] == Cform[0][0] && Ans[now-2] == Cform[0][1]) || (Ans[now-1] == Cform[0][1] && Ans[now-2] == Cform[0][0])){
               now -= 2;
               Ans[now] = Cform[0][2];
               now++;
               bb = 0;
            }
            
            k = (k+1) % C;
            

            for (int l = 0; l < D ; l++){
                for ( int h = 0;h<now;h++){
                    bool Dflag = false;
                    if (Ans[h] == Doop[l][0])
                       for (int hh = 0;hh<now;hh++)
                           if (Ans[hh] == Doop[l][1]){
                              Dflag = true;
                              now = 0;
                              break;
                           }
                    if (Dflag) break;
                }
            }
            
            while (k!=bb){
                  
                  if ((Ans[now-1] == Cform[k][0] && Ans[now-2] == Cform[k][1]) || (Ans[now-1] == Cform[k][1] && Ans[now-2] == Cform[k][0])){
                              now -= 2;
                              Ans[now] = Cform[0][3];
                              bb = k;
                  }   
                  
                  k = (k+1) % C;
                  
                  
                  for (int l = 0; l < D ; l++){
                      for ( int h = 0;h<now;h++){
                      bool Dflag = false;
                           if (Ans[h] == Doop[l][0])
                              for (int hh = 0;hh<now;hh++)
                                  if (Ans[hh] == Doop[l][1]){
                                     Dflag = true;
                                           now = 0;
                                           break;
                                  }
                      if (Dflag) break;
                      }
                  }
                  
                  if (now < 1) break;
                  
            }
        }
                 int kk;   
            outfile << "Case #" << i+1 << ": [";
            for (kk = 0;kk<now-1;kk++){
                outfile<<Ans[kk]<<", ";
            }
            if (now > 0)
            outfile << Ans[kk] << ']' <<endl;   
            else outfile <<']' <<endl;   
    }
    system("pause");
}
