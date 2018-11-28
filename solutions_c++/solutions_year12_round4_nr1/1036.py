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
#include <cstdlib>
#include <ctime>
using namespace std;

bool solve(vector<int> d,vector<int> l,int D){
    int dp[10005]={0};
    dp[0]=d[0];
    for(int k=0;k<d.size();k++){
        for(int i=k+1;i<d.size();i++){
            if(d[i]-d[k]>dp[k]) break;
            dp[i]=max(dp[i],min(d[i]-d[k],l[i]));
        }
    }
    for(int i=0;i<d.size();i++)
        if(dp[i]+d[i]>=D) return 1;
    return 0;
}

int main() {
    int T;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        vector<int> d,l;
        int D,N,dz,lz;
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%d %d",&dz,&lz);
            d.push_back(dz);
            l.push_back(lz);
        }
        scanf("%d",&D);
        
        bool a=solve(d,l,D);
        
        printf("Case #%d: %s\n",t+1,a?"YES":"NO");
    }
    return 0;
}
