#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define mp make_pair
#define sz(x) x.size()
using namespace std;

typedef long long ll;

int a[200];
int b[200][300];


int main(void){int tt, t, D, I, m, n, i, j, k;
    
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    fo(tt,t){
             scanf("%d%d%d%d", &D, &I, &m, &n);
             fo(i,n)scanf("%d", &a[i]);
             
             fo(i,n){
                     fo(j,256){
                              //amis washla tviton 
                              if (!i) b[i][j] = D + I; else b[i][j] = b[i-1][j] + D;
                              
                              //wina kvelas washla
                              b[i][j] = min(b[i][j], D*i + abs(j-a[i]));
                              b[i][j] = min(b[i][j], D*i + D + I);
                              
                              //amis shecvla j mdeda wina k
                              if (i){
                                     fo(k, (m+1)){
                                           if (j+k < 256) b[i][j] = min(b[i][j], b[i-1][j+k] + abs(j-a[i]));
                                           if (j-k > -1) b[i][j] = min(b[i][j], b[i-1][j-k] + abs(j-a[i]));
                                           // imis xarjze rom boloshi ukve damatebuli maqvs
                                           }
                                     }
                              }
                              
                     //boloshi chamatebebit gaumjobeseba tu sheidzleba, j ti k and k ti j
                     if (m!=0){
                     fo(k,256){
                               int btw = 0;
                               for(j=k+1;j<256;j++){
                                        if ((j-k) != 1 && (j-k-1) % m == 0) btw ++;
                                        
                                        b[i][j] = min(b[i][j], b[i][k] + (1+btw) * I);
                                        b[i][k] = min(b[i][k], b[i][j] + (1+btw) * I); 
                                        }
                               }
                     }                     
                     }
             
             int ans = D*n;
             fo(j,256){
                       ans = min(ans, b[n-1][j]);
                       }
             cout << "Case #" << tt+1 << ": " << ans << endl;
    }   
    return 0;
}
