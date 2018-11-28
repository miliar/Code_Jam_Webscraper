#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
#include <complex>
#include <list>

using namespace std;

void ASS(bool b)
{
    if (!b)
    {
	    ++*(int*)0;
    }
}

#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))
#define CLX(x, y) memset(x, y, sizeof(x))

#pragma comment(linker, "/STACK:106777216")

typedef vector<int> vi;
typedef long long LL;

int p[] = {24, 13, 5, 8, 2, 22, 11, 1, 10, 20, 14, 12, 23, 18, 4, 21, 25, 15, 3, 17, 9, 6,
19, 7, 0, 16};

char s[1 << 20];

int main()
{
    {
        vi g(26);
        FOR(i, 26)
            g[p[i]] = i;
        FOR(i, 26)
            p[i] = g[i];
    }
    freopen("c:\\my\\in.txt", "r", stdin);
    freopen("c:\\my\\out.txt", "w", stdout);
    int n;
    gets(s);
    sscanf(s, "%d", &n);
    FOR(i, n)
    {
        gets(s);
        int k = (int)strlen(s);
        FOR(j, k)
        {
            char c = s[j];
            if (c >= 'a' && c <= 'z')
                c = 'a' + p[c - 'a'];
            if (c >= 'A' && c <= 'Z')
                c = 'A' + p[c - 'A'];
            s[j] = c;
        }
        cout << "Case #" << (i + 1) << ": " << s << endl;
    }


    return 0;
}