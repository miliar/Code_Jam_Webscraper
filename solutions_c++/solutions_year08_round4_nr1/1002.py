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

#define FOR(A, B) for(int A = 0; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int gate[12000], change[12000];

/*void resolve(int pos, int gate, int changes)
{
    if(pos >= (m+1)/2)
        return;

    resolve(2*pos, gate[2*pos], changes);
    resolve(2*pos + 1, gate[2*pos + 1], changes);



    if(change[2*pos] == 1){
        if(change[2*pos + 1] == 1){
        resolve(2*pos, gate[2*pos], changes);
    } else {

    }
    if(change[2*pos + 1] == 1){
        resolve(2*pos, 1 - gate[2*pos], changes + 1);
    } else {

    }
}*/

int m, v;
int mini;

void resolve(int pos, int changes, int atual[12000])
{
    if(pos > (m-1)/2){
        int t[12000];
        for(int i = (m-1)/2 + 1; i <= m + 1; i++)
            t[i] = atual[i];
        for(int i = (m-1)/2; i>0;i--){
            if(atual[i] == 1)
                t[i] = (t[2*i] && t[2*i + 1]);
            else
                t[i] = (t[2*i] || t[2*i + 1]);
        }
        if(t[1] == v)
            mini = min(mini, changes);
        return;
    }

    atual[pos] = gate[pos];
    resolve(pos + 1, changes, atual);
    if(change[pos] == 1){
        atual[pos] = 1 - gate[pos];
        resolve(pos + 1, changes + 1, atual);
    }

}

int main()
{
    int n;
    scanf("%d", &n);
    int atual[12000];
    FOR(casos, n){
        scanf("%d %d", &m, &v);
        FOR(i, (m-1)/2)
            scanf("%d %d", &gate[i + 1], &change[i + 1]);
        FOR(i, (m+1)/2)
            scanf("%d", &atual[(m+1)/2 + i]);
        mini = (int)1e7;
        resolve(1, 0, atual);
        if(mini > (int)1e6)
            printf("Case #%d: IMPOSSIBLE\n", casos + 1);
        else
            printf("Case #%d: %d\n", casos + 1, mini);
    }
    return 0;

}

