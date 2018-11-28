#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vi vector<int>
#define pb push_back
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int n, k;
int stocks[20][30];
int inter[20][20];

int chartsmade[20][20];
int chartsize[20];
int resp;

void bt(int pos, int charts)
{
    //printf("pos %d charts %d\n", pos, charts);
    if(pos == n){
        resp = min(charts, resp);
        return;
    }
    if(charts >= resp) return;

    FOR(i, 0, charts){
        bool pode = true;
        FOR(j, 0, chartsize[i]){
            if(inter[pos][chartsmade[i][j]])
                pode = false;
        }
        if(pode){ 
            //printf("pode colocar cara %d no chart %d\n", pos, i);
            chartsmade[i][chartsize[i]++] = pos;
            bt(pos + 1, charts);
            chartsize[i]--;
        }
    }

    //printf("colocando cara %d num chart novo charts %d\n", pos, charts);
    chartsmade[charts][0] = pos;
    chartsize[charts] = 1;
    bt(pos + 1, charts + 1);
    chartsize[charts] = 0;
}

bool inters(int i, int j)
{
    bool b = stocks[i][0] > stocks[j][0];
    if(stocks[i][0] == stocks[j][0]) return true;
    FOR(a, 0, k){
        if( (stocks[i][a] > stocks[j][a]) != b || stocks[i][a] == stocks[j][a])
            return true;
    }
    return false;
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 1, t + 1){
        scanf("%d %d", &n, &k);
        FOR(i, 0, n){
            FOR(j, 0, k){
                scanf("%d", &stocks[i][j]);
            }
        }
        memset(inter, 0, sizeof(inter));
        memset(chartsize, 0, sizeof(chartsize));
        FOR(i, 0, n) FOR(j, i + 1, n){
            if(inters(i, j)){ 
                //printf("Inter %d %d\n", i, j); 
                inter[i][j] = inter[j][i] = 1; 
            }
        }
        resp = 100000000;
        bt(0, 0);
        printf("Case #%d: %d\n", test, resp);
    }
    return 0;
}

