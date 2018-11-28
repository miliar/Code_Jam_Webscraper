#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <sstream>

#define dbg(a) cout << #a << " == " << a << endl
#define print(a) cout << a << endl

using namespace std;

int n;
struct no{
	int tam, n;
} matrix[510][510];

char palavra[510];
char texto[] = "welcome to code jam";
int ttexto = strlen(texto);

int casos = 1;

void process(){
	int tpalavra = strlen(palavra);

	for(int i = 1; i <= ttexto; i++){
		for(int j = 1; j <= tpalavra; j++){
			if(palavra[j-1] == texto[i-1]){
                matrix[i][j].tam = matrix[i-1][j-1].tam + 1;
                matrix[i][j].n = matrix[i-1][j-1].n;
            } else {
                matrix[i][j].tam = max(matrix[i-1][j].tam, matrix[i][j-1].tam);
                matrix[i][j].n = matrix[1][0].n;
            }
 
            if(matrix[i][j-1].tam == matrix[i][j].tam){
                matrix[i][j].n = (matrix[i][j].n + matrix[i][j-1].n)%10000;
            }
              
            if(matrix[i-1][j].tam == matrix[i][j].tam){
                matrix[i][j].n = (matrix[i][j].n + matrix[i-1][j].n)%10000;
            }
        }
    }
    
    if(matrix[ttexto][tpalavra].tam != ttexto){
        matrix[ttexto][tpalavra].n = 0;
    }
	
	
	printf("Case #%d: %.4d\n", casos++, matrix[ttexto][tpalavra].n);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for(int i = 0; i < 510; i++){
        matrix[i][0].n = 0;
        matrix[i][0].tam = 0;
    }

    for(int i = 0; i < 510; i++){
        matrix[0][i].n = 1;
        matrix[0][i].tam = 0;
    }
	
	gets(palavra);
	sscanf(palavra, "%d", &n);
	for(int i = 0; i < n; i++){
		gets(palavra);
		process();
	}
	
	return 0;
}
