#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
using namespace std;

typedef long long int int64;

char v[15000][50];
char lista[150][50];
bool used[50];

int n, m;

bool escolhe(char c, int x, int y, int z) {
	for (int i = 0; i < n; i++) {
		
		if (strlen(v[i]) != strlen(v[x])) continue;
		
		bool erro = true;
				
		for (int j = 0; j < strlen(v[i]); j++) {
			if (c == v[i][j]) {
				erro = false;
				break;
			}	
		}
		
		if (erro) continue;

		for (int j = 0; j < strlen(v[x]); j++) {
			if (used[j] && v[i][j] != v[x][j]) {
				erro = true;
				break;	
			}
		}
		if (erro) continue;
		
		for (int a = 0; a < y; a++) {
			for (int b = 0; b < strlen(v[i]); b++) {
				if (lista[z][a] == v[i][b] && !used[b]) {
					erro = true;
					break;
				}
			}
			if (erro) break;
		}
		
		if (erro) continue;
		
		return true;
	}
	return false;
}

bool match(char c, int x) {
	bool res = false;
	for (int i = 0; i < strlen(v[x]); i++) {
		if (c == v[x][i]) {
			used[i] = true;
			res = true;
		}	
	}
	return res;
}

int main()
{	
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", v[i]);
		}
		for (int i = 0; i < m; i++) {
			scanf("%s", lista[i]);	
		}
		printf("Case #%d:", k+1);
		int res, maior = 0, x;
		//itera nas listas
		for (int i = 0; i < m; i++) {
			maior = 0;
			x = 0;
			// itera nas palavras
			for (int j = 0; j < n; j++) {
				memset(used, false, sizeof(used));
				res = 0;
				// itera na lista
				for (int a = 0; a < 26; a++) {
					if (escolhe(lista[i][a], j, a, i)) {
						if (!match(lista[i][a], j)) {
							res++;
						}
					}	
				}
				//printf("\n%d\n", res);
				if (res > maior) {
					maior = res;
					x = j;	
				}
			}
			printf(" %s", v[x]);
		}
		printf("\n");
	}
	return 0;
}