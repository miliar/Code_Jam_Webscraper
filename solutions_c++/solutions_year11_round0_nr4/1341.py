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
        for (int i=0;i<n;i++){
          scanf("%d", &a[i]);
          a[i]--;
        }
        int ans=0;
        for (int i=0;i<n;i++){
          if (a[i]!=i){
            ans++;
          }
        }
        
        printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}

