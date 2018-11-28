#include <iostream>

using namespace std;

int main(){
    long long    list[1000],count[1000],loopc[1000];
    bool   hash[1000];
    long long t, r, k , n ,g;
    cin >> t;
    for (int tmpi=0; tmpi!=t; tmpi++){
        
        cin >> r >> k >> n;
        for (int i=0; i!=n; i++){
            cin >> list [i];
            hash[i]=false;
            }
        long i=0;
        long long loop=0;
        long long sum=0,allsum=0;
        while (loop<r){
            
              
              if (hash[i%n]){
                 while(loop+loop-loopc[i%n]<r) {
                     loop+=loop-loopc[i%n];
                     allsum+=allsum-count[i%n];
                     }
                 hash[i%n]=false;
                 }
                 
              sum=0;
              long long tmp=i;
              hash[i%n]=true;
              loopc[i%n]=loop;
              count[i%n]=allsum;
              while ((list[i%n]+sum<=k)&&(i-tmp<n)){
                    sum+=list[i%n];
                    i++;
                    }
                 loop++;
                 allsum+=sum;           
              }
              
              cout << "Case #"<<tmpi+1<<": "<< allsum <<endl;
        
        }
    
    return 0;
    
    
}
