#include<stdio.h>
long long a[2010],k,K,ans,r,b[1010],x,y;
int p[1010],d[1010];
int main(){
int T,t,n,i,j;
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%I64d%I64d%d",&r,&K,&n);
a[0]=0;ans=0;
for(i=1;i<=n;i++){scanf("%I64d",&a[i]);a[i]+=a[i-1];d[i-1]=-1;}
for(;i<=2*n;i++)a[i]=a[n]+a[i-n];
if(K>=a[n]){ans=r*a[n];printf("Case #%d: %I64d\n",t,ans);continue;}
k=K;
for(i=0,j=0;i<n;i++){
for(;a[j]-a[i]<=k;j++);
j--;
p[i]=j%n;
}
d[0]=0;b[0]=0;
for(i=0,j=0;d[p[i]]==-1&&j<r;i=p[i],j++){d[p[i]]=d[i]+1;if(p[i]>=i)b[p[i]]=a[p[i]]-a[i];else b[p[i]]=a[p[i]+n]-a[i];b[p[i]]+=b[i];}
if(j==r)ans+=b[i];
else{
ans+=b[p[i]];
r-=d[p[i]];
x=d[i]+1-d[p[i]];
if(p[i]>=i)y=a[p[i]]-a[i];
else y=a[p[i]+n]-a[i];
y+=b[i];
ans+=(r/x)*(y-b[p[i]]);
r=r%x;
for(i=p[i],j=0;j<r;i=p[i],j++){if(p[i]>=i)ans+=a[p[i]]-a[i];else ans+=a[p[i]+n]-a[i];}
}
printf("Case #%d: %I64d\n",t,ans);
}
}
