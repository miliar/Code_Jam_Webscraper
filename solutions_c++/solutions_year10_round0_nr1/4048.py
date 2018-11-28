#include <iostream>
using namespace std;

long long int GlowValue[30];

void Compute()
{
GlowValue[0]=1;
 for(int i=1;i<30;i++)
  GlowValue[i]=2*GlowValue[i-1]+1;
 
}


int Solve(long long int N,long long int k)
{
 if(N==0) return 0;
 long long int Least = GlowValue[N-1]+1 ; 

if(k==GlowValue[N-1]) return 1;
else if(k%Least==GlowValue[N-1]) return 1;

else return 0;
}


int main()
{
 Compute();
 int TC;
 long long int N,K;
 cin>>TC;
 for(int i=0;i<TC;i++)
 {
  cin>>N>>K;
  cout<<"Case #"<<i+1<<": ";
  if(Solve(N,K)) 
     cout<<"ON\n";
  else
     cout<<"OFF\n";
 }
}
