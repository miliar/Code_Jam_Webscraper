#include <iostream>

using namespace std;

main(){
       int T, N, K, bin , num=0;
       cin>>T;
       while (T--){
             bin=1;
             num ++;
             cin>>N>>K;
             for (int i=0; i<N;i++){
                 bin=bin*2;
             }
             K++;
             if (K%bin==0) cout<< "Case #" << num << ": ON"<<endl;
             else cout<< "Case #" << num << ": OFF"<<endl;
       }
             
             
       
}
