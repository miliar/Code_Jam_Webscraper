#include<iostream>
using namespace std;
#include"math.h"
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,n,i,t,m,tm,min,sum;
	while(scanf("%d",&T)!=EOF){
		tm=1;
		while(T--){
			scanf("%d",&n);
			scanf("%d",&t);
			min=t;
			sum=t;
			for(i=1;i<n;i++){
				scanf("%d",&m);
				t^=m;
				if(min>m) min=m;
				sum+=m;
				}
			if(t==0)  printf("Case #%d: %d\n",tm++,sum-min);
			  else    printf("Case #%d: NO\n",tm++);
			}
		}
	return 0;
	}
