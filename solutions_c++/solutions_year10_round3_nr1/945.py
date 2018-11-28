// gcj A1.cpp
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

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int c = 1; c <= T; c++)
    {
        int N;
        cin >> N;
        int ans = 0;
        printf("Case #%d: ", c);
        vector< pair<int, int> > vp;
        for(int i = 0; i < N; i++)
        {
            int a, b;
            cin >> a >> b;
            vp.push_back(make_pair(a, b));
        }
        for(int i = 0; i < vp.size(); i++)
        {
            for(int j = i + 1; j < vp.size(); j++)
            {
                int a1 = vp[i].first,b1 = vp[i].second,
                a2 = vp[j].first,
                b2 = vp[j].second;
        if( a1 - a2 > 0 && b1 - b2 < 0 )
                ans++;
        else if( a1 - a2 < 0 && b1 - b2 > 0 )
                ans++;
            }
        }
        cout << ans;
        printf("\n");
    }
    return 0;
}
