#include<cstdio>
#include<iostream>
#include<cmath>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<sstream>
#include<vector>
#include<utility>
#include<map>
#include<cstdlib>
#include<limits.h>
#include<algorithm>
using namespace std;
int main()
{
 int t,count=0;
 FILE *fi=fopen("A.in","r"),*fp=fopen("ma.txt","w");
 fscanf(fi,"%d",&t);
 //cin>>t;
 while(t--)
 {
  int p,k,l;
  long long ans=0;
  count++;
  fscanf(fi,"%d",&p);
  fscanf(fi,"%d",&k);
  fscanf(fi,"%d",&l);
  //cin>>p>>k>>l;
  vector <int> x(l);
  for(int i=0;i<l;i++)
  {
   int temp;
   fscanf(fi,"%d",&temp);
   //cin>>temp;
   x[i]=temp;
   //fflush(stdin); 
   }
  
  sort(x.begin(),x.end());
  int limit=1;
  int s=1;
  for(int i=l-1;i>=0;i--)
  {
   ans+=x[i]*s;
   limit++;
   if(limit>k){limit=1;s++;}
//   cout<<p<<endl;
//   system("pause");
   }
  fprintf(fp,"Case #%d: %lld\n",count,ans);
  //cout<<ans<<endl;
//  cout<<p<<endl; 
  }
fclose(fp);
 return 0;
 }

