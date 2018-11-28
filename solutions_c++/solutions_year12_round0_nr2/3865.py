#include<stdio.h>

using namespace std;

int main(){
	
	int T,N,S,p,t,i,j,r,n;
	
	scanf("%d",&T);
	for(i=1; i<=T; i++){
		scanf("%d %d %d", &N, &S, &p);
		n=0;
		for(j=0; j<N; j++){
			scanf("%d",&t);
			r=t/3;
			t%=3;
			if(t>0)
				r++;
			if(r>=p){
				n++;
			}
			else{
				if(S>0){
					if(t==2 || (t==0 && r!=0)){
						r++;
						if(r>=p){
							n++;
							S--;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",i,n);
	}
	return 0;
}
