#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>
#include<cassert>
#define dbge( x ) cout << #x << " : " <<  x << endl;
using namespace std;


int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);
        int n, l, h;
        cin >> n >> l >> h;
        vector<int> v;
        for(int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            v.push_back(x);
        }
        int f = 0;
        int ans = 0;
        for(int i = l; i <= h; i++)
        {
            int valid = 1;
            for(int j = 0; j < n; j++)
            {
                if(v[j] % i == 0 || i % v[j] == 0)
                    ;
                else
                    valid = 0; 
            }
            if(valid == 1)
            {
                f = 1;
                ans = i;
                break;
            }
        }
        if(f)
            cout << ans << endl;
        else
            cout << "NO" << endl;

    }
    return 0;
}

