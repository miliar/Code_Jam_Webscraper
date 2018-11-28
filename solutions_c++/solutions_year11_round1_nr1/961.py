#include <iostream>
using namespace std;
int main(){
    int ntc,g,d;
    long long limit;
    cin >>ntc;
    for(int tc=1;tc<=ntc;tc++){
            int no=0;


            cin >> limit >> d>>g;
            if( (d < 100  && g==100) || ( d>0 && g==0))
                    no=1;
            int pd=100;
            for(int i=2;i<=10;i++){
               while(d % i ==0 && pd % i ==0){ d/=i;pd/=i;}        
            }
            if(pd>limit ||  no){
                   printf("Case #%d: Broken\n",tc);
            }
            else{
                   printf("Case #%d: Possible\n",tc);
                   
            }
    } 
} 
