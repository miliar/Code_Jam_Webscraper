#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

void solve(int k)
{
    int n; cin >> n;
    vector<int> v;
    vector<int> sorted;
    for(int i=0;i<n;i++)
    {
        int tmp; cin >> tmp;
        v.push_back(tmp);
        sorted.push_back(tmp);
    }

    sort(sorted.begin(), sorted.end());

    int count = 0;
    for(int i=0;i<n;i++)
    {
        if(sorted[i] != v[i])
            count++;
    }
    printf("Case #%d: %.6f\n", k, (float) count);
}

int main()
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        solve(i+1);
    }
    return 0;
}


