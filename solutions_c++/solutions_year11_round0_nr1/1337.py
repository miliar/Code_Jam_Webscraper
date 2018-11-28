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
        int a[n], b[n];
        for (int i=0;i<n;i++){
          char rot[10]; int pos;
          scanf("%s%d", rot, &pos);
          a[i] = rot[0]=='O';
          b[i] = pos;
        }
        int r1 = 1, r2 = 1;
        int t1 = 0, t2 = 0;
        int curr = 0;

        int t, diff;
        for (int i=0;i<n;i++){
          if (a[i]==0){
            t = abs(r1-b[i]);
            diff = t1+t - curr;
            if (diff<0) diff = 0;
            curr += diff + 1;

            r1 = b[i];
            t1 = curr;
          }else{
            t = abs(r2-b[i]);
            diff = t2+t - curr;
            if (diff<0)diff=0;
            curr += diff + 1;

            r2 = b[i];
            t2 = curr;
          }
        }

        printf("Case #%d: %d\n",ti,curr);
        
    }
    return 0;
}

