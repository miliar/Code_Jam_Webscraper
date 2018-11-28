#include <cstdio>

int main(){

	int casos, jueces, sorpresas, score, a, resultado;

	scanf("%d\n",&casos);

	for(int i=0; i<casos; i++){
		resultado=0;
		scanf("%d%d%d",&jueces, &sorpresas, &score);

		for(int j=0; j<jueces; j++){
			
			scanf("%d",&a);
			a-=score;
			if(a==(score*2)-3 || a==(score*2)-4){
				if(sorpresas>0 && a>=0){
				resultado++;
				sorpresas--;
				}
			}
			else if(a<(score*2)-4){}
			else {
				resultado++;
			}
		}

		printf("Case #%d: %d\n",i+1,resultado);
	}
}
