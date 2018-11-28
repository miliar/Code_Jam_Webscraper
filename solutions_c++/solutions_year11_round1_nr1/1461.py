#include <stdio.h>
#include <stdlib.h>

int main(){
    int T,N,i,j,aux,D,G,res;
    scanf("%d",&T);
    for(i=0;i<T;i++){
                     scanf("%d %d %d",&N,&D,&G);
                     res = 0;
			while(N != 0){
                                      aux = (D * N) % 100;
					if(aux == 0 ) res = 1;
					N--;

                     }                                     
		if(res == 1 && (G != 100 || D == 100) && (G!=0 || D == 0))printf("Case #%d: Possible\n",i+1);
		else printf("Case #%d: Broken\n",i+1);
    }
}
    
