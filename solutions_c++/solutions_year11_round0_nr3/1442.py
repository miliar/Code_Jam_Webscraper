/* 
 * File:   main.cpp
 * Author: perpetuity
 *
 * Created on 2011年5月7日, 上午8:52
 */

#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

/*
 * 
 */
int a[1001];

int main(int argc, char** argv) {
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        sort(a,a+n);
        int sum=0,s=0;
        for(int i=0;i<n;i++){
            sum=sum^a[i];
            s+=a[i];
        }
        if(sum!=0) printf("Case #%d: NO\n",cas);
        else printf("Case #%d: %d\n",cas,s-a[0]);
    }
    return 0;
}

