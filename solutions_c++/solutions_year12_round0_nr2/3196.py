#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <cmath>
using namespace std;

bool compare(long long a,long long b){
    return a<b;
}

class Solver {
  public:
    long long solve (long long N, long long S, long long p, vector<long long> scores) {
        long long count=0;
        sort(scores.begin(),scores.end(),compare);
        for(long long i=0;i<scores.size();i++){
            //cout << scores.at(i)<<endl;
            if(scores.at(i)<p)continue;
            long long max = floor((scores.at(i)+4)/3.0);
            if(max>=p && S>0){
                count++;
                S--;
            }else{
                max = floor((scores.at(i)+2)/3.0);
                if(max>=p || scores.at(i)==1 && p<=1)
                    count++;
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
        long long N,S,p;
        vector<long long> scores;
        scanf("%lld %lld %lld",&N,&S,&p);
        for(long long j=0;j<N;j++){
            long long sc;
            scanf("%lld",&sc);
            scores.push_back(sc);
        }
        Solver solver;
        long long res = solver.solve(N,S,p,scores);
        printf("Case #%ld: %lld\n",i,res);
    }
    return 0;
}
