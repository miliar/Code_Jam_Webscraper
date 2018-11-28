#include <iostream>
  using namespace std;
  int f[1200000],a[110][11000],bh[30],t,n,m,dx[4],dy[4];
int getf(int x){
  if(f[x]==x)return x;
  f[x]=getf(f[x]);
  return f[x];
}
main(){
  freopen("b.in","r",stdin);freopen("b.out","w",stdout);
  dx[0]=-1;dx[1]=dx[2]=0;dx[3]=1;
  dy[0]=dy[3]=0;dy[1]=-1;dy[2]=1;
  int i,j,k,x,y,ii,jj,sj,min;
  scanf("%d\n",&t);
  for(sj=1;sj<=t;sj++){
    printf("Case #%d:\n",sj);
    scanf("%d%d\n",&n,&m);    
    for(i=0;i<n;i++)
    for(j=1;j<=m;j++)scanf("%d",&a[i][j]);  
    for(i=1;i<=n*m;i++)f[i]=i;
    for(i=0;i<n;i++)
    for(j=1;j<=m;j++){
      min=1000000;
      x=i*m+j;
      for(k=0;k<4;k++){
        ii=i+dx[k];jj=j+dy[k];
        if(ii>=0 && jj>0 && ii<n && jj<=m && min>a[ii][jj]){min=a[ii][jj];y=ii*m+jj;};
        };
      if(min<a[i][j]){
        x=getf(x);y=getf(y);
        if(x<y)f[y]=x;else f[x]=y;
        };
      };
    x=-1;
    for(i=1;i<=n*m;i++)if(getf(i)==i)bh[i]=++x;
    for(i=0;i<n;i++){
      for(j=1;j<m;j++){
        x=i*m+j;
        x=getf(x);
        x=bh[x];
        printf("%c ",x+'a');
        };
      x=i*m+m;
      x=getf(x);
      x=bh[x];
      printf("%c\n",x+'a');
      };
      };
}
      
  
  
  
