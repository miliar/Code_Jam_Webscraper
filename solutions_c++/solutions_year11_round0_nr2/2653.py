#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int map[128];
int combineSize[10];
pair<int, char> combine[10][80];
int opposeSize[10];
int oppose[10][80];

void init(){
	for(int i=0; i<128; i++)
		map[i] = -1;
	map['Q'] = 0;
	map['W'] = 1;
	map['E'] = 2;
	map['R'] = 3;
	map['A'] = 4;
	map['S'] = 5;
	map['D'] = 6;
	map['F'] = 7;
}

void reset(){
	for(int i=0; i<10; i++){
		opposeSize[i] = 0;
		combineSize[i] = 0;
	}
}

int main(){
	init();
	int C, D, N,n;
	char str[1024];
	char out[1024];
	char rule[50];
	int combined;
	
	int T,CASE=1;
	scanf("%d\n",&T);
	while(T--){
		reset();
		
		scanf("%d\n",&C);
		for(int i=0; i<C; i++){
			scanf("%s\n",rule);
			int a = map[rule[0]], b = map[rule[1]];
			combine[a][combineSize[a]++] = make_pair(b, rule[2]);
			combine[b][combineSize[b]++] = make_pair(a, rule[2]);
		}
		
		scanf("%d\n",&D);
		for(int i=0; i<D; i++){
			scanf("%s\n",rule);
			int a = map[rule[0]], b = map[rule[1]];
			oppose[a][opposeSize[a]++] = b;
			oppose[b][opposeSize[b]++] = a;
		}
		
		scanf("%d\n%s\n",&N,str);
		n = 0;
		for(int i=0; i<N; i++){
			int a,b;
			a = map[str[i]];
			if(n>0){
				//checking combine
				b = map[out[n-1]];
				combined = 0;
				if(b>=0){
					for(int j=0; j<combineSize[a]; j++){
						if(b == combine[a][j].first){
							//printf("Combinei %c %c e inseri %c\n",str[i],out[n-1],combine[a][j].second);
							out[n-1] = combine[a][j].second;
							combined = 1;
							break;
						}
					}
				}
				if(!combined){
					out[n++] = str[i];
					//printf("Inseri %c\n",str[i]);
				}
				
				a = map[out[n-1]];
				//checking oppose
				for(int j=n-2; a >=0 && j>=0; j--){
					b = map[out[j]];
					if(b>=0){
						for(int k=0; k<opposeSize[b]; k++){
							if(oppose[b][k]==a){
								n=0;
								//printf("Limpei\n");
								break;
							}
						}
					}
				}
			}else{
				out[n++] = str[i];
				//printf("Inseri %c\n",str[i]);
			}
		
		}
		
		printf("Case #%d: [",CASE++);
		for(int i=0; i<n; i++){
			if(i){
				printf(", ");
			}
			printf("%c",out[i]);
		}
		printf("]\n");
	}
}

