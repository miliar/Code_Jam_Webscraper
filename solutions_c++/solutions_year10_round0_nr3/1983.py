#include<cstdio>
long long g[1002],x[1002],loop;
int nx[1002],used[1002];
int main(){
  int t,tt,r,k,n,i,j,p,loopsize;
  long long ans=0;
  scanf("%d",&t);
  for(tt=1;tt<=t;tt++){
    scanf("%d",&r);
    scanf("%d",&k);
    scanf("%d",&n);
    loopsize = 1;
    loop = 0;
    ans = 0;
    for(i=0;i<n;i++){
      scanf("%lld",&g[i]);
      x[i] = 0;
      used[i] = 0;
    }
    for(i=0;i<n;i++){
      for(j=0;j<n;j++){
	p = (i+j)%n;
	if(x[i]+g[p]<=k){
	  x[i] += g[p];
	}else{
	  break;
	}
      }
      nx[i] = (i+j)%n;
    }
    p=0;
    for(i=0;i<r;i++){
      if(used[p]){
	break;
      }
      used[p]++;
      ans += x[p];
      p = nx[p];
    }
    for(j=p;;loopsize++){
      loop += x[j];
      j = nx[j];
      if(j==p){
	break;
      }
    }
    ans += loop*((r-i)/loopsize);
    i += loopsize*((r-i)/loopsize);
    for(;i<r;i++){
      ans += x[p];
      p = nx[p];
    }
    /*
    for(i=0;i<n;i++){
      printf("%lld ",x[i]);
    }printf("\n");
    for(i=0;i<n;i++){
      printf("[%d]",nx[i]);
    }printf("\n");
    for(i=0;i<=loopsize;i++){
      printf("%lld ",y[i]);
    }printf("\n");
    */
    printf("Case #%d: %lld\n",tt,ans);
  }
  return 0;
}
