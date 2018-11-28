#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#define TAM 1024
using namespace std;
char s[TAM];
int v[TAM], temp[TAM];
int main(){
	int i, j, n, tam, cs = 1, a, k;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf(" %s", s);
		tam = strlen(s);
		for(j = 0; j < tam; j++){
			temp[j] = v[j] = s[j]-'0';
		}
		next_permutation (v,v+tam);
		
		printf("Case #%d: ", cs++);
		if(v[0] == 0){
			for(j = 1; j < tam; j++){
				if(v[j] != 0){
					break;
				}
			}
			v[0] = v[j];
			v[j] = 0;
		}
		for(j = 0; j < tam; j++){
			printf("%d", v[j]);
			if(j == 0 && v[0] <= temp[0]){
				if(v[0] == temp[0]){
					k = 1;
					while(k < tam && v[k] == temp[k]){
						k++;
					}
					if(k < tam && v[k] > temp[k]){
						continue;
					}
				}
				printf("0");
			}
		}
		printf("\n");
	}
	return 0;
}