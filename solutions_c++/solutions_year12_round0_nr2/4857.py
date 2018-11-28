#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int T;

int main(){
    scanf("%d",&T);
    for (int t=0;t<T;t++){
        int n,s,p;
        int a[205];
        scanf("%d %d %d",&n,&s,&p);
        int res=0;
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        for (int i=0;i<n;i++){
            if (a[i]>=3*p-2) res++; else {
                if (a[i]==30||a[i]==29||a[i]==1||a[i]==0) continue;             
                if (s==0) continue;
                if (a[i]>=3*p-4) {res++; s--;}                             
               }
            }
        printf("Case #%d: %d\n",t+1,res);
        }
    return 0;
    }
