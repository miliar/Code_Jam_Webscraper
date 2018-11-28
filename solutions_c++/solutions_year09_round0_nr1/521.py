/*************************************************************************
Author: aMR
Created Time: 2009-9-3 14:06:18
File Name: a.cpp
Description: 
************************************************************************/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
using namespace std;
#define out(x) (cout<<#x<<": "<<x<<endl)
const int inf=0x7fffffff;
int L, D, N;
char dic[5010][20];
char tmp[5010];

inline bool isalp(char c) {
    return 'a' <= c && c <= 'z';
}

bool check(int x) {
    for(int i=0, pos=0; i<L; ++i, ++pos) {
        if(isalp(tmp[pos])) {
            if(tmp[pos] == dic[x][i])
                continue;
            return false;
        } else if(tmp[pos] == '(') {
            bool ok = false;
            while(true) {
                ++ pos;
                if(tmp[pos] == ')') break;
                if(tmp[pos] == dic[x][i])
                    ok = true;
            }
            if(ok) continue;
            return false;
        }
    }
    return true;
}

int count() {
    int ret = 0;
    for(int i=0; i<D; ++i) {
        if(check(i))
            ++ret;
    }
    return ret;
}

int main()
{
    freopen("a.txt", "w", stdout);
    while(scanf("%d%d%d", &L, &D, &N) == 3) {
        for(int i=0; i<D; ++i)
            scanf("%s", dic[i]);
        for(int i=1; i<=N; ++i) {
            scanf("%s", tmp);
            int ans = count();
            printf("Case #%d: %d\n", i, ans);
        }
    }
    return 0;
}
