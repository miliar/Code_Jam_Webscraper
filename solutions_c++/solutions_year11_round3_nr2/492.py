#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;
int T;
int main(){
    scanf("%d",&T);
    for (int T1=0;T1<T;T1++){
        int a[2000];
        int l,n,c;
        long long t;
        scanf("%d %I64d %d %d",&l,&t,&n,&c);
        for (int i=0;i<c;i++) scanf("%d",&a[i]);
        long long res=0;
        vector<int> v;
        for (int i=0;i<n;i++){
            if (res+2*a[i%c]<=t) {res=res+2*a[i%c]; continue;}
            long long t1=t;
            t=t-res;
            res=t1;
            v.push_back(a[i%c]-t/2);
            for (int j=i+1;j<n;j++) {v.push_back(a[j%c]);}
            break;
            }
        sort(v.begin(),v.end());
        int st=0;
        for (int i=v.size()-1;i>=0;i--){
            st++;
            if (st<=l) res=res+v[i]; else res=res+2*v[i];
            }
        printf("Case #%d: %I64d\n",T1+1,res);
        }
    return 0;
    }
