/*************************************************************************
Author: aMR
Created Time: 2010/5/23 0:51:56
File Name: b.cpp
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
const int maxint=0x7FFFFFFF;
typedef long long lint;
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

int n, k, b, t;
int x[100], v[100], fin[100];

void work() {
    int cnt = 0, ans = 0, num = 0;
    for(int i=n-1; i>=0 && num < k; --i) {
        if(fin[i] < b) {
            ++ cnt;
            continue;
        }
        ans += cnt;
        ++ num;
    }
    if(num < k) {
        puts("IMPOSSIBLE");
    } else {
        printf("%d\n", ans);
    }
}

int main()
{
    int z;
    cin >> z;
    for(int ca=1; ca<=z; ++ca) {
        cin >> n >> k >> b >> t;
        for(int i=0; i<n; ++i) {
            cin >> x[i];
        }
        for(int i=0; i<n; ++i) {
            cin >> v[i];
        }
        for(int i=0; i<n; ++i) {
            fin[i] = x[i] + v[i] * t;
        }
        printf("Case #%d: ", ca);
        work();
    }
    return 0;
}

