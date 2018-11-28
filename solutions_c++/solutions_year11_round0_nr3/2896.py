#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C.txt","w",stdout);
	int t,n,c[1005],i,all,sum,cs=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		memset(c,0,sizeof(c));
		for(i=0,sum=0 ; i < n ; i++){
			scanf("%d",&c[i]);
			sum += c[i];
		}
		sort(c,c+n);
		for(i=2,all=c[1] ; i < n ; i++)
			all=all^c[i];
		if(all==c[0])
			printf("Case #%d: %d\n",cs++,sum-c[0]);
		else
			printf("Case #%d: NO\n",cs++);
	}
	return 0;
}
