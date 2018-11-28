#include <iostream>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, B) for(int A = 0; A < (int)B; A++)
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ERRO 1e-9
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

char engines[110][110];
char queries[1100][110];

int main()
{
    int n, s, q;
    map<string, int> mapa;
    scanf("%d", &n);
    FOR(caso, n){
        mapa.clear();
                
        scanf("%d", &s); getchar();
        FOR(i, s){
            fgets(engines[i], 110, stdin);
            string ss(engines[i]);
            mapa[ss] = i;
        }
        
        list<int> lista[110];

        scanf("%d", &q); getchar();
        FOR(i, q){
            fgets(queries[i], 110, stdin);
            string ss(queries[i]);
            lista[mapa[ss]].push_back(i);
        }

        int swaps = -1, atual = -1;
        while(1){
            /*printf("S and list\n");
            FOR(i, s){
                printf("%s", engines[i]);
                for(list<int>::iterator it = lista[i].begin(); it != lista[i].end(); it++)
                    printf("%d ", *it);
                printf("\n");
            }*/

            int pos = 0, later = -1;
            FOR(i, s){
                if(i != atual && lista[i].empty()){
                    pos = i;
                    break;
                }
                if(i != atual && *(lista[i].begin()) > later){
                    later = *(lista[i].begin());
                    pos = i;
                }
            }
            //printf("pos %d later %d\n", pos, later);

            swaps++;
            //printf("Swaps %d\n", swaps);
            atual = pos;
            
            if(lista[pos].empty()) break;

            FOR(i, s){
                while(1){
                    if(lista[i].empty()) break;
                    if(*(lista[i].begin()) <= later)
                        lista[i].erase(lista[i].begin());
                    else break;
                }
            }
        }
        printf("Case #%d: %d\n", caso + 1, swaps);
    }
    return 0;

}

