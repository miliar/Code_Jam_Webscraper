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

int k;
string s;
int used[10], mini;

void conta(string nova)
{
    int resp = 1;
    FOR(i, SZ(nova) - 1)
        if(nova[i] != nova[i + 1])
            resp++;
    mini = min(resp, mini);
}

void codifica(int atual[10])
{
    string nova = "";
    for(int i = 0; i < SZ(s); i += k)
        FOR(j, k)
            nova += s[atual[j] + i];
    conta(nova);
}

void permut(int pos, int atual[10])
{
    if(pos == k){
        codifica(atual);
        return;
    }

    FOR(i, k)
        if(used[i] == -1){
            used[i] = 1;
            atual[pos] = i;
            permut(pos + 1, atual);
            used[i] = -1;
        }
}

int main()
{
    int n;
    scanf("%d", &n);
    FOR(casos, n){
        cin >> k;
        cin >> s;
        FOR(i, 10) used[i] = -1;
        mini = (int)1e8;
        int atual[10];
        permut(0, atual);
        printf("Case #%d: %d\n", casos + 1, mini);
    }
    return 0;
}

