/*************************************************************************
Author: aMR
Created Time: 2009/9/27 0:03:12
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
const int maxint=0x7FFFFFFF;
const int maxn = 110;
int d[maxn];
char tmp[maxn];
int main()
{
    int z, n, ca=0;
    freopen("a.txt", "w", stdout);
    scanf("%d", &z);
    while(z--) {
        scanf("%d", &n);
        for(int i=0; i<n; ++i) {
            scanf("%s", tmp);
            int t = 0;
            for(int j=0; j<n; ++j) {
                if(tmp[j] == '1')
                    t = j;
            }
            d[i] = t;
        }
        int ans = 0;
        for(int i=0; i<n; ++i) {
            if(d[i] <= i) continue;
            int t;
            for(int j=i+1; j<n; ++j) {
                if(d[j] <= i) {
                    t = j;
                    break;
                }
            }
            int k = d[t];
            for(int j=t; j>i; --j) {
                d[j] = d[j-1];
                ++ans;
            }
            d[i] = k;
        }
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}

