#include<iostream>
#include<cmath>
#include<map>
using namespace std;

int execute(int kase){
     int A,B;
     cin>>A>>B;

     int temp=A,c=0;
     while(temp){
                temp/=10;
                c++;
     }     
     
     int power=c;
     
     c=0;
     for(int i=A;i<=B;i++){
             
             int num=i;
             map<int, bool> M;    
             for(int j=1;j<power;j++){
                     int val1=pow( (double)10.0,j);
                     int val2=pow( (double)10.0,power-j);
                     
                     int add1= num/val1;
                     int add2= (num%val1)*val2;
                     
                     int add = add1+add2;
                     
                     if(add>num && add<=B){
                                if( M.find(add)==M.end()){
                           //       cout<<num<<" "<<add<<endl;
                                  c++;
                                  M[add]=true;
                                }
                     }
             }
     }
     
     cout<<"Case #"<<kase<<": "<<c<<endl;  
     return 0;
}




int main(){
    int cases;
    cin>>cases;
    for(int kases=1;kases<=cases;kases++){
            execute(kases);
    }        
    return 0;   
}
