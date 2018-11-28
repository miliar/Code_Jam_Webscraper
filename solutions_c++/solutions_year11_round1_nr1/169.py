#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;

LL t, pd, pg;

int possiblr() {
    if (pg == 0)
        return pd == 0;
    if (pg == 100)
        return pd == 100;
    for (int i = 1; i <= 100; i++)
        if (i <= t 
            && (i * pd / 100 * 100 == i * pd))
        return 1;
    return (t >= 100);
}


int main(){
    int caseNumber;
    scanf("%d", &caseNumber);
    //cin>>caseNumber;
    REP(caseN, caseNumber) {
        scanf("%lld%lld%lld", &t, &pd, &pg);
        //~ cout<<t;
        printf("Case #%d: ", caseN + 1);
        if (possiblr()) 
            puts("Possible");
        else 
            puts("Broken");
    }
    return 0;
}
