#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
using namespace std;

int a[5];
int n;

int calcgcd(int x,int y)
{
    if (x < y) swap(x,y);
    if (!x) return y;
    if (!y) return x;
    if (x & 1 && y & 1) return calcgcd((x - y)/2,y);
    if (x & 1) return calcgcd(x,y/2);
    else if (y & 1) return calcgcd(x/2,y);
    return 2 * calcgcd(x/2,y/2);
};

int main()
{
    freopen("b1.in","r",stdin);
    freopen("b1.ou","w",stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        printf("Case #%d: ", it);
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", &a[i]);
        vector<int> delta;
        for (int i = 0; i < n; i++) if (a[0] != a[i]) delta.push_back(abs(a[0] - a[i]));
        int gcd = 0;
        for (int i = 0; i < delta.size(); i++) gcd = calcgcd(gcd,delta[i]);
//        cout << "div " << gcd << endl;
        
        int ret = 0;
        for (int i = 0; i < n; i++)
        {
            int t = a[i]/gcd;
            if (a[i] % gcd) t++;
            ret = max(ret,t * gcd - a[i]);            
        };
        printf("%d\n", ret);
    };
};
