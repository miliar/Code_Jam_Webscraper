/* 
 * File:   main.cpp
 * Author: NIKUNJ
 *
 * Created on May 7, 2011, 3:43 PM
 */

#include <vector>
#include <string>
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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>

using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second

typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;


/*
 * 
 */
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t=SS;
    REP(i,t)
    {
        int n=SS,flag=0;
        VI candy(n);
        REP(j,n)
        candy[j]=SS;
        int sum=accumulate(ALL(candy),0);
        int no=pow(2.0,n-1),s1=0,s2=0,maxi=0;
        //REP(j,no)
        FOR(j,1,no)
        {
            int k=j,sum1=0;
            s1=s2=0;
            REP(m,n)
            {
                if(k&1)
                {
                    s1^=candy[m];
                    sum1+=candy[m];
                }
                else
                    s2^=candy[m];
                k>>=1;
            }
            if(s1==s2)
            {
                maxi=max(maxi,max(sum1,sum-sum1));
                flag=1;
            }
        }
        if(flag)
        {
            printf("Case #%d: %d\n",i+1,maxi);
        }
        else
            printf("Case #%d: NO\n",i+1);
    }
    fclose(stdout);
    return 0;
}

