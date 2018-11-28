#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iterator>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cstddef>
#include <cmath>
#include <cctype>
#include <ctime>

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(iter,list) for(VAR(iter,(list).begin());iter!=(list).end();++iter)
#define R 50
#define C 50

using namespace std;

void execute(int caseno)
{
        int r, c;
        char str[C], matrix[R][C];
        bool flag_t = true;
        scanf("%d %d", &r, &c);
        REP(i,r) { scanf("%s", str); REP(j,c) matrix[i][j] = str[j]; }

        printf("Case #%d:\n", caseno);

        REP(i,r) REP(j,c)
        {
                bool flag = true;
                REP(k,2) REP(l,2) if(matrix[i+k][j+l] != '#') flag = false;
                if(flag == true) { matrix[i][j] = '/'; matrix[i][j+1] = '\\'; matrix[i+1][j] = '\\'; matrix[i+1][j+1] = '/'; }
        }

        REP(i,r) REP(j,c)
        {
                if(matrix[i][j] == '#') flag_t = false;
        }
        if(flag_t == true) REP(i,r) { REP(j,c) printf("%c",matrix[i][j]); printf("\n"); }
        else printf("Impossible\n");

        return;
}

int main()
{
        int test;
        scanf("%d", &test); REP(i,test) execute(i+1);
        return 0;
}
