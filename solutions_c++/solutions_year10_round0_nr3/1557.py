/*
 * Author: SmartEgg
 * Created Time:  2010/5/8 12:06:03
 * File Name: code.cpp
 */
#include <iostream>
#include<sstream>
#include<algorithm>
#include<functional>
#include<string>
#include<numeric>
#include<set>
#include<map>
#include<queue>
#include<vector>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<assert.h>
using namespace std;
//MACROS START
#define FOR(i,t,n)  for(int i=(t);i< (n);i++)
#define FORE(i,t,n) for(int i=(t);i<=(n);i++)
#define FORB(i,t,n) for(int i=(t);i>=(n);i--)
#define dbg(n) cout<<#n <<"     "<<(n)<<endl;
#define dbg2(x,y) cout<<#x<<"\t"<<(x)<<"\t"<<#y<<"\t"<<(y)<<endl;
//MACROS END
int R,K,N;
int a[1<<11];
int pos[1<<10];
long long wt[1<<10];

int main() {
    int T;
    int cnt = 0;
    freopen("code2.out","w",stdout);
    freopen("C-large.in","r",stdin);
    scanf("%d",&T);
    while(T--){
        scanf("%d %d %d",&R ,&K,&N);
        FOR(i,0,N)    scanf("%d",a+i);
        FOR(i,0,N)    a[i+N] = a[i];
        FOR(i,0,N){
            long long t = 0;
            int j = i;
            for(;;){
                t += a[j];
                if(t> K ) break;
                j = (j+1)%N;
                if( j == i){
                    t+=a[j];
                    break;
                }
            }
            pos[i] = j;
            wt[i]  = t - a[j];
        }

       /* FOR(i,0,N){
            dbg2(pos[i],wt[i]);
        }*/
        long long  cur = 0,ans = 0;
        FOR(i,0,R){
            ans +=wt[cur];
            cur = pos[cur];
        }
        printf("Case #%d: %I64d\n",++cnt,ans);
        
    }
    return 0;
}

