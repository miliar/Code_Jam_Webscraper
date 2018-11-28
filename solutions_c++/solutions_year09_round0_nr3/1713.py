#include <iostream>
  using namespace std;
  int f[600][3],pre[300][3][2],a[600],t,n,link[300];
void init(){
  int i,x,j,y;
  char s[]="welcome to code jam";  
  freopen("c.in","r",stdin);freopen("c.out","w",stdout);
  scanf("%d\n",&t);
  memset(pre,255,sizeof(pre));
  memset(link,0,sizeof(link));
  link['w'-' ']=1;
  for(i=1;i<19;i++){
    x=s[i]-' ';y=s[i-1]-' ';
    pre[x][link[x]][0]=y;pre[x][link[x]][1]=link[y]-1;
    link[x]++;
    };  
}
main(){
  init();
  int sj,i,j,k,x,y;
  char ch;
  for(sj=1;sj<=t;sj++){
    memset(f,0,sizeof(f));
    printf("Case #%d: ",sj);
    n=0;
    scanf("%c",&ch);
    while(ch!='\n'){      
      a[++n]=ch-' ';
      if(ch=='w')f[n][0]=1;
      scanf("%c",&ch);
      };
    for(i=2;i<=n;i++)
    for(j=0;j<3;j++)if(pre[a[i]][j][0]>=0){
      x=pre[a[i]][j][0];y=pre[a[i]][j][1];      
      for(k=1;k<i;k++)if(a[k]==x){
        f[i][j]=(f[i][j]+f[k][y]) % 10000;        
        };
      };
    y=0;
    for(i=5;i<=n;i++)if(a[i]=='m'-' ')y=(y+f[i][1])%10000;   
    if(y<1000)printf("0");
    if(y<100)printf("0");
    if(y<10)printf("0");
    printf("%d\n",y);
    };
}
      
      
      
  
  
