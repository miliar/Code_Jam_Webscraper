#include <iostream>
#include <cstdio>
#include <vector>
#define MAXN 4096
#define MAXP 12
#define INF 1000010000
using namespace std;
int mecze[MAXN][MAXP];
int ile_max[MAXN];
int koszty[MAXN];
int main() {
    int t;
    scanf("%d", &t);
    for(int z=1; z<=t; z++) {
	for(int i=0; i<MAXN; i++) {
	    for(int j=0; j<MAXP; j++)
		mecze[i][j] = INF;
	    koszty[i] = 0;
	    ile_max[i] = 0;
	}
	int P;
	scanf("%d", &P);
	int ileteam = 1<<P;
// 	cout << P << endl;
// 	cout << ileteam << endl;
	for(int i=0; i<ileteam; i++)
	    scanf("%d", &ile_max[i]);
	for(int i = P-1; i>=0; i--) {
	    int pot = ( 1 << i );
	    for(int j= 0; j<pot; j++)
		scanf("%d", &koszty[pot+j]);
	}
	for(int i=0; i<ileteam; i++) {
	    for(int j=(P-ile_max[i]); j<=P; j++) {
// 		printf("Musze zagrac %d %d\n", i, j);
		mecze[ileteam+i][j] = 0;
	    }
	    //mecze[ileteam+i][P - ile_max[i]] = 0;
// 	    mecze[(ileteam+i)/2][P - max(ile_max[i], ile_max[i+1])] = 0;
	}
	for(int i=ileteam-1; i>=1; i--) {
	    int lsyn = i*2;
	    int psyn = i*2+1;
	    for(int j=0; j<=P; j++) {
		int nie_gram_tu = mecze[lsyn][j] + mecze[psyn][j];
		int gram_tu = mecze[lsyn][j+1] + mecze[psyn][j+1] + koszty[i];
		mecze[i][j] = min(min(min(gram_tu, nie_gram_tu), INF), mecze[i][max(j-1, 0)]);;
// 		printf("mecze[%d][%d] = %d (%d,%d)\n", i, j, mecze[i][j], gram_tu, nie_gram_tu);
	    }
	}
	printf("Case #%d: %d\n", z, mecze[1][0]);
    }
    return 0;
}