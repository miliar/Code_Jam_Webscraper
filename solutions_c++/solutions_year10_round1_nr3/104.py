#include<cstdio>
int a[1000001],b[1000001];
inline int cnt(int r,int p){
  if(p<a[r]){
    return 0;
  }else if(p>b[r]){
    return b[r]-a[r]+1;
  }else{
    return p-a[r]+1;
  }
}
int main(){
  int t,tt,n,i,j,a1,a2,b1,b2;
  long long ans;
  a[1]=1;
  b[1]=1;
  j=1;
  for(i=2;i<1000001;i++){
    if(i>b[j]){
      j++;
    }
    a[i]=j;
    b[i]=j+i-1;
  }
  scanf("%d",&t);
  for(tt=1;tt<=t;tt++){
    ans = 0ll;
    scanf("%d",&a1);
    scanf("%d",&a2);
    scanf("%d",&b1);
    scanf("%d",&b2);
    for(i=a1;i<=a2;i++){
      ans += cnt(i,b2)-cnt(i,b1-1);
    }
    printf("Case #%d: %lld\n",tt,((long long)(a2-a1+1))*((long long)(b2-b1+1))-ans);
  }
  return 0;
}
