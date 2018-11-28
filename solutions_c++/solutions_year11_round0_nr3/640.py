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

int t;

int main(){
    scanf("%d",&t);
    for (int c=0;c<t;c++){
        int n;
        int v[2000];
        scanf("%d",&n);
        for (int i=0;i<n;i++) scanf("%d",&v[i]);
        int b=v[0];
        for (int i=1;i<n;i++) b=b^v[i];
        if (b!=0) {printf("Case #%d: NO\n",c+1); continue;}
        int minz=v[0];
        int sum=0;
        for (int i=0;i<n;i++){
            minz=min(minz,v[i]);
            sum+=v[i];
            }
        int res=sum-minz;
        printf("Case #%d: %d\n",c+1,res);
        }
    return 0;
    }
