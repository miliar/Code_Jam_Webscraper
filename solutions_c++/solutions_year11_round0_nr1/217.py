#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
#define N 111
int n;
struct node{
    char who;
    int op;
}robot[N];
int main(){
    int i,j,k;
    int cas,ans;
    char cc;
    int p,q,r;
    int posa,posb;
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    scanf("%d",&cas);
    for(k = 1; k <= cas; k++){
        ans = 0; p = 1; q = 1;
        posa = posb = 1;
        scanf("%d",&n);
        for(i = 1; i <= n; i++) scanf(" %c %d",&robot[i].who,&robot[i].op);
        while(p <= n && robot[p].who != 'O') p++;
        while(q <= n && robot[q].who == 'O') q++;
        while(p <= n || q <= n){
            if(p < q){
                r = abs(posa-robot[p].op) + 1;
                if(abs(posb-robot[q].op) <= r) posb = robot[q].op;
                else if(posb > robot[q].op) posb -= r;
                else posb += r;
                ans = ans + r;
                posa = robot[p].op; p++;
                while(p <= n && robot[p].who != 'O') p++;
            }
            else{
                r = abs(posb-robot[q].op) + 1;
                if(abs(posa-robot[p].op) <= r) posa = robot[p].op;
                else if(posa > robot[p].op) posa -= r;
                else posa += r;
                ans = ans + r;
                posb = robot[q].op; q++;
                while(q <= n && robot[q].who == 'O') q++;
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
