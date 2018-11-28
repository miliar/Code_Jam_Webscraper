# include <iostream>
# include <cstdio>
# include <algorithm>
# include <vector>
# include <fstream>
# include <map>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large-output");
    
    int T, cas = 0;
    in>>T;
    
    while (T--) { 
               int N;
               in>>N;
               
               map<string, int> r;
               r["O"] = 1;
               r["B"] = 1;
               string pr = "";
               map<string, int> pb;
               pb["O"]=1;
               pb["B"]=1;
               int pt = 0;

               int time = 0;               
               int totalTime = 0;
               
               while (N--) {
                          
                          int P;
                          string R;
                          in>>R>>P;
                          
                          if (R != pr) {
                                  if (pb[R] - P >= 0) {
                                        if(r[R] - time > P){ 
                                         r[R] -= time;
                                         }
                                         else{
                                              r[R] = P;
                                              }
                                  }
                                  else if (P - pb[R] >= 0) {
                                       if(r[R] + time < P){
                                        r[R] += time;
                                       }
                                       else {
                                            r[R] = P;
                                            }
                                  }    
                                       time = 0;
                               }
                     
                               pt = 0;
                               if (P < r[R]) {
                                     pt += (r[R] - P);                           
                                     }
                               else {
                                     pt += (P - r[R]);                                     
                                    }
                                    
                                    r[R] = P;
                                    
                                    pt += 1;    //push the button
                                    time += pt;
                                    totalTime += pt;      
                                    
                                    pr = R;
                                    pb[R] = P;                              
                          }
                          out << "Case #" << ++cas << ": " << totalTime << endl;                                        
               }
 
 return 0;   
}
