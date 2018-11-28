#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>

using namespace std;

#define INF 1<<28
#define SIZE 10000

#define REP(i,n) for (int i=0; i<n; ++i)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (int i=p; i<=k; ++i)

#define MP(a,b) make_pair(a,b)

#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) (int)x.size()
#define PB push_back

#define gcd(a,b)    __gcd(a,b)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<string> vs;
typedef map<string,int> msi;


int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int i,j,cnt,test,m,n,Case=1,a,b;
    vi x,y;

    scanf("%d",&test);

    while(test--)
    {
        scanf("%d",&n);
        x.clear();
        y.clear();
        for(i=0;i<n;i++)
        {
            scanf("%d %d",&a,&b);
            x.push_back(a);
            y.push_back(b);
        }
        cnt=0;
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if((x[i]>x[j] && y[i] <y[j]) || (x[i]<x[j] && y[i]>y[j]))
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",Case++,cnt);
    }

    return 0;
}
