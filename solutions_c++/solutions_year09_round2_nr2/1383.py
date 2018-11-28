#include<iostream>
using namespace std;
int main()
{
 int t;
 cin>>t;
for(int i=1;i<=t;i++)
{
 int n;
 cin>>n;
 int arr[10]={0},m=n;
 while(m>0)
 {
  arr[m%10]++;
  m/=10; 
 }
 bool check=false;
 while(check==false)
 {
  n++;check=true;
  int mem[10]={0},m=n;
  while(m>0)
  {
    mem[m%10]++;
    if(m%10!=0 && mem[m%10]>arr[m%10])
    {check=false;break;}
   m/=10;
  }
   for(int q=1;q<10;q++)
   if(arr[q]!=mem[q])
   check=false;
  
 }
  cout<<"Case #"<<i<<": "<<n<<endl;
}  
 return 0;
}
