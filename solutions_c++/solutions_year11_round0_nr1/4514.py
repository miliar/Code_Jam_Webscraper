#include<iostream> 
#include<cstdio>
using namespace std;
int t1,n,ti,zr;
int p[1001],a[1001],xo[1001],xb[1001],t[1001];

void init(){
     memset(p,0,sizeof p);
     memset(a,0,sizeof a);
     memset(xo,0,sizeof xo);
     memset(xb,0,sizeof xb);
     memset(t,0,sizeof t);
}
 
int main(){
    //freopen("a.out","w",stdout); 
    scanf("%d",&t1);
    while (t1--){
          init();
          scanf("%d",&n);
          for (int i=1;i<=n;i++){
              getchar();
              
              char x=getchar();
              scanf("%d",&a[i]);
              
              if (x=='O') p[i]=1; else p[i]=2;
          }
          
          xo[0]=1;xb[0]=1;t[0]=0;
          
          for (int i=1;i<=n;i++){
              //orange
              if (p[i]==1){
                  ti=abs(xo[i-1]-a[i])+1;
                  xo[i]=a[i];
                  int i1=-1;
                  for (int j=i+1;j<=n;j++){
                      if (p[j]==2) {i1=j;break;}
                  }
                  if (i1!=-1){
                     if (xb[i-1]>a[i1]) xb[i]=max(a[i1],xb[i-1]-ti);
                     if (xb[i-1]<a[i1]) xb[i]=min(a[i1],xb[i-1]+ti);
                     if (xb[i-1]==a[i1]) xb[i]=xb[i-1];
                  }
             }
              //blue
              if (p[i]==2){
                  ti=abs(xb[i-1]-a[i])+1;
                  xb[i]=a[i];
                  int i1=-1;
                  for (int j=i+1;j<=n;j++)
                      if (p[j]==1) {i1=j;break;}
                  if (i1!=-1){
                     if (xo[i-1]>a[i1]) xo[i]=max(a[i1],xo[i-1]-ti);
                     if (xo[i-1]<a[i1]) xo[i]=min(a[i1],xo[i-1]+ti);
                     if (xo[i-1]==a[i1]) xo[i]=xo[i-1];
                  }

             }
             t[i]=t[i-1]+ti;
         }zr++;
        printf("Case #%d: %d\n",zr,t[n]);
   }
}
