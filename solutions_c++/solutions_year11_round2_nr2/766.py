#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;
#define clr(x,y) memset(x,y,sizeof(x));
const int maxn=205;
double p[maxn],d;
int v[maxn];
int c;
bool check(double mid){
    double flag=0;
    flag=p[0]-mid;
    for (int i=0;i<c;i++){
        int m=v[i];
        if (i==0)
            m--;
        while (m--){
            flag+=d;
            double L=p[i]-mid;
            double R=p[i]+mid;
            if (L<=flag && flag<=R)
                continue;
            if (flag<L)
                flag=L;
            if (flag>R)
                return 0;
        }
    }
    return 1;
}
int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T; cin>>T;
    for (int t=1;t<=T;t++){
        printf("Case #%d: ",t);
        cin>>c>>d;
        for (int i=0;i<c;i++)
            cin>>p[i]>>v[i];
        double L=0,R=10e12;
        while (R-L>(1e-6)){
            double mid=(R+L)/2;
            if (check(mid))
                R=mid;
            else
                L=mid;
        }
        double res=(L+R)/2;
        printf("%f\n",res);
    }
    return 0;
}

