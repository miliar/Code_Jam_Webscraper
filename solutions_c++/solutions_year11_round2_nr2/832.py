#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <climits>

double myabs(double x){
    return (x>0 ? x:-x);   
}
using namespace std;
typedef long long ll;
int n,ntest,c,d ,total;
int p[222], v[222];

bool test(ll x){
     double now = x*1.0/1000000;
     int temp = total - 1 ;
     double cur = p[0] - now;
     v[0] -- ;
     bool found = true; 
     for(int i = 0; i<c;i++){
        if (!found) break;
        for(int j = 0 ; j<v[i] ; j++){
           if ( myabs(p[i] - cur - d) <= now) 
             cur = cur + d;
             else  if (cur + d < p[i]) cur = p[i] - now;
             else {
                    found = false;
                    break;
                }
            temp --;
        }
    }
    v[0] ++;
    return (temp > 0 ? 0:1);
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);    
    cin >> ntest;
    for(int r = 0;r<ntest;r++){
        cout << "Case #"<< r+1 <<": " ;   
        
        cin >> c >> d;
        total = 0;
        for(int i = 0;i<c;i++) {
            cin >> p[i] >> v[i];
            total += v[i];
        }
        
        ll low = 0 , hi = ll(INT_MAX) * (ll) 1000000;
        
        while (low != hi){
            ll mid = (low + hi)/2;
            if (test(mid)) hi = mid; 
              else low = mid+1;   
        }
        printf("%.7lf\n",low*1.0/1000000);
    }   
    return 0;    
}
