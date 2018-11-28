#include <cstdio>

using namespace std;

int main(){
int t;
scanf("%d", &t);
for(int ti = 1; ti <= t; ti++){
    int n;
    scanf("%d", &n);
    int jmuc[n][2];
    int x =0;
    for(int i = 0; i < n; i ++ ){
        scanf("%d %d", &jmuc[i][0], &jmuc[i][1]);
        for(int j = 0; j < i; j++){
            if( jmuc[i][0] > jmuc[j][0] && jmuc[i][1] < jmuc[j][1] ||  jmuc[i][0] < jmuc[j][0] && jmuc[i][1] > jmuc[j][1] )
               x++;
        }
    }
    printf("Case #%d: %d\n",ti,x);
}
return 0;
}
