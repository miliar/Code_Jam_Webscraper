#include <iostream>
#include <fstream>

using namespace std;

int main(){
    
    ifstream sisf("A.in");
    ofstream valf("A.out");
    
    
    int T;
    
    sisf >> T;
    
    for(int t = 1; t<=T; t++){
        long long int N, D, G, V=1;
        sisf >> N >> D >> G;
        for(long long int i = 1; i <=N; i++){
            if((i*D)%100==0)break;
            if(i==N)V=0;
        }
        if(G==0&&D!=0)V=0;
        if(G==100&&D!=100)V=0;
        
        valf << "Case #" << t << ": ";
        if(V==1)valf << "Possible\n";
        else valf << "Broken\n";
        
        
        
    }
    
  
    
    
    return 0;
}
