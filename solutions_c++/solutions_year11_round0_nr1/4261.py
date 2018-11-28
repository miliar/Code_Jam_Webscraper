#include<stdio.h>
#include<stdlib.h>
int ans;
int w,n;
char c;
int t;
int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int ca=0;
  int w1,w2,t1,t2;
  int i;
  scanf("%d",&t);
  while (t--){
    ca++;
    scanf("%d",&n);
    w1=1;w2=1;
    t1=0;t2=0;
    ans=0;
    for (i=0;i<n;i++){
      scanf(" %c %d",&c,&w);
      if (c=='O'){
        int temp=abs(w-w1);
        if (t1<temp) {ans+=temp-t1;t2+=temp-t1+1;}
        else t2+=1;
        ans++;
        t1=0;
        w1=w;
      }
      else{
        int temp=abs(w-w2);
        if (t2<temp) {ans+=temp-t2;t1+=temp-t2+1;}
        else t1+=1;
        ans++;
        t2=0;
        w2=w;
      }
    }
    printf("Case #%d: %d\n",ca,ans);
  }
  return 0;
}
