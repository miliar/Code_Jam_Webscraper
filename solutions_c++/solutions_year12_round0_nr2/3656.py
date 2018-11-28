#include <cstdio>

using namespace std;

int v;

int main(){
	int casos;
	scanf("%d",&casos);
	
	for(int u=1; u<=casos; u++){
		int t, s, p;
		scanf("%d %d %d",&t,&s,&p);
		int qtd = 0;
		for(int i=0; i<t; i++){
			scanf("%d",&v);
			int a = v/3;
			int b = v/3;
			int c = v/3;
			if(v%3 >= 1) a++;
			if(v%3 >= 2) b++;
			
			if(a >= p) qtd++;
			else if(a+1 >= p){
				if(s > 0 && (a+1) - (b-1) <= 2 && (b-1)>=0){
					qtd++;
					s--;
				}
			}
		}
		
		printf("Case #%d: %d\n",u,qtd);
		
	}
	
	return 0;
}

