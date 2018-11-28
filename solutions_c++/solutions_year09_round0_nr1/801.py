#include <iostream>
#include <string>
#include <stdio.h>
#include <memory.h>

using namespace std;

int numtest, len, n;
char w[5000][16];

int bcnt;
bool b[16][26];



void input()
{
    scanf("%d%d%d", &len, &n, &numtest);
    for (int i=0; i<n; i++) scanf("%s", w[i]);
}


bool analyze(char a[1000])
{
    int lena = strlen(a);

    //
    bcnt = 0;
    memset(b, false, sizeof(b));

    //
    bool k = false;
    for (int i=0; i<lena; i++)
    {
        if (bcnt > len) return false;
        switch (a[i])
        {
            case '(': k = true; break;
            case ')': k = false; bcnt++; break;
            default : b[bcnt][a[i]-'a'] = true; if (!k) bcnt++; break;
        }
    }
    return bcnt==len;
}

bool match(char w[16])
{
    for (int i=0; i<len; i++) if (!b[i][w[i]-'a']) return false;
    return true;
}

void process()
{
    char a[1000];
    int res;

    for (int i=0; i<numtest; i++)
    {
        //
        res = 0;
        scanf("%s", a);

        //
        if (analyze(a))
        {
            for (int j=0; j<n; j++) if (match(w[j])) res++;
        }

        //
        printf("Case #%d: %d\n", i+1, res);
    }
}

int main()
{
    input();
    process();

    return 0;
}

