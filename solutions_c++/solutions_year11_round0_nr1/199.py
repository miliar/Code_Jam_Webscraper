#include<stdio.h>
using namespace std;
int T,n;
int last1[101],last2[101],opt[101];
int temp1,temp2,temp,ans=0;
int now1,now2,p1,p2;
char re;
int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int i,j,k,p;
  scanf("%d",&T);
  for(k=1;k<=T;k++){
    ans=0,temp=0,temp1=0,temp2=0,now1=1,now2=1,p1=1,p2=1;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
      scanf(" %c %d",&re,&p);
      if(re=='O'){
         opt[++temp]=2;
         last2[++temp2]=p;}
      else{
        opt[++temp]=1;
        last1[++temp1]=p;}
    }
    for(i=1;i<=temp;i++){
      if(opt[i]==1){
        while(p1!=last1[now1]){
          if(p1<last1[now1]) p1++;
          if(p1>last1[now1]) p1--;
          if(p2<last2[now2]) p2++;
          if(p2>last2[now2]) p2--;
          ans++;}
        if(p2<last2[now2]) p2++;
        if(p2>last2[now2]) p2--;
        now1++,ans++;}
      else{
        while(p2!=last2[now2]){
          if(p1<last1[now1]) p1++;
          if(p1>last1[now1]) p1--;
          if(p2<last2[now2]) p2++;
          if(p2>last2[now2]) p2--;
          ans++;}
        if(p1<last1[now1]) p1++;
        if(p1>last1[now1]) p1--;
        now2++,ans++;}
    }
    printf("Case #%d: %d\n",k,ans);
  }
  scanf("%d",&n);
  return 0;
}
