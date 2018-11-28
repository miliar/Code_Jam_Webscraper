/*
 *  Problema:
 *  Tecnica Utilizada:  Ad hoc - Aritmetica
 *	
 *
 *  Dificuldade: 
 *	Complexidade:
 *				O(  )
 */

#include <map> 
#include <set> 
#include <list>
#include <cmath> 
#include <queue> 
#include <ctime>
#include <cfloat>
#include <vector> 
#include <string> 
#include <cstdio>
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <sstream>
#include <iostream>
#include <algorithm>

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFF

//Lembrete : declaracao de variavel no loop
//Iteracao no intervalo [a, b)
#define FOR(i, a, b) for(int i = a; i < b; ++i)
//Iteracao reversa no interalo [a, b) 
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
//Iteracao no intervalo [0, n)
#define REP(i, N) FOR(i, 0, N)
//Iteracao reversa no intervalo [n, 0)
#define RREP(i, N) RFOR(i, N, 0)
//Iteracao de estrutura STL usando iterator TI(X)
#define FORIT(i, a) for( IT(a) i = a.begin(); i != a.end(); i++ )

//Fill preenche o vetor com algum valor usando memset
#define FILL(X, V) memset( X, V, sizeof(X) )

//TI retorna o tipo de X, e usado para declaracoes em que nao se conhece o tipo a priori
//Usado normalmente para reotrnar o iterador de inicio de uma estrutura
#define IT(X) typeof(X.begin())

//ALL forma um range de begin() ate end()
#define ALL(V) V.begin(), V.end()

//Size retorna o size() da estrutura
#define SIZE(V) (int)V.size()

//pb = push_back
#define pb push_back
//mp = make_pair
#define mp make_pair

using namespace std;

long long gcd(int x, int y){
    long long aux;
    while(y){
        aux = x;
        x = y;
        y = aux%y;
    }
    return x;
}
int main(){
    long long t, n, pd, pg, teste = 1;
    cin >> t;
    
    while(t--){
        cin >> n >> pd >> pg;
        
        long long g = gcd(pd, 100);
        
        cout << "Case #" << teste++ << ": ";
        if(100/g > n || (pg == 100 && pd != 100) || (pg == 0 && pd != 0))
            cout << "Broken" << endl;
        else
            cout << "Possible" << endl;
    }
    return 0;
}
