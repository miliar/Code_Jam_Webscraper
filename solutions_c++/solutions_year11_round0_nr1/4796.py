#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>
#define MAX 110
#define absol(x) ((x) < 0 ? -(x): (x))
using namespace std;

int main(){
	int i, j, k, n, m, T, izq, der, cuenta, suma, cuenta_izq, cuenta_der, next[MAX];
	string move[MAX];
	cin >> T;
	for(k = 1; k <= T; k++){
		scanf("%d", &n);
		for(i = 0; i < n; i++){
			cin >> move[i] >> next[i];
		}
		izq = der = 1;
		cuenta = 0;
		cuenta_izq = cuenta_der = 0;
		for(i = 0; i < n; i++){
			if(move[i][0] == 'O'){
				suma = absol(izq-next[i]);
				if(cuenta_der < suma){
					cuenta+=(suma-cuenta_der);
					cuenta_izq += (suma-cuenta_der)+1;
				}
				else
					cuenta_izq += 1;
				cuenta++;
				cuenta_der = 0;
//				cuenta_izq += suma+1;
				izq = next[i];
			}
			else{
				suma = absol(der-next[i]);
				if(cuenta_izq < suma){
					cuenta+=(suma-cuenta_izq);
					cuenta_der += (suma-cuenta_izq)+1;
				}
				else
					cuenta_der += 1;
				cuenta++;
				cuenta_izq = 0;
//				cuenta_der += suma+1;
				der = next[i];
			}
//printf("cuenta = %d, c_izq = %d, c_der = %d, izq = %d, der = %d\n", cuenta, cuenta_izq, cuenta_der, izq, der);
		}
		printf("Case #%d: %d\n", k, cuenta);
	}
	return 0;
}
