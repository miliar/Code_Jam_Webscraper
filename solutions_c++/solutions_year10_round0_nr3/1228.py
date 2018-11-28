#include<iostream>
using namespace std;
int main(){
unsigned long totcases,R,k,N,cur=0;
cin>>totcases;
while(totcases--)
{
cin>>R;
cin>>k;
cin>>N;
unsigned long g[N];
for(unsigned long itr=0;itr<N;itr++)
{
cin>>g[itr];
}
unsigned long long toteuro=0;
unsigned long itr=0;
while(R--)
{unsigned long ctr=0,curr=0;
for(;ctr<N;itr=(++itr)%N)
{
if(curr+g[itr]<=k) {curr+=g[itr];toteuro+=g[itr];}else break;
ctr++;
}
}
cout<<"Case #"<<++cur<<": "<<toteuro<<endl;
}
return 0;
}