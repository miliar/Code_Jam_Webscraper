#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdlib>

using namespace std;

long long int N,K,B,T;
long long int X[51],V[51];
long long int mp[51][51];

long long int getval( long long int n,long long  int k)
{

if(k==0) {  return 0;}
if((n+1)<k) {  return -1; }


if( mp[n][k]!=-1) return mp[n][k];


double btime = double(B-X[n])/double(V[n]);
if(btime<=T)
{
mp[n][k]=getval(n-1,k-1);
return mp[n][k];
}
else
{
long long int temp=getval(n-1,k);
if(temp==-1) { mp[n][k]=temp; return temp; }
else { mp[n][k]=k+temp; return k + temp;}
}

}




int main()
{
int t;
scanf("%d",&t);

for(int count=0;count<t;count++)
{

scanf("%lld %lld %lld %lld",&N,&K,&B,&T);
memset(mp,-1,sizeof(long long int)*51*51);

for(int i=0;i<N;i++)
scanf("%lld",&X[i]);

for(int i=0;i<N;i++)
scanf("%lld",&V[i]);

long long int swap=getval(N-1,K);
if(swap==-1)
printf("Case #%d: IMPOSSIBLE\n",count+1);
else
printf("Case #%d: %d\n",count+1,swap);

}



return 0;
}
