#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int C, D,N;
char map[300][300], off[300][300];
char pilha[200];
int tam;

void process(){
	char str[300];
	scanf("%d", &C);
	
	memset(map,0,sizeof(map));
	memset(off,0,sizeof(off));
	tam = 0;
	
	for(int i = 1; i <= C; i++){
		scanf("%s", str);
		map[str[0]][str[1]] = map[str[1]][str[0]] = str[2];
	}
	
	scanf("%d", &D);
	
	for(int i = 1; i <= D; i++){
		scanf("%s", str);
		off[str[0]][str[1]] = off[str[1]][str[0]] = 1;
	}
	
	scanf("%d", &N);
	scanf("%s", str);
	for(int i = 0; i < N; i++){
		if(tam > 0 && map[pilha[tam-1]][str[i]] != 0){
			pilha[tam-1] = map[pilha[tam-1]][str[i]];
		}else{
			bool clear = false;
			for(int j = 0; j < tam; j++){
				if(off[pilha[j]][str[i]]){
					clear = true;
				}
			}
			if(clear){
				tam = 0;
			}else{
				pilha[tam++] = str[i];
			}
		}
	}
	printf("[");
	
	for(int i = 0; i < tam; i++){
		if(i > 0)
			printf(", ");
		printf("%c",pilha[i]);
	}
	
	printf("]\n");
}

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		
		printf("Case #%d: ", i);
		
		process();
	}
	
	return 0;
}
