#include <fstream>
#include <cstdlib>
#include <cstring>
using namespace std;



int main()
{
    fstream in, out;
    int T, N, S, p, pa;
    
    
    
    in.open("inputL.in", ios::in);
        
    out.open("output.txt", ios::out);
    
    in>>T;
    
    for(int j=0; j<T; j++){
               
               in>>N;
               in>>S;
               in>>p;
               
               int cont=0;
               
               for(int i=0; i<N; i++){
                       
                       in>>pa;
                       if(pa>=p){
                                 
                       if((pa-p)/2 >= p-1)    cont++;
                       
                       else if((pa-p)/2 >= p-2  && S>0) {
                                                     cont++;
                                                     S--;
                                                     }
                                                     }
                       
                       }
                       
               out<<"Case #"<<1+j<<": "<<cont<<endl;
               
               }
               
    in.close();   
    out.close();
    
    return 0;
    
    }
