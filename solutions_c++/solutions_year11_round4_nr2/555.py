#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <string>
using namespace std;

#define ii pair<int,int>
//#define iii pair<int,ii>

string map[501];
long long int m[501][501];
long long summ[501][501];
long long xm[501][501];
long long ym[501][501];
long long sumxm[501][501];
long long sumym[501][501];


long long getsumxm(int l,int r,int t,int b);
long long getsumym(int l,int r,int t,int b);
long long getsumm(int l,int r,int t,int b);

int main()
{
   int T;
   cin>>T;
   for(int it=0;it<T;it++){
      int ans=-1;
      int r,c,d;
      cin>>r>>c>>d;
      for(int i=0;i<r;i++){
         cin>>map[i];
      }
      for(int i=0;i<r;i++){
         for(int j=0;j<c;j++){
            m[i][j]=map[i][j]-'0'+d;
            sumxm[i][j]=j*m[i][j];
            xm[i][j]=j*m[i][j];
            ym[i][j]=i*m[i][j];
            if(i>0){
               sumxm[i][j]+=sumxm[i-1][j];
            }
            if(j>0){
               sumxm[i][j]+=sumxm[i][j-1];
            }
            if(i>0 && j>0)
               sumxm[i][j]-=sumxm[i-1][j-1];
               
            sumym[i][j]=i*m[i][j];
            if(i>0){
               sumym[i][j]+=sumym[i-1][j];
            }
            if(j>0){
               sumym[i][j]+=sumym[i][j-1];
            }
            if(i>0 && j>0)
               sumym[i][j]-=sumym[i-1][j-1]; 
               
            summ[i][j]=m[i][j];
            if(i>0){
               summ[i][j]+=summ[i-1][j];
            }
            if(j>0){
               summ[i][j]+=summ[i][j-1];
            }
            if(i>0 && j>0)
               summ[i][j]-=summ[i-1][j-1]; 
         }   
      }
 /*     
      printf("Mm:\n");
      for(int i=0;i<r;i++){
         for(int j=0;j<c;j++){
            printf("\t%d",m[i][j]);
         }
         printf("\n");
      }
      
      printf("Ms:\n");
      for(int i=0;i<r;i++){
         for(int j=0;j<c;j++){
            printf("\t%lld",summ[i][j]);
         }
         printf("\n");
      }
      
      printf("x:\n");
      for(int i=0;i<r;i++){
         for(int j=0;j<c;j++){
            printf("\t%d",xm[i][j]);
         }
         printf("\n");
      }
      
      printf("sumx:\n");
      for(int i=0;i<r;i++){
         for(int j=0;j<c;j++){
            printf("\t%lld",sumxm[i][j]);
         }
         printf("\n");
      }*/
      
      int ms=min(r,c);
      for(int k=3;k<=ms;k++){
         for(int i=0;i<=r-k;i++){
            for(int j=0;j<=c-k;j++){
               long long l=j;
               long long r=j+k-1;
               long long t=i;
               long long b=i+k-1;
               long long int sx=getsumxm(l,r,t,b)-xm[t][l]-xm[t][r]-xm[b][l]-xm[b][r];
               long long int sy=getsumym(l,r,t,b)-ym[t][l]-ym[t][r]-ym[b][l]-ym[b][r];
               long long int sm=getsumm(l,r,t,b)-m[t][l]-m[t][r]-m[b][l]-m[b][r];
               if((sm*(r+l)==2*sx) && sm*(t+b)==2*sy){
                  ans=k;
                  i=1000;
                  j=1000;
               }
             //  printf("it:%d sx:%lld sy:%lld sm:%lld l:%lld r:%lld t:%lld b:%lld i:%d j:%d k:%d\n",it,sx,sy,sm,l,r,t,b,i,j,k);
            }
         }
      }
      
      if(ans!=-1)
         printf("Case #%d: %d\n",it+1,ans);
      else
         printf("Case #%d: IMPOSSIBLE\n",it+1);
      //cout<<"Case #"<<(it+1)<<": "<<ans<<endl;
   }
   return 0;
}

long long getsumxm(int l,int r,int t,int b)
{
   long long ans=sumxm[b][r];
   if(l>0)
      ans-=sumxm[b][l-1];
   if(t>0)
      ans-=sumxm[t-1][r];
   if(t>0 && l>0)
      ans+=sumxm[t-1][l-1];
   
   return ans;
}

long long getsumym(int l,int r,int t,int b)
{
   long long ans=sumym[b][r];
   if(l>0)
      ans-=sumym[b][l-1];
   if(t>0)
      ans-=sumym[t-1][r];
   if(t>0 && l>0)
      ans+=sumym[t-1][l-1];
   
   return ans;
}

long long getsumm(int l,int r,int t,int b)
{
   long long ans=summ[b][r];
   if(l>0)
      ans-=summ[b][l-1];
   if(t>0)
      ans-=summ[t-1][r];
   if(t>0 && l>0)
      ans+=summ[t-1][l-1];
   
   return ans;
}


