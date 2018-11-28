/*
 * Author: NomadThanatos
 * Created Time:  2011/5/7 15:14:00
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>

using namespace std;

#define SZ(v) ((int)(v).size())
const int MAXINT = -1u>>1;
const int MAXN = 1000000 + 1;

string out;

int main() {
    freopen("C.out","w",stdout);
    
    int N;
    scanf("%d",&N);
    int t = 0;
    while(scanf("%d",&N) == 1) {
        int res = -MAXN,can = 0,minm = MAXN;
        for(int i = 0 ; i < N ; i++) {
            int val;
            scanf("%d",&val);
            can ^= val;
            if (val < minm) {
                res += minm;
                minm = val;
            }
            else {
                res += val;
            }
        }
        
        if (!can) {
            printf("Case #%d: %d\n",t + 1,res);
        }
        else {
            printf("Case #%d: NO\n",t + 1);
        }
        t++;
    }
    return 0;
}

