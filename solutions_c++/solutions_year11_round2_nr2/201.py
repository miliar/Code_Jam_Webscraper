/**********************************************************************
Author: hanshuai
Created Time:  2011/5/22 0:38:37
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
const int maxn = 205;
typedef long long LL;
const LL INF = (LL)1e15;
pair<int,int> a[maxn];
int C, D;
bool ok(LL ti){
    LL pre = -INF;
    for(int i = 0; i < C; i ++){
        LL cur = max(pre+D, (LL)a[i].first-ti);
        LL cur2 = cur + (LL)D*(a[i].second-1);
        if(cur2 > a[i].first+ti) return false;
        pre = cur2;
    }
    return true;
}
int main() {
    freopen("b.out", "w", stdout);
    int cas = 0, test;
    scanf("%d", &test);
    while(test--){
        scanf("%d%d", &C, &D);
        D *= 2;
        for(int i = 0; i < C; i ++){
            scanf("%d%d", &a[i].first, &a[i].second);
            a[i].first *= 2;
        }
        LL l = 0, r = INF, ans = -1;
        while(l <= r){
            LL mid = (l + r)/2;
            if(ok(mid)){
                r = mid - 1;
                ans = mid;
            }else l = mid + 1;
        }
//        cout << ans << endl;
        cout << "Case #" << (++cas) << ": ";
        cout << ans/2;
        if(ans&1) cout << ".5";
        cout << endl;
    }
    return 0;
}

