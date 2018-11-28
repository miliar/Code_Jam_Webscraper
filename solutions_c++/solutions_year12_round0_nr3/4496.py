#include<iostream>
using namespace std;
int main()
{
 int T,A,B,temp;
 int times;
 int mod[10];
 int ten=1;
 int count=0;
 cin>>T;
 for(int k=0;k<T;k++)
 {
   cin>>A>>B;
   times=0;
   temp=A;
   ten = 1;
   while((temp=temp/10)&&++times&&(ten=ten*10));
   for(int i=0;i<=9;i++)
    mod[i]=i*(ten);
    count=0;
   for(int i=A;i<=B;i++)
   {
      temp = i;
      for(int j=0;j<times;j++)
      {
         temp = temp / 10 + mod[temp%10];
         if(temp < A || temp >B || temp==i)
            continue;
         count++;
      }
   }
   cout<<"Case #"<<(k+1)<<": "<<count/2<<endl;
 }
}
