#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#define TAM 256

using namespace std;
int v[TAM];
char s[TAM];
int main(){
	int n, i, j, fim, total, tam;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf(" %s", s);
		tam = strlen(s);
		fim = 0;
		memset(v, -1, sizeof(v));
		v[s[0]] = 1;
		for(j = 1; j < tam; j++){
			if(v[s[j]] == -1){ 
				v[s[j]] = fim++;
				if(fim == 1) fim = 2;
			}
		}
		if(fim == 0 || fim == 1) fim = 2;
		total = 0;
		for(j = 0; j < tam; j++){
			total += v[s[j]]*pow(fim, (tam-j-1));
		}
		printf("Case #%d: %d\n", i+1, total);
	}
	return 0;
}
