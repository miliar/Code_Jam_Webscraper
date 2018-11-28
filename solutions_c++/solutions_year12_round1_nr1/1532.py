#include <iostream>
#include "stdio.h"
#include "math.h"
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

double getProb(double a[], int N) {
    double res = 1;
    for(int i=0; i<N; i++)
       res *= a[i];
    return res; 
}

int main(void) {
    
    int T, A, B;
    cin>>T;
    for(int c = 1; c<=T; c++) {
        double probability[100002];
        cin>>A>>B;
        
        for(int i=0; i<A; i++)
            cin>>probability[i];

        double res[100004];//could be A+2 results;
        
        double pp = getProb(probability, A);
        res[0] = pp*(B-A+1)+(1-pp)*(B-A+B+2);
        res[1] = B+2;
        
        for(int i=1; i<=A; i++) {
            double pp_t = getProb(probability, A-i);
            res[i+1] = pp_t*(i+(B-A)+i+1) + (1-pp_t)*(i+(B-A)+i+1+B+1); 
        }

        double min = res[0]; 
        for(int i=1; i<A+2; i++) {
            if(min>res[i])
                min = res[i];
        }
        printf("Case #%d: %0.6f\n", c, min);       
       // cout<<"Case #"<<c<<": "<<setprecision(6)<<min<<endl;
    } 
    
    return 0;

}
