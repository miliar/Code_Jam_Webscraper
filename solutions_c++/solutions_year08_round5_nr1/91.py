#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>

using namespace std;

char comando[100];
int len;
int times;
int limits[8000][2];
int bestbef[8000][2];
int bestaft[8000][2];
int area;
int total;
int x, y;
int dir;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int main() {
    int teste, t;
    int i, j, k;
    scanf("%d", &teste);
    
    for (t=0; t<teste; t++) {
        int n;
        for (i=0; i<8000; i++){
            limits[i][0] = 4000;
            limits[i][1] = -4000;
        }
        x = 0;
        y = 0;
        dir = 0;
        area = 0;
        scanf("%d", &n);
        for (i=0; i<n; i++){
            scanf("%s %d", comando, &times);
//            printf("%s %d\n", comando, times);
            len = strlen(comando);
            for (j=0; j<times; j++){
                for (k=0; k<len; k++){
                    if (comando[k] == 'R') dir = (dir+1)%4;
                    if (comando[k] == 'L') dir = (dir+3)%4;
                    if (comando[k] == 'F') {
                       x += dx[dir];
                       y += dy[dir];
                       //printf("%d %d\n", x, y);
                       area += dx[dir]*y;
                       if (dy[dir]==1) {
                          if (limits[y+4000][0] > x) limits[y+4000][0] = x;
                          if (limits[y+4000][1] < x) limits[y+4000][1] = x;
                       }
                       if (dy[dir]==-1) {
                          if (limits[y+4001][0] > x) limits[y+4001][0] = x;
                          if (limits[y+4001][1] < x) limits[y+4001][1] = x;
                       }
                    }
                }
            }
        }
        if (area < 0) area = -area;
//        printf("%d\n", area);
        total = 0;
        int aux = 4000;
        for (i=0; i<8000; i++){
            if (limits[i][0]<aux) aux = limits[i][0];
            bestbef[i][0] = aux;
        }
        aux = -4000;
        for (i=0; i<8000; i++){
            if (limits[i][1]>aux) aux = limits[i][1];
            bestbef[i][1] = aux;
        }
        aux = 4000;
        for (i=7999; i>=0; i--){
            if (limits[i][0]<aux) aux = limits[i][0];
            bestaft[i][0] = aux;
        }
        aux = -4000;
        for (i=7999; i>=0; i--){
            if (limits[i][1]>aux) aux = limits[i][1];
            bestaft[i][1] = aux;
        }
        for (i=0; i<8000; i++){
            int aux = min(bestbef[i][1], bestaft[i][1]) - max(bestbef[i][0], bestaft[i][0]);
            if (aux < 0) continue;
/*            if (aux!=0) printf("%d %d\n", i, aux);
            if (i>=4000 && i<4010) printf("%d %d %d %d %d %d\n", i, aux, bestbef[i][1], bestaft[i][1], bestbef[i][0], bestaft[i][0]);*/
            total += aux;
        }
        printf("Case #%d: %d\n", t+1, total-area);   
    }
    return 0;    
}
