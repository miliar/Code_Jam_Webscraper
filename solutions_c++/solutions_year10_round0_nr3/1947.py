#include<stdio.h>
#include<iostream>
#include<queue>
#include<stdlib.h>
#include<cstring>
#include<time.h>
using namespace std;
long long r,n,k;
long long m[2048];
long long s[2048];
long long pos(long long f,long long l)
{
  long long ff = f;
  long long ll = l;
  while(ff <= ll)
    {
     long long mid = (ff+ll)/2;
     if(s[mid] - s[f] + m[f] > k)
       ll = mid-1;
     else if(s[mid] - s[f] + m[f] == k)
            return mid;
     else if(s[mid] - s[f] + m[f] < k)
            ff = mid+1;
    }
    return ll;
}
int main()
{
 FILE *fin,*fout;
 fin = fopen("park.in","r");
 fout = fopen("park.out","w");
 int t;
 fscanf(fin,"%d",&t);
 for(int i = 0; i < t ; i++)
 {
   memset(m,0,sizeof(0));
   memset(s,0,sizeof(0));
   fscanf(fin,"%lld%lld%lld",&r,&k,&n);
   for(int j = 0; j < n; j++)
   {
     fscanf(fin,"%lld",&m[j]);
     m[j+n] = m[j];
   }
   s[0] = m[0];
   for(int j = 1; j < 2*n; j++)
     s[j] = s[j-1] + m[j];
   long long f = 0;
   long long l = n-1;
   long long res = 0;
   for(int j = 0; j < r; j++ )
   {
    int p = pos(f,l);
    //cout<<"bin "<<f<<" "<<l<<" "<<p<<endl;
    res += s[p] - s[f] + m[f];
    //cout<<"res "<<res<<endl;
    f = p+1;
    l = (f+(n-1));
   // cout<<"new"<<f<<" "<<l<<endl;
    if(f >= 2*n || l>= 2*n) { f-=n;l-=n;}
   }
   fprintf(fout,"Case #%d: %lld\n",i+1,res);
   //printf("Got case %d in %lf\n",i+1,(double)clock()/(double)CLOCKS_PER_SEC);
 }
   return 0;
}