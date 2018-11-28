#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n; scanf("%d", &n);
        int a[n];
        int x = 0, sum=0;
        int m = 1<<28;
        for (int i=0;i<n;i++){
          scanf("%d", &a[i]);
          x = x ^ a[i];
          if (a[i] < m)m=a[i];
          sum += a[i];
        }
        if (x==0){
          printf("Case #%d: %d\n",ti,sum-m);
        }else{
          printf("Case #%d: NO\n",ti);
        }
        
    }
    return 0;
}

