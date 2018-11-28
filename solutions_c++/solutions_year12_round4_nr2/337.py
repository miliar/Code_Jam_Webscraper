//
//  pb.cpp
//  
//
//  Created by mac on 12/5/26.
//  Copyright (c) 2012年 __MyCompanyName__. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <algorithm>

int n, W, L;
int ID[1010];
long long r[1010];
double px[1010], py[1010];

bool cmp(const int &a, const int &b) {
    return (r[a] > r[b]);
}

double Dist(int i, int j) {
    double dx = px[i]-px[j];
    double dy = py[i]-py[j];
    return sqrt(dx*dx+dy*dy);
}

int main() {
    int t, cases=0;
    srand(time(NULL));
    
    scanf("%d",&t);
    while(t--) {
        scanf("%d%d%d",&n,&W,&L);
        for(int i=0;i<n;++i)
            scanf("%lld",r+i);
        for(int i=0;i<n;++i)
            ID[i] = i;
        std::sort(ID, ID+n, cmp);

        while(1) {
            bool yes = false;
            for(int i=0;i<n;++i) {
                while(1) {
                    px[ID[i]] = (rand()%((W+1)*100))/100;
                    py[ID[i]] = (rand()%((L+1)*100))/100;
                    //printf("%d %.3lf %.3lf\n",i,px[i],py[i]);
                    //scanf("%*d");
                    bool valid = true;

                    for(int j=0;j<i;++j) {                                                    //printf("%.3lf %lld\n",Dist(i,j),r[i]+r[j]);
                        if( Dist(ID[i],ID[j]) < r[ID[i]]+r[ID[j]] ) {
                            valid = false;
                            break;
                        }
                    }
                    if(valid) {
                        yes = true;
                        break;
                    }
                }
            }
            if(yes) break;
        }
        
        printf("Case #%d:",++cases);
        for(int i=0;i<n;++i)
            printf(" %.3lf %.3lf",px[i], py[i]);
        puts("");
    }
    
    return 0;
}
