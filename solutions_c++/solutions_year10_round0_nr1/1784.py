#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <conio.h>
#include <cmath>

using namespace std;

#define dv(vn) for(int ii=0;ii<vn.size();ii++) cout<<vn[i]<<" "; cout<<endl;

int main(void){
    fstream inp("A-large.in",ios::in);
    fstream out("A-large.out",ios::out);
    int T;
    inp>>T;    
    for(int i=1;i<=T;i++){
            int N;
            long long int K;
            inp>>N>>K;            
            out<<"Case #"<<i<<": ";
            if(K>0 && ((K+1) % (long long int)pow(2.0,N)) == 0)
                out<<"ON"<<endl;
            else
                out<<"OFF"<<endl;
            
    }
    getch();
    return 0;
}

