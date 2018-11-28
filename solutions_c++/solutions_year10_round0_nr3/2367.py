#include <stdio.h>
#include <queue>

using namespace std;

int t,N,k,R,atual,total,teste=1,i,x,g;

int main(){
	
	scanf("%d",&t);
	
	while(t--){
		
		scanf("%d %d %d",&R,&k,&N);
		
		queue <int> q;
		
		for(i=1;i<=N;i++){
			scanf("%d",&x);
			q.push(x);
		}
		total = 0;
		for(i=1;i<=R;i++){
			atual = 0;
			g = 0;
			while(g<N){
				x = q.front();
				if(atual + x <= k){
					atual = atual + x;
					q.pop();
					q.push(x);
					g++;
				}else{
					break;	
				}
			}
			
			
			total = total + atual;
		}
		printf("Case #%d: %d\n",teste++,total);
	}
	
	
}
