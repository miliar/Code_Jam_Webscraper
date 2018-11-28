/*
 * File:   joj2679.cpp
 * Author: 1025bit
 *
 * Created on 2010年6月1日, 下午6:52
 */

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
using namespace std;
int n,L,H;
int a[10005];
int check(){
    for (int i=L;i<=H;i++){
        int flag=1;
        for (int j=0;j<n;j++){
            if (a[j]%i!=0 && i%a[j]!=0){
                flag=0;
                break;
            }
        }
        if (flag)
            return i;
    }
    return -1;
}
int main(int argc, char** argv) {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for (int t=1;t<=T;t++){
        printf("Case #%d: ",t);
        scanf("%d%d%d",&n,&L,&H);
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        int res=check();
        if (res==-1)
            printf("NO\n");
        else
            printf("%d\n",res);
    }
    return 0;
}

