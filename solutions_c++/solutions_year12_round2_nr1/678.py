#include<iostream>
#include<stdio.h>
using namespace std;


int main(){
    int cases;
    cin>>cases;
    for(int kases=1; kases<=cases; kases++){
        int N,score[1000];
        cin>>N;
        int sum=0;
        for(int i=0;i<N;i++){
                cin>>score[i];
                sum+=score[i];
        }
        
        cout<<"Case #"<<kases<<":";
        
        for(int i=0;i<N;i++){
          double start=0;
          double end=1;
          double mid=0;
          while(end-start>0.0000000001){
                mid = start + (end-start)/2;
                
                double testVal = score[i]+mid*sum;
                double otherValue=0;
                for(int j=0;j<N;j++){
                        if(j==i)
                           continue;
                        double myVal = max( (testVal-score[j])/ sum, 0.0);
                     //   cout<<myVal<<" "<<endl;
                        otherValue+= myVal;
                }
                 if(otherValue < 1-mid)
                     start=mid;
                 else 
                     end=mid;                 
                                     
          }
          double ans = mid*100;
          printf(" %.8lf",ans);       
          //cout<<" "<<ans;
        }
        cout<<endl;
    }
    return 0;   
}
