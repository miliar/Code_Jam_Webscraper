#include <iostream>
  using namespace std;
  int a[110],f[110][110],n,m,t;
int dp(int x,int y){
  if(f[x][y]>=0)return f[x][y];
  if(x>=y-1)return 0;
  f[x][y]=100000000;
  int i,k;
  for(i=x+1;i<y;i++){
    k=dp(x,i)+dp(i,y)+(a[y]-a[x]-2);
    if(k<f[x][y])f[x][y]=k;
    };
  return f[x][y];
}
main(){
  freopen("c.in","r",stdin);freopen("c.out","w",stdout);
  scanf("%d\n",&t);
  int i,j,k,x,sj;
  for(sj=1;sj<=t;sj++){
    printf("Case #%d: ",sj);
    scanf("%d%d\n",&n,&m);
    memset(f,255,sizeof(f));
    for(i=1;i<=m;i++)scanf("%d\n",&a[i]);
    for(i=1;i<m;i++)
    for(j=i+1;j<=m;j++)if(a[i]>a[j]){
      k=a[i];a[i]=a[j];a[j]=k;
      };
    a[0]=0;a[m+1]=n+1;
    x=dp(0,m+1);
    cout<<x<<endl;
    }
}
    
