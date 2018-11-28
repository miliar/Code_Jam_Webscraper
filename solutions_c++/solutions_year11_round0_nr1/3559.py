#include<iostream>
using namespace std;
#include"math.h"
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int oy,by,os,bs,tm;
	int i,n,t,T;
	char c;
	while(scanf("%d",&T)!=EOF){
		tm=1;
		while(T--){
			scanf("%d",&n);
			oy=by=1;
			os=bs=0;
			for(i=0;i<n;i++){
				scanf("%*c%c%*c%d",&c,&t);
				if(c>70){
					os+=(int)fabs(t-oy)+1;
					if(os<=bs) os=bs+1;
					oy=t;
					}
				  else {
					bs+=(int)fabs(t-by)+1;
					if(bs<=os) bs=os+1;
					by=t;
					}
				}
			if(os<bs) os=bs;
			printf("Case #%d: %d\n",tm++,os);
			}
		}
	return 0;
	}
