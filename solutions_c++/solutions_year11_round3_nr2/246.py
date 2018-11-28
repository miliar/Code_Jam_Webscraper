#include<stdio.h>
#include<algorithm>
using namespace std;
int T,p,n,l,i,j,k,c,m;
int a[1001];
int coun[1001];
int w[1001];
long long ans,f1,f2,sum,t;
inline bool cmp(const int &x,const int &y){
	return a[y]<a[x];
}
int main(){
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d%I64d%d%d",&l,&t,&n,&c),ans=0;
    for(i=0;i<c;++i){
      scanf("%d",&a[i]);
      coun[i]=n/c+(i<n%c),w[i]=i;
      ans+=(long long)coun[i]*a[i]*2;
    }
    sort(w,w+c,cmp);
    printf("Case #%d: ",p),sum=0;
    for(i=0;i<n;++i){
      if(t<=sum+2*a[i%c]) break;
      else {sum+=2*a[i%c];coun[i%c]--;}
    }
    if(i==n || !l ){
      printf("%I64d\n",ans);continue;}
    f1=a[i%c]-(t-sum)/2;coun[i%c]--;
    k=l-1;
    for(j=0;j<c;++j){
      if(coun[w[j]]<k) 
        k-=coun[w[j]],f1+=(long long)coun[w[j]]*a[w[j]];
      else{
		f1+=k*a[w[j]];break;
		}
    }
    f2=0;k=l;
    for(j=0;j<c;++j){
      if(coun[w[j]]<k) 
        k-=coun[w[j]],f2+=(long long)coun[w[j]]*a[w[j]];
      else{
	    f2+=k*a[w[j]];break;
      }
    }
    if(f1<f2) ans-=f2;
    else ans-=f1;
    printf("%I64d\n",ans);
  }
  scanf("%d",&T);
  return 0;
}

