#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;




int main(){
    
    ifstream sisf("C.in");
    ofstream valf("C.out");
    
    int T;
    sisf >> T;
    
    for(int t = 1; t<=T; t++){
       int N;
       int sum=0, min=int(1e100), cur=0, tem;
       sisf >> N;
       for(int i = 0; i<N; i++){
          sisf >> tem;
          if(tem < min)min=tem;
          sum+=tem;
          cur = cur ^ tem;
       }
       valf << "Case #" << t << ": ";
       if(cur!=0)valf << "NO\n";
       else valf << sum-min << endl;
          
       
    }
    /*cout << cor(22021) << endl;
    system("PAUSE");*/
    
    /*for(int i = 1; i<=1000000; i++)
       valf << dec2bin(i) << endl;*/
    
    
    
    
    return 0;
}
