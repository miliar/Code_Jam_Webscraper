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

int t, a, b, c, n;
int bombom[2001];

int main (){
    int contador = 1;
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
	scanf("%d", &t);
	while(t--){
        printf("Case #%d: ", contador);
        scanf("%d", &n);
        a = b = c = 0;
        for(int i = 0; i < n; i++){
            scanf("%d", &bombom[i]);
            a ^= bombom[i];
            b |= bombom[i];
            c += bombom[i];
        }
        if(a) printf("NO\n");
        else{
            sort(bombom, bombom+n);
            printf("%d\n", c-bombom[0]);
        }
        contador++;
    }
    return 0;
}
