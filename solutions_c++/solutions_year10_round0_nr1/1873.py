#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf


int main()
{
    int t;
    sf("%d",&t);
    int kase=1;
    while ( t--)
    {
        int n,k;
        sf("%d %d",&n,&k);
        int val = (1<<n) - 1;
        if ( (k & val) == val )
            pf("Case #%d: ON\n",kase++);
        else
            pf("Case #%d: OFF\n",kase++);
    }
    return 0;
}
