#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define maxn 1024

int n,m;
bool flag[12];
int A[maxn],B[maxn][maxn],C[maxn][maxn];

void input(){
     scanf("%d%d",&n,&m);
     for(int i=0;i<m;i++){
         scanf("%d",&A[i]);
         for(int j=0;j<A[i];j++){
             scanf("%d%d",&B[i][j],&C[i][j]);
             B[i][j]--;
         }     
     }     
}

bool judge(){
     bool f;
     for(int i=0;i<m;i++){
         f=false;
         for(int j=0;j<A[i];j++){
             if(C[i][j]==1&&flag[B[i][j]]==true)f=true;
             if(C[i][j]==0&&flag[B[i][j]]==false)f=true;
             if(f==true)break;
         }
         if(f==false)return false;
    }
    return true;
}
int main(){
    //freopen("data.in","r",stdin);   
    //freopen("data.out","w",stdout); 
    int cases;
    scanf("%d",&cases);
    for(int K=1;K<=cases;K++){
          input();
          int res=n+1;
          int ans=-1;
          for(int i=0;i<(1<<n);i++){
              memset(flag,false,sizeof(flag));
              int t=0;
              int tt=i;
              for(int j=0;j<n;j++){
                  if(tt%2==1){t++;flag[j]=true;}
                  tt=tt/2;
              } 
              if(judge()==true){
                  if(t<res){res=t;ans=i;}
              }    
          }
          printf("Case #%d:",K);
          if(ans==-1)printf(" IMPOSSIBLE");
          else {
             for(int i=0;i<n;i++){
                 printf(" %d",ans%2); 
                 ans=ans/2;
             }
          }
          printf("\n");
    }
    return 0;
}
