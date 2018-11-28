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
        scanf("%d",&n);
        double st=0.0;
        for (int i=0;i<n;i++) {
            int a;
            scanf("%d",&a);
            if (a-1!=i) st=st+1.0;
            }
        printf("Case #%d: %.6f\n",c+1,st);
        }
    return 0;
    }
