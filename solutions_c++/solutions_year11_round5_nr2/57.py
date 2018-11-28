#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;
int in[1010];
int n;
int cnt[20010];
int cc[20010];
inline int f(int x){
    if(x==1)return 1;
    int i,j;
    memcpy(cc,cnt,sizeof(cnt));
    for(i=1;i<=10000;i++){
	if(cc[i]){
//	    printf("i=%d\n",i);
	    if(i>10001-x)return 0;
	    int k=cc[i],s=0;
	    cc[i]=0;
	    for(j=i+1;j<i+x;j++){
		if(cc[j]<k||cc[j]<cc[j-1])return 0;
		cc[j]-=k;
	    }
	    for(j=i+x;k&&j<=10000;j++){
		int r=max(cc[j-1]-cc[j-x],0);
//		printf("j=%d k=%d r=%d\n",j,k,r);
		
//		printf("r=%d\n",r);
		if(r<cc[j]){
		  //  puts("!");
		    k=min(cc[j]-r,k);
		    cc[j]-=k;
		}else break;
	    }
	}
    }
 //   puts("!");
    return 1;
}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
	int i;
	scanf("%d",&n);
	memset(cnt,0,sizeof(cnt));
	for(i=0;i<n;i++){
	    scanf("%d",&in[i]);
	    cnt[in[i]]++;
	}
	sort(in,in+n);
//	printf("%d:",n);
//	for(i=0;i<n;i++)printf(" %d",in[i]);puts("");
	printf("Case #%d: ",cas++);

	if(n==0){
	    puts("0");
	    continue;
	}
//	f(3);
	int l=1,r=n;
//	/*
	while(l<r){
	    int m=(l+r+1)/2;
//	    printf("%d %d\n",m,f(m));
	    if(f(m))l=m;
	    else r=m-1;
	}
//	*/
	printf("%d\n",l);
    }
}
