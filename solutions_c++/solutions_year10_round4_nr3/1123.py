/*************************************************************************
Author: aMR
Created Time: 2010/6/5 23:18:38
File Name: c.cpp
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
const int maxint=0x7FFFFFFF;
typedef long long lint;
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

char mp[110][110];
char tmp[110][110];

void out() {
    for(int i=1; i<8; ++i) {
        for(int j=1; j<8; ++j) {
            printf("%d", (int)mp[i][j]);
        }
        puts("");
    }
}

bool check() {
    for(int i=1; i<=100; ++i) {
        for(int j=1; j<=100; ++j) {
            if(mp[i][j]) return true;
        }
    }
    return false;
}

int calc() {
    for(int k=0; ; ++k) {
        if(!check()) {
            return k;
        }
        for(int i=1; i<=100; ++i) {
            for(int j=1; j<=100; ++j) {
                tmp[i][j] = mp[i][j];
                if(mp[i][j]) {
                    mp[i][j] = tmp[i-1][j] || tmp[i][j-1];
                } else {
                    mp[i][j] = tmp[i-1][j] && tmp[i][j-1];
                }
            }
        }
    }
}
int main()
{
    int z;
    scanf("%d", &z);
    for(int ca=1; ca <= z; ++ca) {
        int n;
        scanf("%d", &n);
        memset(mp, 0, sizeof(mp));
        memset(tmp, 0, sizeof(tmp));
        for(int k=0; k<n; ++k) {
            int x1, y1, x2, y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            if(x2 < x1) swap(x1, x2);
            if(y2 < y1) swap(y1, y2);
            for(int i=x1; i<=x2; ++i) {
                for(int j=y1; j<=y2; ++j) {
                    mp[i][j] = 1;
                    tmp[i][j] = 1;
                }
            }
        }
        printf("Case #%d: %d\n", ca, calc());
    }
    return 0;
}

