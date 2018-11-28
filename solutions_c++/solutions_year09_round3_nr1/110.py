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

char message[150]; int tam;
long long resp;
int mapa[255];


long long tobase10(long long b)
{
    long long mult = 1;
    long long res = 0;

    for(int i = tam - 1; i >= 0; i--){
        res += (long long)mapa[message[i]] * mult;
        mult *= b;
    }
    return res;
}

long long tobase10_small(long long b)
{
   long long n = 0;
   long long result=0;
   long long multiplier=1;
     

   for(int i = tam - 1; i>= 0; i--){
       n += mapa[message[i]]*multiplier;
       multiplier *= 10;
   }

   multiplier = 1;

   //printf("n %lld base %lld", n, b);

   while(n>0)
   {
       result+=n%10*multiplier;
       multiplier*=b;
       n/=10;
   }

   //printf(" res %lld\n", result);

   return result;
}

int baseresp;

void ans()
{
    int biggest = 0;
    FOR(i, 0, tam)
        biggest = max(biggest, mapa[message[i]]);
    long long at = tobase10((long long)biggest + 1);
    //resp = min(resp, tobase10((long long)biggest + 1));
    if(at < resp){
        resp = at;
        baseresp = biggest + 1;
    }
}

int mapeados[100];

void solve_small(int pos)
{
    if(pos == tam){
        ans();
        return;
    }

    if(mapa[message[pos]] == -1){
        FOR(i, 0, 10){
            if(pos == 0 && i == 0) continue;
            if(mapeados[i] != -1) continue;
            mapeados[i] = 1;
            mapa[message[pos]] = i;
            solve_small(pos + 1);
            mapa[message[pos]] = -1;
            mapeados[i] = -1;
        }
    } else solve_small(pos + 1);
}

long long solve()
{
    int diff = 0;
    int mapac[255];

    memset(mapac, -1, sizeof(mapac));
    FOR(i, 0, tam){
        if(mapac[message[i]] == -1){
            mapac[message[i]] = 1;
            diff++;
        }
    }
    //printf("diff %d\n", diff);
    if(diff == 1) diff++;
     
    FOR(pos, 0, tam) if(mapa[message[pos]] == -1){
        FOR(i, 0, diff){
            if(pos == 0 && i == 0) continue;
            if(mapeados[i] != -1) continue;
            //printf("pos %d i %d\n", pos, i);
            mapeados[i] = 1;
            mapa[message[pos]] = i;
            break;
        }
    }
    //printf("base %d\n", diff);
    return tobase10((long long)diff);
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 0, t){
        scanf("%s", message);
        tam = strlen(message);
        resp = 1000000000000000000LL;
        memset(mapa, -1, sizeof(mapa));
        memset(mapeados, -1, sizeof(mapeados));
        printf("Case #%d: %lld\n", test + 1, solve());
        //printf("base usada %d\n", baseresp);
    }
    return 0;
}

