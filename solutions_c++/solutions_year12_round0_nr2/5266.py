#include<iostream>
using namespace std;
main()
{
 int t;
 cin>>t;
 for(int l=1;l<=t;l++)
 {
  int a,n,s,p,sur=0,count=0;
  cin>>n>>s>>p;
  for(int i=0;i<n;i++)
  {
   cin>>a;
   int x = a/3;
   if(x<p)
   x=p;
   a=a-x;
   if(a<0)
   continue;
   a=a/2;
   if((a==x)||(a==x-1)||(a-1==x))
   count++;
   else if((a==x-2)||(a-2==x))
   sur++;
  }
  if(s>sur)
  count+=sur;
  else
  count+=s;
  cout<<"Case #"<<l<<": "<<count<<endl;
 }
 return 0;
} 
