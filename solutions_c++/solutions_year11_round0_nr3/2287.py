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
int main(int argc, char** argv) {
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for (int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        int sum=0,s=0;
        int min1=~0u>>1;
        int x=0;
        int k; scanf("%d",&k);
        while (k--){
            scanf("%d",&x);
            s^=x;
            sum+=x;
            min1=min(min1,x);
        }
        if(s==0){
            printf("%d\n",sum-min1);
        }else{
            printf("NO\n");
        }
    }
    return 0;
}

