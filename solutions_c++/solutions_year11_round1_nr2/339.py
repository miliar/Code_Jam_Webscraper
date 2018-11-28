#include<stdio.h>
#include<string.h>
int n,m,t;
char sn[110][20],sm[30],a[20];
int ans,w;
int can[110];
int used[300];
int main(){
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  int ca=0;
  int i,j,k,j1,k1;
  int can1,can2;
  int ts;
  scanf("%d",&t);
  while (t--){
    ca++;
    scanf("%d%d",&n,&m);
    for (i=0;i<n;i++) scanf("\n%s",sn[i]);
    printf("Case #%d:",ca);
    for (i=0;i<m;i++){
      scanf("\n%s",sm);
      ans=0;w=-1;
      for (j=0;j<n;j++){
        int sum=0;
        memset(can,0,sizeof(can));
        memset(used,0,sizeof(used));
        for (j1=0;sn[j][j1];j1++) a[j1]='_';
        for (j1=0;j1<n;j1++)
          if (strlen(sn[j])!=strlen(sn[j1])) can[j1]=1;
        for (k=0;sm[k];k++){
          can1=0;
          for (j1=0;j1<n;j1++){
            if (can[j1]==0)
              for (k1=0;sn[j1][k1];k1++)
                if (sn[j1][k1]==sm[k]){can1=1;break;}
            if (can1) break;
          }
          if (can1==0) continue;
          can2=0;
          for (j1=0;sn[j][j1];j1++)
            if (sn[j][j1]==sm[k]) {a[j1]=sm[k];can2=1;}
          if (can2==0){
            sum++;
            for (j1=0;j1<n;j1++)
              if (can[j1]==0)
                for (k1=0;sn[j1][k1];k1++)
                  if (sn[j1][k1]==sm[k]) {can[j1]=1;break;}
          }
          else{
            used[sm[k]]=1;
            for (j1=0;j1<n;j1++)
              if (can[j1]==0){
                for (k1=0;k1<sn[j1][k1];k1++){
                  if (a[k1]!='_'&&sn[j1][k1]!=a[k1]) {can[j1]=1;break;}
                  if (a[k1]=='_'&&used[sn[j1][k1]]) {can[j1]=1;break;}
                }
              }
          }
          can1=1;
          for (j1=0;a[j1];j1++)
            if (a[j1]=='_') {can1=0;break;}
          if (can1) break;
        }
        if (sum>ans||(sum==ans&&w<0)){
          ans=sum;
          w=j;
        }
      }
      printf(" %s",sn[w]);
    }
    printf("\n");
  }
  return 0;
}    
            
