#include<cstdio>

int t,n,k,r;

int main (){
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++){
		scanf("%d%d",&n,&k);
		while(k%2 == 1){
			r++;
			k>>=1;
		}
		printf("Case #%d: %s\n",tc, r<n?"OFF":"ON");
		r=0;
	}
}
