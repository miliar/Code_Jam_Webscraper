/*
 * Author: NomadThanatos
 * Created Time:  2011/5/7 17:16:36
 * File Name: D.cpp
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

int main() {
    freopen("D.out","w",stdout);
    int N;
    scanf("%d",&N);
    int t = 0;
    while(scanf("%d",&N) == 1) {
        int res = 0;
        for(int i = 1 ; i < N + 1 ; i++) {
            int val;
            scanf("%d",&val);
            if (val != i) res++;
        }
        printf("Case #%d: %d\n",t + 1,res);
        t++;
    }
    
    return 0;
}

