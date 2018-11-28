//
//  A.cpp
//  GoogleCodeJam
//
//  Created by Bakhodir Ashirmatov on 5/26/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

long long dist[10001], len[10001];
long long dp[10001];
bool dost[10001];

int main(){
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int t;
    cin>>t;
    //scanf("%d", &t);
    
    for (int ti=0; ti<t; ti++){
        
        int n;
        cin>>n;
        
        for (int i=0; i<n; i++){
            cin>>dist[i]>>len[i];
            dost[i] = false;
        }
        
        long long D;
        cin>>D;
        
        dist[n] = D;
        len[n] = 2*D;
        dost[n] = false;
        
        dp[0] = dist[0];
        dost[0] = true;
        
        for (int i=1; i<=n; i++){
            dp[i] = 0;
            for (int j=0; j<i; j++){
                if (dp[j] + dist[j] >= dist[i] && dp[i] < min(len[i], dist[i] - dist[j]) && dost[j]){
                    dp[i] = min(len[i], dist[i] - dist[j]);
                    dost[i] = true;
                }
            }
        }
        
        
        cout<<"Case #"<<ti+1<<": ";
        //printf("Case #1: ");
        
        if (dost[n])
            cout<<"YES";
        else {
            cout<<"NO";
        }

        cout<<endl;
        //printf("\n");
    }
}
             
             
             
             
             
             
             
             
             
             
             
             
             


