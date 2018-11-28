#include<iostream>
#include<string>
#include<math.h>
using namespace std;


long long int minSecond(string );
int main()
{
string s;
int t;
//cout<<"enter the string";
cin>>t;

for(int i=0;i<t;i++)
{
cin>>s;
cout<<"Case #"<<i+1<<": "<<minSecond(s)<<"\n";
}
return 0;
}



long long int minSecond(string s)
{
 int now=0;
  int len=s.length();
  int hold[len];
  hold[0]=1;
  int lim=0,j,k; 
 //lexicographically assign
  for(int i=1;i<len;i++) 
  {
   for(j=0;j<=lim;j++)
   {
     if(s[i]==s[j])
     break;
      
   }    

    if(j>lim)
    {
       if(now==1)
       now++;
       hold[i]=now++;
 
    }   
   else
   hold[i]=hold[j];
  lim++;
 
  } 
int max=hold[0];
for(int i=1;i<len;i++)
if(max<hold[i])
max=hold[i];

max++;
long long int num=0;
//form the number
for(int i=len-1,k=0;i>=0;i--,k++)
{
   num+=hold[i]*pow(max,k);
 
}
return num;
}


