#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <cmath>

using namespace std;

pair<int, int> pai[105][105];
int mapa[105][105];
char resp[105][105];
int x,y;
int X[] = {0,-1,1,0};
int Y[] = {-1,0,0,1};
bool inLimits(int cX, int cY){
    return cX >= 0 && cX < x && cY >= 0 && cY < y;
}
pair<int, int> rep(int numX, int numY){
    if(numX == pai[numY][numX].first && numY == pai[numY][numX].second){
           return pai[numY][numX];
    }else  return pai[numY][numX] = rep(pai[numY][numX].first, pai[numY][numX].second);
}
/*void join(int a, int b){
    int repA = rep(A);
    int repB = rep(B);
    int countA = 0, countB = 0;
    for(int i = 0; i < x*y; i++){
        if(pai[i] == repA)countA++;
        else if(pai[i] == repB)countB++;
    }
    if(countA > countB)pai[b] = repA;
    else if(countB > countA)pai[a] = repB;
    else{
        pai[max(a,b)] = min(a,b);
    }
}*/
void read(){
    scanf("%d%d", &y, &x);
    for(int i = 0; i < y; i++){
        for(int j = 0; j < x; j++){
            scanf("%d", &mapa[i][j]);
        }
    }
    memset(resp, 0, sizeof(resp));
    for(int i = 0; i < y; i++){
        for(int j = 0; j < x; j++){
            pai[i][j] = make_pair(j,i);
        }
    }
}
void process(){
    for(int i = 0; i < y; i++){
        for(int j = 0; j < x; j++){
            int menorCoord = 0;
            int volante = mapa[i][j];
            for(int t = 0; t < 4; t++){
                if(inLimits(j + X[t], i + Y[t])){
                    if(mapa[i + Y[t]][j + X[t]] < volante){
                        pai[i][j] = make_pair(j+X[t], i + Y[t]);
                        volante = mapa[i + Y[t]][j + X[t]];
                    }
                }
            }
        }
    }
    map<pair<int, int>,int> mapa;
    mapa.clear();
    for(int i = 0; i < y; i++){
        for(int j = 0; j < x; j++){
            rep(j,i);
        }
    }
    /*for(int i = 0; i < y; i++){
        for(int j = 0; j < x; j++){
            printf("%d %d - ", pai[i][j].first, pai[i][j].second);
        }
        printf("\n");
    }*/
    char cNovo = 'a';
    for(int i = 0; i < y; i++){
        bool oKay = 1;
        for(int j = 0; j < x; j++){
            if(oKay)oKay = 0;
            else printf(" ");
            if(mapa.find(pai[i][j]) != mapa.end()){
                printf("%c", mapa[pai[i][j]]);
            }else{
                mapa[pai[i][j]] = cNovo;
                printf("%c", cNovo++);
            }
        }
        printf("\n");
    }
}
int main(){
    int casos;
    scanf("%d", &casos);
    for(int i = 1; i <= casos; i++){
        read();
        printf("Case #%d:\n", i);
        process();
    }
}
