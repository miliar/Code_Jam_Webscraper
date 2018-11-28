#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

int ctrz(int a)
{
    int trzeros=0;
     while(a%10==0){
                          trzeros++;
                          a=a/10;//a=112
           }
     return trzeros;
}
int findnumdigs(int num)
{
    int i=0;
  while(num!=0)
    {
       num=num/10;
      ++i;
      }  
      return i;
}


int shiftright(int a)
{
  int i=0,trzeros;
  int num=a;
  int b=a%10;
  if(b==0) //0 cannot be brought to front!
  {
           while(a%10==0){
                          trzeros++;
                          a=a/10;//a=112
           }
           b=a%10;
            while(num!=0)
            {
      
             num=num/10;
              ++i;
               b=b*10;
               }//b=20000
           b=b/10;
           b=b+a/10;
           return b;
  }
  while(num!=0)
    {
      
      num=num/10;
      ++i;
      b=b*10;
}
  b=b/10;  
  a=a/10;
  a=a+b;
  return a;
}

int main()
{
   int N,A,B,cnt=0,numdigs;// no of test cases
   
   cin>>N;
   for(int i=0;i<N;i++){
     cnt =0;
     cin>>A>>B;
     vector<int> v;
     //cout<<"A = "<<A<<"B= "<<B<<endl;
     
     numdigs=findnumdigs(A);
   for(int j=A;j<=B;j++){
           
           int l=j;
           v.clear();
           for(int k=0;k<numdigs;k++){
                   
                   if(ctrz(l)>0)
                   k=k+ctrz(l);
                   v.push_back(l);
                   l=shiftright(l);
                   
                   if(find(v.begin(),v.end(),l)<v.end())
                   continue;         
                   if(l>j&&l<=B){
                   cnt++;
                  // cout<<"pair ("<<j<<","<<l<<")"<<endl;
                   }     
           }
   }
   
     cout<<"Case #"<<i+1<<": "<<cnt<<endl;
   }
  
  return 0;
}
