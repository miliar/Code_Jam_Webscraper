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

int t, a, C, D, n, ind, at;

char lista[201];
char entrada[201];

struct combo{
    char um, dois, vira;
} combos[50];

int dest[50][2];
int total[26];

int main (){
    int contador = 1;
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
	scanf("%d", &t);
	while(t--){
        printf("Case #%d: [", contador);
        scanf("%d", &C);
        for(int i = 0; i < C; i++){
            scanf("%s", entrada);
            combos[i].um = entrada[0];
            combos[i].dois = entrada[1];
            combos[i].vira = entrada[2];
        }
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%s", entrada);
            dest[i][0] = entrada[0]-'A';
            dest[i][1] = entrada[1]-'A';
        }
        scanf("%d", &n);
        scanf("%s", entrada);
        memset(total, 0, sizeof(total));
        ind = at = 0;
        bool mudou;
        for(int i = 0; i < n; i++){
            mudou = false;
            lista[at] = entrada[i];
            if(at)
            for(int j = 0; j < C; j++){
                if((lista[at] == combos[j].um && lista[at-1] == combos[j].dois) || (lista[at-1] == combos[j].um && lista[at] == combos[j].dois)){
                    total[lista[--at]-'A']--;
                    lista[at] = combos[j].vira;
                    mudou = true;
                    break;
                }
            }
            at++;
            if(!mudou){
                total[entrada[i]-'A']++;
                for(int j = 0; j < D; j++){
                    if(total[dest[j][0]] && total[dest[j][1]]){
                        memset(total, 0, sizeof(total));
                        at = 0;
                        break;
                    }
                }
            }
        }
        if(at) printf("%c", lista[0]);
        for(int i = 1; i < at; i++){
            printf(", %c", lista[i]);
        }
        printf("]\n");
        contador++;
    }
    return 0;
}
