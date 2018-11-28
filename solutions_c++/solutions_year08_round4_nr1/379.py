#include <iostream>
#include <algorithm>

using namespace std;

const int mmax=20005;

int nx;
int g[mmax], c[mmax];
int l[mmax];
int ans[mmax][2];
int m,v;
int i,j,k,t;
int p[mmax];

int main(){
     freopen("a.in","r",stdin);
     freopen("a.out","w",stdout);
     scanf("%i", &nx);
     for(i=0;i<nx;i++){
          scanf("%i%i", &m,&v);
          for(j=1;j<(m+1)/2;j++){
               scanf("%i%i",&g[j],&c[j]);
          }
          for(j=(m+1)/2;j<=m;j++){
               scanf("%i",&l[j]);
               ans[j][l[j]]=0;
               ans[j][abs(l[j]-1)]=-1;
               p[j]=l[j];
          }
          int prev_t=-1;
          for(j=m;j>1;j--){
               if(j%2)
                    k=j-1;
               else
                    k=j+1;
               t=j/2;
               if(t==prev_t)continue;
               prev_t=t;
               if(g[t]==1){
                    p[t]=p[j]*p[k];
                    ans[t][p[t]]=0;
               }else{
                    p[t]=max(p[j],p[k]);
                    ans[t][p[t]]=0;
               }
                    int tmp=5*mmax;
                    if(g[t]==1){
                         if(p[t]!=p[k]*abs(p[j]-1) && ans[j][abs(p[j]-1)]!=-1)
                              if(ans[j][abs(p[j]-1)]<tmp)tmp=ans[j][abs(p[j]-1)];
                    }else{
                         if(p[t]!=max(p[k],abs(p[j]-1)) && ans[j][abs(p[j]-1)]!=-1)
                              if(ans[j][abs(p[j]-1)]<tmp)tmp=ans[j][abs(p[j]-1)];
                    }
                    if(g[t]==1){
                         if(p[t]!=p[j]*abs(p[k]-1) && ans[k][abs(p[k]-1)]!=-1)
                              if(ans[k][abs(p[k]-1)]<tmp)tmp=ans[k][abs(p[k]-1)];
                    }else{
                         if(p[t]!=max(p[j],abs(p[k]-1)) && ans[k][abs(p[k]-1)]!=-1)
                              if(ans[k][abs(p[k]-1)]<tmp)tmp=ans[k][abs(p[k]-1)];
                    }
                    if(g[t]==1){
                         if(p[t]!=abs(p[k]-1)*abs(p[j]-1) && ans[j][abs(p[j]-1)]!=-1 && ans[k][abs(p[k]-1)]!=-1)
                              if(ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)]<tmp)tmp=ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)];
                    }else{
                         if(p[t]!=max(abs(p[k]-1),abs(p[j]-1)) && ans[j][abs(p[j]-1)]!=-1 && ans[k][abs(p[k]-1)]!=-1)
                              if(ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)]<tmp)tmp=ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)];
                    }
                    if(c[t]==1){
                         if(g[t]==0){
                              if(p[t]!=p[k]*p[j])
                                   tmp=1;
                         }else{
                              if(p[t]!=max(p[k],p[j]))
                                   tmp=1;
                         }
                         if(g[t]==0){
                              if(p[t]!=p[k]*abs(p[j]-1) && ans[j][abs(p[j]-1)]!=-1)
                                   if(ans[j][abs(p[j]-1)]+1<tmp)tmp=ans[j][abs(p[j]-1)]+1;
                         }else{
                              if(p[t]!=max(p[k],abs(p[j]-1)) && ans[j][abs(p[j]-1)]!=-1)
                                   if(ans[j][abs(p[j]-1)]+1<tmp)tmp=ans[j][abs(p[j]-1)]+1;
                         }
                         if(g[t]==0){
                              if(p[t]!=p[j]*abs(p[k]-1) && ans[k][abs(p[k]-1)]!=-1)
                                   if(ans[k][abs(p[k]-1)]+1<tmp)tmp=ans[k][abs(p[k]-1)]+1;
                         }else{
                              if(p[t]!=max(p[j],abs(p[k]-1)) && ans[k][abs(p[k]-1)]!=-1)
                                   if(ans[k][abs(p[k]-1)]+1<tmp)tmp=ans[k][abs(p[k]-1)]+1;
                         }
                         if(g[t]==0){
                              if(p[t]!=abs(p[k]-1)*abs(p[j]-1) && ans[j][abs(p[j]-1)]!=-1 && ans[k][abs(p[k]-1)]!=-1)
                                   if(ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)]+1<tmp)tmp=ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)]+1;
                         }else{
                              if(p[t]!=max(abs(p[k]-1),abs(p[j]-1)) && ans[j][abs(p[j]-1)]!=-1 && ans[k][abs(p[k]-1)]!=-1)
                                   if(ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)]+1<tmp)tmp=ans[j][abs(p[j]-1)]+ans[k][abs(p[k]-1)]+1;
                         }     
                    }
                    if(tmp!=5*mmax)
                         ans[t][abs(p[t]-1)]=tmp;
                    else
                         ans[t][abs(p[t]-1)]=-1;
          }
          if(ans[1][v]==-1)
               printf("Case #%i: IMPOSSIBLE\n",i+1);
          else
               printf("Case #%i: %i\n",i+1, ans[1][v]);
     }

     fclose(stdin);
     fclose(stdout);
     return 0;
}