#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#define INF 99999999
using namespace std;

long long test,K,M,H,N,kase;


int main()
{
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        cin>>N>>K;
        M = (1<<N);
        if(K%M==M-1)printf("Case #%lld: ON\n",++kase);
        else printf("Case #%lld: OFF\n",++kase);
    }
    return 0;
}
