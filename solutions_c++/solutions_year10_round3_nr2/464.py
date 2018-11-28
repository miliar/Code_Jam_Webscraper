/* 
 * File:   main.cpp
 * Author: Kimi
 *
 * Created on 2010年5月23日, 下午5:48
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <climits>
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

/*
 *
 */
const string FILENAME="B-large";


int get(long long M, long long m, long long c)
{
    for (int i=0; ; i++) {
        if (m>=M) return i;
        m*=c;
    }
}

int main() {
    freopen((FILENAME+".in").c_str(),"r",stdin);
    freopen((FILENAME+".out").c_str(),"w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=0; t<T; t++) {
        int L,P,C;
        scanf("%d%d%d",&L,&P,&C);
        printf("Case #%d: %d\n",t+1,max(get(get(P,L,C),1,2),0));
//        printf("Case #%d: %d\n",t+1,max(int(ceil(log((log(P*1.0/L)/log(C)))/log(2))),0));
    }
    return (EXIT_SUCCESS);
}
