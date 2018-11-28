#include <stdio.h>
#include <queue>

using namespace std;

int main(){
	long long T,R,k,kk,N,g,i,j,l,loe;
	scanf("%lli\n",&T);
	for(i=1;i<=T;i++){
		queue <long long>q;
		kk=0;
		loe=0;
		scanf("%lli %lli %lli\n",&R,&k,&N);
		for(j=0;j<N;j++){
			scanf("%lli ",&g);
			q.push(g);
		}
		for(j=0;j<R;j++){
			l=0;
			kk=0;
			while(l<N){
				g=q.front();
				if(kk+g>k){
					loe+=kk;
					kk=0;
					break;
				}
				else{
					kk+=g;
					q.pop();
					q.push(g);
				}
				l++;
				if(l==N)loe+=kk;
			}
		}
		printf("Case #%lli: %lli\n",i,loe);
	}
	return 0;
}
