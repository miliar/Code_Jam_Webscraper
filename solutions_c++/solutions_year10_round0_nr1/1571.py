/*
 * Author: SmartEgg
 * Created Time:  2010/5/8 10:32:40
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

int main() {
    int T;
    int u,v;
    int cnt = 0;
    freopen("code222.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        scanf("%d %d",&u,&v) ;
        int mod = 1 << u;
        bool ok = v % mod ==((mod)-1) ? true:false;
        printf("Case #%d: %s\n",++cnt,ok?"ON":"OFF");
    }
    return 0;
}

