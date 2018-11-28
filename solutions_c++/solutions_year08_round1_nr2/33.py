//#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


int n,m;

int black[2100];
int d[2100];
int e[2100][2100];
int f[2100],closed;
int ans[2100];

int main(){
    freopen("binput2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,k,test,cases;
    
    cases=0;
    scanf("%d",&test);
    while (test){
          test--;
          cases++;
          scanf("%d%d",&n,&m);
          
          
          
          memset(black,0,sizeof(black));
          memset(d,0,sizeof(d));
          foru(i,1,n) e[i][0]=0;
          
          int t;          
          foru(i,1,m){
             scanf("%d",&t);
             while (t){
                t--;
                scanf("%d%d",&j,&k);
                if (k==1) black[i]=j;   
                else {
                   e[j][0]++;
                   e[j][e[j][0]]=i;
                   d[i]++;
                }   
             }
          }
          memset(ans,0,sizeof(ans));
          closed=0;
          foru(i,1,m) if (d[i]==0) { closed++; f[closed]=i;}
          int open=0;
          
//          foru(i,1,closed) printf("%d ",f[i]);
  //        printf("\n");
          
          bool bt=true;
          while (open<closed){
                open++;
                i=f[open];
                j=black[i];
                if (j==0) {bt=false; break;}
                ans[j]=1;
                
                foru(k,1,e[j][0]){
                    d[e[j][k]]--;
                    if (d[e[j][k]]==0){
                         closed++;
                         f[closed]=e[j][k];                  
                    }               
                }
          }
          if (!bt) printf("Case #%d: IMPOSSIBLE\n",cases);
          else {
               printf("Case #%d:",cases);
               foru(i,1,n) printf(" %d",ans[i]);
               printf("\n");
          }
    }
    return 0;
}
