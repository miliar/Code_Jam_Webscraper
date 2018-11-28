//
//  2B.cpp
//  GoogleCodeJam
//
//  Created by Bakhodir Ashirmatov on 4/28/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

struct point {
    int a, b;
};

point p[1000];
bool ua[1000], ub[1000]={0};

bool cmp(point x, point y){
    return x.b>y.b;
}

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int T;
    cin>>T;
    for (int t=0; t<T; t++){
        int n;
        scanf("%d", &n);
        for (int i=0; i<n; i++){
            scanf("%d %d", &p[i].a, &p[i].b);
            ua[i]=ub[i]=false;
        }
        
        sort(p, p+n, cmp);
        
        int cnt=0, bestcnt=0, pointcnt=0;
        while (bestcnt<n){
            bool found=false;
            
            for (int i=0; i<n; i++){
                if (!ub[i] && pointcnt>=p[i].b && !found){
                    ub[i]=true;
                    if (!ua[i])
                        pointcnt+=2;
                    else
                        pointcnt++;
                    bestcnt++;
                    cnt++;
                    found=true;
                }
            }
            
            for (int i=0; i<n; i++){
                if (!ua[i] && !ub[i] && pointcnt>=p[i].a && !found){
                    ua[i]=true;
                    pointcnt++;
                    cnt++;
                    found=true;
                }
            }
            
            if (!found)
                break;          
        }
        
        if (bestcnt<n)
            printf("Case #%d: Too Bad\n", t+1);
        else     
            printf("Case #%d: %d\n", t+1, cnt);
    }
}

