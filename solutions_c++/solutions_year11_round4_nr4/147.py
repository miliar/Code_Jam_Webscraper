#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

int casos, p, w, a, b;
bool grafo[40][40];

struct estado{
    int threat, conq;
    long long tenho;
    estado (long long t, int thr, int con){
        tenho = t;
        threat = thr;
        conq = con;
    }
    
    const bool operator < (const estado &that) const{
        if(conq != that.conq) return conq > that.conq;
        return threat < that.threat;
    }
    
};

int calc2(long long retorno){
    int ret = 0;
    while(retorno){
        if(retorno&1) ret++;
        retorno >>= 1;
    }
    return ret;
}

int calc (long long tem){
    long long retorno = 0;
    for(int i = 0; i < p; i++){
        if((1LL<<i)&tem){
            for(int j = 0; j < p; j++){
                if(grafo[i][j] && !((1LL<<j)&tem)){
                    retorno |= 1LL<<j;
                }
            }
        }
    }
    return calc2(retorno);
}

int main (){
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
	scanf("%d", &casos);
	int contador = 1;
	while(casos--){
	    memset(grafo, 0, sizeof(grafo));
        printf("Case #%d: ", contador++);
        scanf("%d %d", &p, &w);
        for(int i = 0; i < w; i++){
            scanf("%d,%d", &a, &b);
            grafo[a][b] = true;
            grafo[b][a] = true;
        }
        priority_queue<estado> fila;
        map<long long, bool> mark;
        fila.push(estado(1, calc(1), 0));
        mark[calc(1)] = true;
        while(true){
            estado atual = fila.top(); fila.pop();
            for(int i = 0; i < p; i++){
                 if(((1LL<<i)&atual.tenho) && grafo[i][1]){
                     a = atual.conq;
                     b = atual.threat;
                     goto saida;
                 }
            }
            for(int i = 0; i < p; i++){
                if((1LL<<i)&atual.tenho){
                    for(int j = 0; j < p; j++){
                        if(grafo[i][j] && !((1LL<<j)&atual.tenho)){
                            long long temp = atual.tenho|(1LL<<j);
                            if(!mark[temp]){
                                fila.push(estado(temp, calc(temp), atual.conq+1));
                                mark[temp] = true;
                            }
                        }
                    }
                }
            }
        }
        saida:
        printf("%d %d\n", a, b);
	}
    return 0;
}
