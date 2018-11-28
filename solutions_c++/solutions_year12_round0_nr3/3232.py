#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;

class Solver {
  public:
    long long solve (long long a, long long b) {
        long long count=0;
        stringstream ossN;
        stringstream ossM;
        stringstream ossT;
        for(long long i=a;i<=b;i++){
            ossN.str("");
            ossN << i;
            string sN = ossN.str();
            for(long long j=i+1;j<=b;j++){
                ossM.str("");
                ossM << j;
                string sM = ossM.str();
                bool achou=false;
                for(long k=1;k<sN.size() && !achou;k++){
                    size_t found;
                    if((found=sM.find(sN.substr(0,k)))!=string::npos){
                        ossT.str("");
                        ossT << sN.substr(k,sN.size()) <<sN.substr(0,k);
                        if(ossT.str()==sM){
                            count++;
                            achou=true;
                        }
                    }
                }
                
            }
        }
        return count;
    }
};

int main(int argc,char *argv[]){
	FILE *in = fopen(argv[1],"r");
	stdin = in;
    long qnt;
    scanf("%ld",&qnt);
    for(long i=1;i<=qnt;i++){
        long long a,b;
        scanf("%lld %lld",&a,&b);
        Solver solver;
        long long res = solver.solve(a,b);
        printf("Case #%ld: %lld\n",i,res);
    }
    return 0;
}
