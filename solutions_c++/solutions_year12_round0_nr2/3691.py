#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n,s,p;
        scanf("%d%d%d", &n, &s, &p);
        int ans=0;
        int p1 = max(p, p*3-2);
        int p2 = max(p, p*3-4);

        for (int i=0;i<n;i++){
            int score;
            scanf("%d", &score);
            if (score >= p1){ // normal range
                ans++;
            }else if (s>0 && score >= p2){ //sup
                s--;
                ans++;
            }
        }
        printf("Case #%d: %d\n",ti,ans);
    }
    return 0;
}

