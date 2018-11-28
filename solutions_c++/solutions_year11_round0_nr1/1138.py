#include<stdio.h>
using namespace std;
int T,n;
int wc1[101],wc2[101],opt[101];
int lc1,lc2,lc,ans=0;
int now1,now2,p1,p2;
char re;
int main()
{
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int i,j,k,p;
  scanf("%d",&T);
  for(k=1;k<=T;k++){
    ans=0,lc=0,lc1=0,lc2=0,now1=1,now2=1,p1=1,p2=1;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
      scanf(" %c %d",&re,&p);
      if(re=='O'){
         opt[++lc]=2;
         wc2[++lc2]=p;}
      else{
        opt[++lc]=1;
        wc1[++lc1]=p;}
    }
    for(i=1;i<=lc;i++){
      if(opt[i]==1){
        while(p1!=wc1[now1]){
          if(p1<wc1[now1]) p1++;
          if(p1>wc1[now1]) p1--;
          if(p2<wc2[now2]) p2++;
          if(p2>wc2[now2]) p2--;
          ans++;}
        if(p2<wc2[now2]) p2++;
        if(p2>wc2[now2]) p2--;
        now1++,ans++;}
      else{
        while(p2!=wc2[now2]){
          if(p1<wc1[now1]) p1++;
          if(p1>wc1[now1]) p1--;
          if(p2<wc2[now2]) p2++;
          if(p2>wc2[now2]) p2--;
          ans++;}
        if(p1<wc1[now1]) p1++;
        if(p1>wc1[now1]) p1--;
        now2++,ans++;}
    }
    printf("Case #%d: %d\n",k,ans);
  }
  scanf("%d",&n);
  return 0;
}
