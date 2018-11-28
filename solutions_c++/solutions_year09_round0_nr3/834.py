#include <iostream>
#include <string>
#include <stdio.h>
#include <memory.h>

using namespace std;

const long long M = 10000;
const char* W = "welcome to code jam";

int lena, lenW;
char a[1000];
long long res, c[1000][30];



void input()
{
    gets(a);
    lena = strlen(a);
}

void process()
{
    //
    memset(c, 0, sizeof(c));
    for (int i=0; i<lena; i++) if (a[i] == W[0]) c[i][0] = 1;

    //
    for (int j=1; j<lenW; j++) for (int i=0; i<lena; i++) if (a[i] == W[j])
    {
        for (int k=0; k<i; k++) if (a[k] == W[j-1])
        {
            c[i][j] += c[k][j-1];
        }
        c[i][j] %= M;
    }

    //
    res = 0;
    for (int i=0; i<lena; i++) res += c[i][lenW-1];
    res %= M;
}


int main()
{
    //
    int numtest;
    scanf("%d\n", &numtest);

    //
    lenW = strlen(W);
    for (int i=0; i<numtest; i++)
    {
        input();
        process();
        printf("Case #%d: %04lld\n", i+1, res);
    }

    return 0;
}

