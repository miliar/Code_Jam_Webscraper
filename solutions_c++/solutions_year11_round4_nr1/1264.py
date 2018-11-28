#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main(){
    
    ifstream sisf("A-large.in");
    //ofstream valf("A.out");
    FILE * val;
    val = fopen("A-large.out", "w");
    
    int T;
    sisf >> T;
    
    for(int j = 1; j<=T; j++){
       double X, S, R, N;
       double t;
       sisf >> X >> S >> R >> t >> N;
       
       
       double way[110]; //[speed]=distance;
       double vastus = 0;
       
       for(int i = 0; i<=105; i++)way[i]=0;
       
       way[0]=X;
       
       for(int i = 1; i<= N; i++){
          int B, E, W;
          sisf >> B >> E >> W;
          way[W]+=E-B;
          way[0]-=E-B;
       }
       
       for(int i = 0; i<=105; i++){
          if(way[i]/(i+R) > t && t!=0){
             way[i]=way[i]-double(((i+R)*t));
             vastus+=t;
             t=0;
             i--;  
          }
          else if(t==0){
             vastus+=way[i]/(i+S);
          }
          else{
             vastus += way[i]/(i+R);
             t-= way[i]/(i+R);
          }

       }
       
       
       
       //valf << setprecision(std::numeric_limits<double>::digits10 + 1) << "Case #" << j << ": "<< vastus << endl;
       fprintf(val, "Case #%d: %f\n", j, vastus);
    }
    
    
    

    return 0;
}
