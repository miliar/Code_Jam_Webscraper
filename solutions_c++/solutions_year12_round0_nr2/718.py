#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstring>
#define LOCAL
using namespace std;
int sum[102];
int max(int a,int b)
{ if(a>=b){return a;}
 else{ return b;}
}    
int main()
{
#ifdef LOCAL
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
#endif
int T;
cin>>T;
for(int tt=1;tt<=T;tt++)
{int N,S,p,cas,m;
    memset(sum,0,sizeof(sum));
    cas=0;m=0;
cin>>N>>S>>p;
   for(int i=0;i<N;i++)
   {cin>>sum[i];
     if(sum[i]>=2*max(p-1,0)+p){cas++;}
     else if(sum[i]>=2*max(p-2,0)+p){m++;}
   }

if(m>=S){cas+=S;}
else{cas+=m;}

//qsort(sum,N,sizeof(int),comp);

cout<<"Case #"<<tt<<": "<<cas<<endl;

}



return 0;
}

