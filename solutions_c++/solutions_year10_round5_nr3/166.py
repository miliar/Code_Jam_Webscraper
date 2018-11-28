#include<stdio.h>
#define MAX 4500000
int a[4500010],h[4500010],k,ans,v[4500010];
int main(){
freopen("C-small-attempt0.in","r",stdin);
freopen("C-small-attempt0.out","w",stdout);
int T,t,n,i,x,y;
scanf("%d",&T);
for(t=1;t<=T;t++){
k=0;ans=0;
scanf("%d",&n);
for(i=0;i<4500010;i++){a[i]=0;v[i]=0;}
for(i=0;i<n;i++){
scanf("%d%d",&x,&y);
a[x+2000010]+=y;
if(v[x+2000010])continue;
if(a[x+2000010]>1){h[k++]=x+2000010;v[x+2000010]=1;}
}
for(i=0;i<k;i++){
x=h[i%MAX];v[x]=0;
if(a[x]<=1)continue;
y=(a[x]/2);ans+=y;
a[x-1]+=y;
a[x+1]+=y;
a[x]-=2*y;
if(a[x-1]>1&&v[x-1]==0){h[k++%MAX]=x-1;v[x-1]=1;}
if(a[x+1]>1&&v[x+1]==0){h[k++%MAX]=x+1;v[x+1]=1;}
}
printf("Case #%d: %d\n",t,ans);
}
scanf(" ");
}
