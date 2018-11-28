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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <string>
using namespace std;
int a[1005];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int T,n;
    cin>>T;
    int t=1;
    while(T--){
        cin>>n;
        for(int i=1;i<=n;i++) cin>>a[i];
        double ans=0;
        for(int i=1;i<=n;i++){
            if(a[i]!=i) ans+=1.0;
        }
        printf("Case #%d: ",t++);
        printf("%.6lf\n",ans);
    }
    return 0;
}
