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
    for (int t=1;t<=T;t++){
        int f[20000];
        int n,l,h;
        scanf("%d %d %d",&n,&l,&h);
        for (int i=0;i<n;i++) scanf("%d",&f[i]);
        int res=-1;
        for (int i=l;i<=h;i++){
            bool b=true;
            for (int j=0;j<n;j++){
                if (i%f[j]!=0&&f[j]%i!=0) b=false;
                }
            if (b&&res==-1) res=i;
            }
        if (res>0) printf("Case #%d: %d\n",t,res); else printf("Case #%d: NO\n",t);
        }
    return 0;
    }
