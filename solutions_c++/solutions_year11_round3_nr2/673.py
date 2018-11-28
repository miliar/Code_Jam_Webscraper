#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<string>
#include<math.h>
using namespace std;


int a[1010],pre,bb[1010],minn,ans,t1,tmp;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("bb.out","w",stdout);
	int t,k,i,j,T,L,N,C;
	scanf("%d",&T);
	for(k=1;k<=T;k++) {
		scanf("%d%d%d%d",&L,&t,&N,&C);
		for(i=0;i<C;i++) scanf("%d",&a[i]);
		printf("Case #%d: ",k);
		bb[0]=pre=0;
		for(i=1;i<=N;i++) {
			bb[i]=bb[i-1]+a[pre];
			pre=(pre+1)%C;
		}
		if(L==0) printf("%d\n",2*bb[N]);
		else if(L==1) {
			minn=2*bb[N];
			for(i=0;i<N;i++) {
				if(2*bb[i+1]>=t) {
					if(t<=2*bb[i]) ans=2*bb[N]-bb[i+1]+bb[i];
					else ans=2*bb[N]-(bb[i+1]-bb[i]-(t-2*bb[i])/2);
					if(ans<minn) minn=ans;
				}
			}
			printf("%d\n",minn);
		}
		else {
			minn=2*bb[N];
			for(i=0;i<N;i++) {
				if(2*bb[i+1]>=t) {
					if(t<=2*bb[i]) t1=bb[i+1]+bb[i];
					else t1=2*bb[i+1]-(bb[i+1]-bb[i]-(t-2*bb[i])/2);
					for(j=i+1;j<N;j++) {
						if(2*(bb[j+1]-bb[i+1])+t1>=t) {
							if(t<=2*(bb[j]-bb[i+1])+t1) tmp=bb[j+1]-bb[j];
							else tmp=(bb[j+1]-bb[j]-(t-2*(bb[j]-bb[i+1])-t1)/2);
						}
						if(t1+2*bb[N]-2*bb[i+1]-tmp<minn) minn=t1+2*bb[N]-2*bb[i+1]-tmp;
					}
				}
			}
			printf("%d\n",minn);
		}

	}
	return 0;
}
