#include <cstdio>


int main(){
	freopen("A-large-practice.in","r",stdin);
	freopen("A-large-practice.out","w",stdout);
	int N, C, I, i1, i2;
	const int maxI = 2000;
	int items[maxI];
	scanf("%d",&N);
	for (int n=1;n<=N;n++){
		scanf("%d",&C);
		scanf("%d",&I);
		for (int i=1;i<=I;i++){
				scanf("%d",&items[i]);
		}
		for (int x=1;x<I;x++){
			for (int y=x+1;y<=I;y++){
				if(C== items[x]+items[y]){
					i1=x;
					i2=y;
				}
			}
		}
		printf("Case #%d: %d %d\n",n,i1,i2);
	}

	return 0;
}