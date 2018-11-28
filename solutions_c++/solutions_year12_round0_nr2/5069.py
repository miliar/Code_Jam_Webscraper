/*
 * Author:  xioumu
 * Created Time:  2012-4-14 12:55:36
 * File Name: b.cpp
 * solve: b.cpp
 */
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
#define esp 1e-8
#define maxn 1007
typedef long long int64;
int a[maxn];
int n, s, q;
int main(){
    int t;
    freopen("b.out","w",stdout);
    scanf("%d",&t);
    for(int ii = 1; ii<=t; ii++){
        int ans = 0;
        scanf("%d %d %d",&n,&s,&q);
        for(int i=1; i<=n; i++){
            int k,r,w,h = 0, n1 = 0, n2 = 0;
            scanf("%d",&h);
            k = h / 3;
            w = h % 3;
            if(w == 2 && s > 0) { n1 = k + 2; n2 = k + 1;}
            else if(w == 2) n2 = k + 1;
            
            if(w == 1 && k > 0 && s > 0) { n1 = k + 2; n2 = k + 1; }
            else if(w == 1) n2 = k + 1;
            
            if(w == 0 && k > 0 && s > 0) { n1 = k + 1; n2 = k;}
            else if(w == 0){
                n2 = k;
            }
            
            if(n2 >= q)  ans++;
            else if(n1 >= q){
                ans++;
                s--;
            }
        }
        printf("Case #%d: %d",ii,ans);
        if(ii != t) printf("\n");
    }
    return 0; 
}
