#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;


int main(){
    int cases;
    cin>>cases;
    
    
    for(int kases=1; kases<=cases; kases++){
           
            double D;
            int N, A;
            cin>>D>>N>>A;
            double Val[105][2];
            for(int i=0;i<N;i++)
                    cin>>Val[i][0]>>Val[i][1];
            double timeOfOther =0;
            if(N==2)
                    timeOfOther = ( (D - Val[0][1]) * (Val[1][0] - Val[0][0]) )/ ( Val[1][1] - Val[0][1]);
            else
                    timeOfOther = 0;
            cout<<"Case #"<<kases<<":\n";
            for(int i=0;i<A;i++){
                    double acc;
                    cin>>acc;
                    double timeOfCar = sqrt( (2*D)/acc );
                    double maxVal = max( timeOfOther, timeOfCar );
                    
                    printf("%.8lf\n", maxVal);
            }
    }
    return 0;   
}
