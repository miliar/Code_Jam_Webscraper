#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define debug 0
#define dprintf debug&&printf

int g[64], orig[64];

void test() {
	int N;
	scanf("%d", &N);
	char s[64];
	dprintf("\n");
	for(int y=0;y<N;y++){
		scanf("%s",s);
		//dprintf("'%s'\n",s);
		g[y] = 0;
		for(int x=0;x<N;x++){
			if(s[x] == '1'){
				g[y] = x;
			}
		}
		orig[y] = g[y];
		dprintf("%d",g[y]);
	}
	dprintf("\n");
	int svar =0;
	for(int i=0;i<N;i++){
		if(g[i]>i){
			int j;
			for(j=i+1;g[j]>i;j++){
				if(j==N){
					printf("fel\n");
					return;
				}
			}
			while(j>i){
				int temp = g[j];
				g[j] = g[j-1];
				g[j-1] = temp;
				j--;
			}
		}
	}
	//sort(g,g+N);


	for(int i=0;i<N;i++){
		dprintf("%d", g[i]);
	}
	dprintf("\n");
	for(int fr=0;fr<N;fr++){
		int to;
		for(to=fr;orig[fr] != g[to];to++){
			int apa = 42;
		}
		while(fr != to){			
			svar++;
			int temp = g[to];
			g[to] = g[to-1];
			g[to-1] = temp;
			to--;
		}
	}
	for(int i=0;i<N;i++){
		dprintf("%d", g[i]);
	}
	dprintf("\n");
	printf("%d\n", svar);
}

int main(){
	int N;
	scanf("%d\n", &N);
	for(int fall=0;fall<N;fall++){	
		printf("Case #%d: ", fall+1);
		test();
	}
	return 0;
}
