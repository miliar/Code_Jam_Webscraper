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

int t, a, n, tempo;
int botao[201];
bool vezblue[201];
int orablu[2];
int old[2];
char entrada[10];

int main (){
    int contador = 1;
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
	scanf("%d", &t);
	while(t--){
        printf("Case #%d: ", contador);
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            scanf("%s %d", entrada, &a);
            botao[i] = a;
            if(entrada[0] == 'B'){
                vezblue[i] = true;
            }
            else vezblue[i] = false;
        }
        orablu[0] = orablu[1] = 1;
        old[0] = old[1] = 0;
        tempo = 0;
        for(int i = 0; i < n; i++){
            tempo += max(0, (abs(orablu[vezblue[i]]-botao[i]) - (tempo-old[vezblue[i]])))+1;
            orablu[vezblue[i]] = botao[i];
            old[vezblue[i]] = tempo;
        }
        printf("%d\n", tempo);
        contador++;
	}
    return 0;
}
