// gcj C1help.cpp
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
bool isPure(int n, vector<int> s);

int main()
{
    for(int i = 2; i <= 25; i++)
    {
        int ans = 0;
        vector<int> mset;
        for(int j = 2; j <= i; j++)
            mset.push_back(j);
        int ms = mset.size();
        for(int j = 1; j < (1 << ms); j++)
        {
            vector<int> tset;
            for(int k = 0, l = ms - 1; k < mset.size(); k++, l--)
            {
                if(j & (1 << l))
                    tset.push_back(mset[k]);
            }
            if(isPure(i, tset))
                ans++;
        }
        cout << ans << ", " << endl;
    }
    return 0;
}

bool isPure(int n, vector<int> s)
{
    int rank[n+1];
    memset(rank, 0, sizeof rank);
    for(int i = 0; i < s.size(); i++)
        rank[s[i]] = i + 1;
    int r = rank[n];
    while(r != 1)
    {
        r = rank[r];
        if(r == 0)
            return false;
    }
    return true;
}
