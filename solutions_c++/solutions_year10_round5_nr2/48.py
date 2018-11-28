#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

long long dis[100000],s[100000];
int q[10000000];
bool inq[10000000];
long long a[100];
int n;
long long len;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    cin >> T;
    for (int casenum=1;casenum<=T;casenum++)
    {
        printf("Case #%d: ",casenum);
        cin >> len; cin >> n; long long Max=0;
        for (int i=0;i<n;i++) {cin >> a[i];Max=max(Max,a[i]);}
        for (int i=0;i<Max;i++) dis[i]=-1;
        dis[len % Max]=0;
        s[len % Max]=0;
        int t=1,w=1;
        q[t]=len % Max;
        while (t<=w)
        {
            int now=q[t++]; inq[now]=false; 
            for (int i=0;i<n;i++)
               if (dis[(now - a[i]+Max) % Max]==-1 || dis[now]+1-dis[(now - a[i]+Max) % Max]<(s[now]+a[i]-s[(now - a[i]+Max) % Max])/Max)
                   {
                    dis[(now - a[i]+Max) % Max]=dis[now]+1;
                    s[(now - a[i]+Max) % Max]=s[now]+a[i];
                    if (!inq[(now - a[i]+Max) % Max])
                    {
                        q[++w]=(now - a[i]+Max) % Max;
                        inq[(now - a[i]+Max) % Max]=true;
                    }
                }
        }
        if (dis[0]==-1) cout << "IMPOSSIBLE" << endl;
            else cout << (len-s[0])/Max+dis[0] <<endl; 
    }
}
