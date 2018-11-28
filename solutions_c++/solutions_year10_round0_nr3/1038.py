#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<cstdio>
using namespace std;

int main()
{
long long t,i;
int test = 1;
cin>>t;
while(t--)
{
long long r , k , n;
cin>>r>>k>>n;
vector<long long> a;
vector<long long> gain;
vector<long long> next;
a.resize(n);
gain.resize(n);
next.resize(n);

for(int i = 0 ; i < n ; i++)
    scanf("%lld",&a[i]);
  


for(int i = 0 ; i < n ; i++)
{
   long long tot = a[i];
   long long j = i+1;
   if( j == n )
     j-=n;
   while( tot + a[j] <= k && j!= i)
   {
      tot+=a[j];
      j++;
      if( j == n )
	  j-=n;
   }
   gain[i] = tot;
   next[i] = j;
  
}


long long total = 0;
long long start = 0;
for(int j = 1 ; j <= r ; j++)
{
    total += gain[start];
    start = next[start];
}  
  
cout<<"Case #"<<test<<": "<<total<<endl; 
test++;  
}  
return 0;  
}