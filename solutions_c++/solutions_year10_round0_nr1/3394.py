#include<iostream>
using namespace std;

int N;
unsigned long long A,B;

int main()
{
 scanf("%d",  &N);
   
   unsigned long long S;
  for(int i=1;i<=N;i++){
   cin>>A>>B;
    
    S=1<<A;
     B=B+1-S;
      
      cout<<"Case #"<<i<<": ";
      
      if(B%S==0) cout<<"ON\n";
       else cout<<"OFF\n";
       }
       
return 0;
}
     
