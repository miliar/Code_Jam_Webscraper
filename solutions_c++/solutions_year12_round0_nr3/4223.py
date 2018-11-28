// RecycledNumbers.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>

#include <iostream>
#include <vector>

using namespace std;

struct RecycledNumber
{
    int n;
    int m;
};

vector<RecycledNumber> g_Pairs;

bool IsRecycledNumber(int a, int b)
{
    char szA[30];
    char szB[30];
    sprintf(szA, "%d", a);
    sprintf(szB, "%d", b);

    int i, iLen = strlen(szA);
    for (i = 1; i < iLen; i++) {
        if (memcmp(szA+i, szB, iLen-i) == 0 &&
            memcmp(szA, szB + iLen-i, i) == 0)
            return true;
    }
    return false;
}

void AddPair(int a, int b)
{
    RecycledNumber p = {a,b};
    g_Pairs.push_back(p);
}

void CountPairs(int iTc, int start, int end)
{
    int nCount = 0;
    int i;
    for (i = 0; i < g_Pairs.size(); i++) {
        if (g_Pairs[i].n >= start &&
            end >= g_Pairs[i].m)
            nCount++;
    }

    printf("Case #%d: %d\n", iTc, nCount);
}

int _tmain(int argc, _TCHAR* argv[])
{

    int i, j;
    for (i = 10; i < 100; i++) {
        for (j = i+1; j < 100; j++) {
            if (IsRecycledNumber(i, j)) {
                AddPair(i,j);
                //printf("%d %d\n", i, j);
            }
        }
    }
    for (i = 100; i < 1000; i++) {
        for (j = i+1; j < 1000; j++) {
            if (IsRecycledNumber(i, j)) {
                AddPair(i,j);
                //printf("%d %d\n", i, j);
            }
        }
    }

    int nTestCase;
    scanf("%d", &nTestCase);
    
    for (i = 0; i < nTestCase; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        CountPairs(i+1, a, b);
    
    }

	return 0;
}

