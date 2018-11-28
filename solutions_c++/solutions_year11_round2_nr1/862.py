#include<stdio.h>
#include<cstring>
using namespace std;
int T,n,p;
char map[101][101];
int val[101][101];
int wi[101],los[101];
double wp[101];
double owp[101];
double oowp[101];
double cal;
int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int i,j,k,tot;
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d",&n);
    memset(val,0,sizeof(val));
    memset(wi,0,sizeof(wi));
    memset(los,0,sizeof(los));
    for(i=1;i<=n;i++){
      scanf("\n");
      for(j=1;j<=n;j++)
        scanf("%c",&map[i][j]);
    }
    for(i=1;i<=n;i++){
      for(j=1;j<=n;j++){
        if(map[i][j]=='1')
          wi[i]++;
        if(map[i][j]=='0')
          los[i]++;
      }
      wp[i]=(double)wi[i]/(double)(wi[i]+los[i]);
    }
    for(i=1;i<=n;i++){
      cal=0.0,tot=0;
      for(j=1;j<=n;j++)
        if(map[i][j]!='.'){
          tot++;
          if(map[i][j]=='1')
            cal+=(double)(wi[j])/(double)(wi[j]+los[j]-1);
          if(map[i][j]=='0')
            cal+=(double)(wi[j]-1)/(double)(wi[j]+los[j]-1);
        }
      owp[i]=cal/(double)tot*1.0;
    }
    for(i=1;i<=n;i++){
      cal=0.0,tot=0;
      for(j=1;j<=n;j++)
        if(map[i][j]!='.')
          cal+=owp[j],tot++;
      oowp[i]=cal/(double)tot*1.0;
    }
    printf("Case #%d:\n",p);
    for(i=1;i<=n;i++){
      cal=wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25;
      printf("%.12lf\n",cal);
    }
  }
  scanf("%d",&n);
  return 0;
}
    
