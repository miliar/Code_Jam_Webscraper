#include<iostream> 
#include<math.h> 
using namespace std;
int poten10(int n){
    int r=1;
    for(int i=0;i<n;i++)r*=10;
    return r;
}
int nparec(int n,int b){
    int num,front,back,r=0;
    if(n<10){return 0;}
    int d;
    d=int(log10(float(n))+1);
    num=n;
    for(int i=1;i<d;i++){
       back=n%poten10(i);
       back=back*poten10(d-i);
       front=n/poten10(i);
       num=front+back;
       if((num<=b)&&(n<num)){
          r++;
       }
    }
    return r;
}
int main(){ 
   freopen("C-small-attempt0.in","r",stdin);
   freopen("c.out","w",stdout);
   int i,j,a,b,t,r;
   cin>>t;
   for(i=0;i<t;i++){
      cin>>a>>b;
      r=0;
      for(j=a;j<b;j++){
         r+=nparec(j,b);
      }
      cout<<"Case #"<<i+1<<": "<<r<<endl;
   }
   cin.get();
   //nparec(12345,99999);
}
