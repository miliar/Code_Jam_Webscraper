#include <iostream>
#include <cstring>
  using namespace std;
  int t,link[255],a[20],n;
  long long ans;;
  char s[20];
void work(){
  int i,x;
  long long y;
  memset(link,255,sizeof(link));
  link[a[0]]=1;
  x=0;
  for(i=1;i<n;i++)if(link[a[i]]<0){
    link[a[i]]=x;
    x++;
    if(x==1)x++;
    };
  if(x==0)x=2;
  y=0;
  for(i=0;i<n;i++)y=y*(long long)x+(long long)link[a[i]];
  ans=y;
}   
    
main(){ 
  freopen("a.in","r",stdin);freopen("a.out","w",stdout);
  scanf("%d\n",&t);
  int sj;
  for(sj=1;sj<=t;sj++){
    printf("Case #%d: ",sj);
    gets(s);
    n=strlen(s);
    for(int i=0;i<n;i++)a[i]=s[i]-'0';
    work();
    cout<<ans<<endl;
    };
}
    
