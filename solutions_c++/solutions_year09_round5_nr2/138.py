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

#define MOD 10009

int k, n;
char buff[100];
char terms[10][10];
char dic[25][55];

int nterms;
int termsize[12];
int respk[10];
int words[10];
int alpha[30];
    

int ret(int pos)
{
    int resp = 0;
    int alpha[30];
    memset(alpha, 0, sizeof(alpha));
    FOR(i, 0, pos){
        int p = 0;
        while(dic[words[i]][p] != '\0'){
            alpha[dic[words[i]][p] - 'a'] += 1;
            p++;
        }
    }
    FOR(i, 0, nterms){
        int ret = 1;
        FOR(j, 0, termsize[i])
            ret = (ret*alpha[terms[i][j] - 'a'])%MOD;
        resp += ret;
        resp = (resp%MOD);
    }
    return resp;
}

void bt(int pos)
{
    //printf("pos %d\n", pos);
    if(pos > k) return;

    if(pos > 0)
        respk[pos] = (respk[pos] + ret(pos))%MOD;

    FOR(i, 0, n){
        words[pos] = i;
        bt(pos + 1);
    }
}


int main()
{
    int t;
    scanf("%d", &t);
    FOR(test, 1, t + 1){
        scanf("%s", buff);
        int pos = 0, ter = 0, tpos = 0;
        nterms = 0;
        memset(termsize, 0, sizeof(termsize));
        while(buff[pos] != '\0' && buff[pos] != '\n'){
            if(buff[pos] >= 'a' && buff[pos] <= 'z'){
                terms[ter][tpos++] = buff[pos++];
                terms[ter][tpos] = '\0';
                termsize[ter] += 1;
            } else {
                while(buff[pos] != '\0' && buff[pos] != '\n' && !(buff[pos] >= 'a' && buff[pos] <= 'z')) pos++;
                ter++;
                tpos = 0;
            }
        }
        nterms = ter + 1;
        scanf("%d %d", &k, &n);
        FOR(i, 0, n) scanf("%s", dic[i]);
        memset(respk, 0, sizeof(respk));
        memset(alpha, 0, sizeof(alpha));
        bt(0);
        printf("Case #%d:", test);
        FOR(i, 0, k){
            printf(" %d", respk[i+1]%MOD);
        }
        printf("\n");
    }
    return 0;
}

