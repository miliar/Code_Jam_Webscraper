#include<cstdio>

int t,s,n,si,i,j,p,r;

int main(){
	scanf("%d",&t);

	for(i=1;i<=t;++i){
		r=0;
		scanf("%d %d %d",&n,&s,&p);
		for(j=0;j<n;++j){
			scanf("%d",&si);
			if(si>3*p-3)
				++r;
			else{
				if(((si==3*p-4 && p-2>=0) || (si==3*p-3 && p-2>=0)) && s>0){
					--s;
					++r;
				}
			
			
			}
		
		}
		printf("Case #%d: %d\n",i,r);
	
	}

	return 0;
}
