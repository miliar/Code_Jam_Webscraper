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

// "welcome to code jam"
const char phrase[] = "welcome to code jam";
int pd[600][40]; // posição/tamanho
char buff[600];
int tam;

int cut(int m)
{
    return (m%10000);
}

int solve(int pos, int size)
{
    //printf("pos %d size %d\n", pos, size);
    if(size < 0)
        return 1;

    if(pos >= tam)
        return 0;

    if(pd[pos][size] != -1)
        return pd[pos][size];

    int resp = 0;

    resp = cut(resp + solve(pos + 1, size));

    //printf("pos %d buff[pos] %c 18-size %d phrase[18-size] %c\n", pos, buff[pos], 18-size, phrase[18-size]);
    if(buff[pos] == phrase[18-size])
        resp = cut(resp + solve(pos + 1, size - 1));

    return (pd[pos][size] = cut(resp));
}

int main()
{
    int n;
    scanf("%d", &n); getchar();
    FOR(caso, 0, n){
        //scanf("%s", buff);
        fgets(buff, 600, stdin);
  
        memset(pd, -1, sizeof(pd));
        tam = strlen(buff) - 1;
        int resp = solve(0, 18);

        printf("Case #%d: ", caso + 1);
        if(resp < 1000) printf("0");
        if(resp < 100) printf("0");
        if(resp < 10) printf("0");
        printf("%d\n", resp);
    }
    return 0;

}



